import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def patch_file(target_path):
    print(f"[*] Aplicando correcciones en {target_path} ...")
    if not os.path.exists(target_path):
        print(f"[!] No existe: {target_path}")
        return False

    with open(target_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Corregir _is_dpapi_storage_candidate
    old_target = """        is_dpapi_share = (
            "protected_storage" in combined or
            "sensitive windows network share" in combined or
            ("network share" in combined and "ipc$" in combined) or
            ("windows_security_5145" in combined) or
            ("5145" in combined and "vmbase8" in combined)
        )
        return is_dpapi_share and ("vmbase8" in combined or "172.16.201.8" in combined or "protected_storage" in combined)"""

    new_target = """        return (
            "protected_storage" in combined or
            "sensitive windows network share" in combined or
            ("network share" in combined and "ipc$" in combined) or
            "windows_security_5145" in combined or
            ("5145" in combined and "share" in combined)
        )"""

    if old_target in content:
        content = content.replace(old_target, new_target)
        print("  [+] _is_dpapi_storage_candidate corregido exitosamente.")
    else:
        print("  [!] old_target de _is_dpapi_storage_candidate no encontrado exactamente.")

    # 2. Configurar auto-cierres activos por defecto (setChecked(True))
    old_defaults = """        self.action_soar_hm = QAction("Auto-Cierre HealthMailbox (Ley de Oro)", self)
        self.action_soar_hm.setCheckable(True)
        self.action_soar_hm.setChecked(False)
        self.action_soar_hm.setToolTip("Auto-toma y resuelve como False Positive los casos de HealthMailbox bajo la Ley de Oro")
        self.action_soar_hm.toggled.connect(self._update_soar_menu_label)

        self.action_soar_translate = QAction("Auto-Cierre Sophos Translate", self)
        self.action_soar_translate.setCheckable(True)
        self.action_soar_translate.setChecked(False)
        self.action_soar_translate.setToolTip("Auto-toma y resuelve como False Positive los casos de Sophos WebControl hacia translate.google.com")
        self.action_soar_translate.toggled.connect(self._update_soar_menu_label)

        self.action_soar_sati = QAction("Auto-Cierre SATI VPN (DNS 53 Failover)", self)
        self.action_soar_sati.setCheckable(True)
        self.action_soar_sati.setChecked(False)"""

    new_defaults = """        self.action_soar_hm = QAction("Auto-Cierre HealthMailbox (Ley de Oro)", self)
        self.action_soar_hm.setCheckable(True)
        self.action_soar_hm.setChecked(True)
        self.action_soar_hm.setToolTip("Auto-toma y resuelve como False Positive los casos de HealthMailbox bajo la Ley de Oro")
        self.action_soar_hm.toggled.connect(self._update_soar_menu_label)

        self.action_soar_translate = QAction("Auto-Cierre Sophos Translate", self)
        self.action_soar_translate.setCheckable(True)
        self.action_soar_translate.setChecked(True)
        self.action_soar_translate.setToolTip("Auto-toma y resuelve como False Positive los casos de Sophos WebControl hacia translate.google.com")
        self.action_soar_translate.toggled.connect(self._update_soar_menu_label)

        self.action_soar_sati = QAction("Auto-Cierre SATI VPN (DNS 53 Failover)", self)
        self.action_soar_sati.setCheckable(True)
        self.action_soar_sati.setChecked(True)"""

    if old_defaults in content:
        content = content.replace(old_defaults, new_defaults)
        print("  [+] Defaults de checkboxes SOAR configurados en True exitosamente.")
    else:
        print("  [!] old_defaults de checkboxes no encontrado exactamente.")

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Validar sintaxis
    import py_compile
    try:
        py_compile.compile(target_path, doraise=True)
        print(f"  [+] Compilacion py_compile OK para {target_path}")
        return True
    except Exception as e:
        print(f"  [!] Error de compilacion en {target_path}: {e}")
        return False

def main():
    paths = [
        r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py",
        r"c:\Users\kevinmoraes\Documents\soc-env\command_center.py"
    ]
    for p in paths:
        patch_file(p)

if __name__ == "__main__":
    main()
