import os
import sys
import winreg

def register_windows_explorer_menu():
    """Registers 'Open in OmniFile Radial Wheel' in Windows File Explorer Right-Click Menu."""
    exe_path = os.path.abspath(sys.argv[0])
    key_path = r"*\shell\OmniFileRadial"
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        winreg.SetValue(key, "", winreg.REG_SZ, "Open in OmniFile Radial Wheel")
        cmd_key = winreg.CreateKey(key, "command")
        winreg.SetValue(cmd_key, "", winreg.REG_SZ, f'"{exe_path}" "%1"')
        print("Successfully integrated with Windows File Explorer!")
    except PermissionError:
        print("Run as Administrator once to add to Windows Explorer right-click menu.")

if __name__ == "__main__":
    register_windows_explorer_menu()
