import subprocess
from netmiko import ConnectHandler
import platform

def is_reachable(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(["ping", param, "2", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"[ERROR] Ping failed: {e}")
        return False

def run_show_commands(device_dict, command_list):
    if not is_reachable(device_dict["host"]):
        print(f"[ERROR] Cannot reach {device_dict['host']}")
        return

    try:
        connection = ConnectHandler(**device_dict)
        connection.enable()  # << ENABLE mode
        print(f"[INFO] Connected to {device_dict['host']} in enable mode")

        output = ""
        for cmd in command_list:
            print(f"[RUNNING] {cmd}")
            result = connection.send_command(cmd)
            output += result + "\n"
        print(output)
        connection.disconnect()
        print(f"[INFO] Disconnected from {device_dict['host']}")
    except Exception as e:
        print(f"[ERROR] SSH failed: {e}")

def run_config_commands(device_dict, config_list):
    if not is_reachable(device_dict["host"]):
        print(f"[ERROR] Cannot reach {device_dict['host']}")
        return

    try:
        connection = ConnectHandler(**device_dict)
        connection.enable()  # << ENABLE mode
        print(f"[CONFIG MODE] Sending config to {device_dict['host']}")

        output = connection.send_config_set(config_list)
        print(output)
        connection.disconnect()
    except Exception as e:
        print(f"[ERROR] Config SSH failed: {e}")
