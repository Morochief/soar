**Describe the bug**
During `sudo soup -y` upgrade (from SO 3.2.x to 3.3.0), the process consistently fails while copying large Docker images to the local embedded registry (`localhost:5000`), specifically:
- `ghcr.io/security-onion-solutions/so-elastic-fleet-package-registry:3.3.0` (~1.8 GB)
- `ghcr.io/security-onion-solutions/so-elasticsearch:9.4.5` (~1.5 GB)

The error logged in `/root/soup.log` is:
```text
#1 [internal] pushing soc-onion:5000/security-onion-solutions/so-elastic-fleet-package-registry
#1 ERROR: copy ... failed to copy: stream error: stream ID 3; PROTOCOL_ERROR; received from peer
Unable to copy so-elastic-fleet-package-registry:3.3.0 to embedded registry
Soup failed with error 1: Unhandled error
```

**To Reproduce**
Steps to reproduce the behavior:
1. Run `sudo soup -y` on an SO 3.x Standalone deployment to upgrade to 3.3.0.
2. Observe `soup` downloading container images.
3. When reaching large image layers (>500MB) such as `so-elastic-fleet-package-registry` or `so-elasticsearch`, the stream aborts with:
   `stream error: stream ID 3; PROTOCOL_ERROR; received from peer`.
4. `soup` exits with code 1.

**Expected behavior**
Large images should successfully copy to the local registry without HTTP/2 stream multiplexing drops, and in the event of transient errors, have a reliable fallback rather than an unhandled fatal abort.

**Root Cause**
In `salt/common/tools/sbin/so-image-common`:
```bash
docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF"
```
`docker-buildx` uses Go's HTTP client which defaults to HTTP/2 multiplexing. When uploading large blob streams to the local containerd/registry on localhost, the stream is terminated unexpectedly (`client disconnected during blob PUT`), causing a fatal `PROTOCOL_ERROR`.

**Proposed Fix**
1. Set `export GODEBUG="http2client=0${GODEBUG:+,${GODEBUG}}"` before `buildx imagetools` to force HTTP/1.1 sequential blob transfers without connection drops.
2. Add a fallback to `docker push` if `buildx imagetools` encounters transient stream errors:
```bash
docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF" >> "$LOG_FILE" 2>&1 || \
docker push $HOSTNAME:5000/$IMAGEREPO/$image >> "$LOG_FILE" 2>&1 || {
  echo "Unable to copy $image to embedded registry" >> "$LOG_FILE" 2>&1
  exit 1
}
```

Tested on a production Standalone deployment: all 24 official container images copied successfully (0.9s and 1.0s transfer times) and the upgrade completed without issues.
