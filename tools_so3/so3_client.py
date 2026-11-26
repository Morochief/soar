#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SO3 SSH Client Wrapper
Proporciona conexión SSH autenticada y helpers para ejecutar comandos con sudo
en el servidor Security Onion 3 (172.17.10.25).
"""

import os
import sys
import shlex
import paramiko
from dotenv import load_dotenv

# Configurar salida segura en UTF-8 para PowerShell y Windows CMD
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Cargar variables de entorno si existen
load_dotenv()

SO3_HOST = os.getenv("SO3_HOST", "172.17.10.25")
SO3_USER = os.getenv("SO3_USER", "soc-admin")
SO3_PASS = os.getenv("SO3_PASS", "LMs0cZXhgds*")

class SO3Client:
    def __init__(self, host=SO3_HOST, user=SO3_USER, password=SO3_PASS):
        self.host = host
        self.user = user
        self.password = password
        self.client = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        if not self.client:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(
                hostname=self.host,
                username=self.user,
                password=self.password,
                timeout=15
            )
        return self.client

    def run(self, cmd):
        """Ejecuta un comando estándar."""
        self.connect()
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode("utf-8", errors="replace"), stderr.read().decode("utf-8", errors="replace")

    def sudo(self, cmd):
        """
        Ejecuta un comando COMPLETO con sudo.

        Antes se armaba `echo <pass> | sudo -S <cmd>`: con comandos compuestos
        (`a && b`, `a || b`, `a | b`) solo la primera parte corría como root. Ej.: en
        flush_swap.py `swapoff -a && swapon -a` ejecutaba `swapon` sin sudo, fallaba y dejaba
        el nodo sin swap. Ahora todo el comando corre dentro de `sudo bash -c '<cmd>'` y la
        contraseña se envía por stdin (no por `echo`, que se rompía con caracteres especiales).
        """
        self.connect()
        full_cmd = f"sudo -S -p '' bash -c {shlex.quote(cmd)}"
        stdin, stdout, stderr = self.client.exec_command(full_cmd)
        stdin.write(f"{self.password}\n")
        stdin.flush()
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        return out, err

    def read_file(self, remote_path):
        """Lee el contenido de un archivo remoto con permisos sudo."""
        out, _ = self.sudo(f"cat {shlex.quote(remote_path)}")
        return out

    def write_file(self, remote_path, content):
        """Escribe un archivo en el servidor remoto usando SFTP temporal + sudo mv."""
        self.connect()
        sftp = self.client.open_sftp()
        tmp_path = f"/tmp/so3_upload_{os.getpid()}"
        with sftp.file(tmp_path, "w") as f:
            f.write(content)
        sftp.close()
        
        self.sudo(f"mv {shlex.quote(tmp_path)} {shlex.quote(remote_path)} && chmod 644 {shlex.quote(remote_path)}")

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
