def test_candidate(case: dict):
    name = str(case.get("name", "")).lower()
    src_user = str(case.get("srcip_username") or "").lower()
    user = str(case.get("username") or case.get("user") or "").lower()
    tags = " ".join(str(t).lower() for t in case.get("tags", []))
    desc = str(case.get("description") or "").lower()
    combined = f"{name} {src_user} {user} {tags} {desc}"

    # HM
    is_hm = "healthmailbox" in combined
    # Translate
    is_translate = (
        "translate.google.com" in combined or
        "webcontrolviolation" in combined or
        ("user execution" in combined and "sophos" in combined)
    )
    # Sati
    is_sati = "sati" in combined and (
        "firewall denial" in combined or 
        "internal firewall denial" in combined or 
        "denial anomaly" in combined or 
        "policyid" in combined or
        "denial" in combined or
        "10.212.134" in combined or 
        "dns" in combined
    )
    # DPAPI
    is_dpapi = (
        "protected_storage" in combined or
        "sensitive windows network share" in combined or
        ("network share" in combined and "ipc$" in combined) or
        ("windows_security_5145" in combined) or
        ("5145" in combined and "vmbase8" in combined)
    ) and ("vmbase8" in combined or "172.16.201.8" in combined or "protected_storage" in combined)

    # Google Drive / AppSheet
    is_gdrive = (
        "cloud drive" in combined or
        "cloud_drive_data_exfiltration_anomaly" in combined or
        "google workspace" in combined or
        "drive.files.get" in combined or
        "appsheet" in combined or
        "appscript" in combined or
        "exfiltration anomaly" in combined
    )

    matches = []
    if is_hm: matches.append("HealthMailbox")
    if is_translate: matches.append("Sophos Translate")
    if is_sati: matches.append("SATI VPN")
    if is_dpapi: matches.append("DPAPI Storage")
    if is_gdrive: matches.append("Google Drive / AppSheet (GSuite)")

    if matches:
        print(f"  -> Candidate MATCHES: {', '.join(matches)}")
    else:
        print(f"  -> Candidate MATCHES: None (General Case)")
