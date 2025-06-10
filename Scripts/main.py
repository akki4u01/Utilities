import yaml
import configparser
import sys
import os
from utils.ssh_handler import run_config_commands, run_show_commands

# Ensure correct path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load device details
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

# Load commands
config = configparser.ConfigParser()
config.read("commands.ini")

def get_commands(section):
    try:
        return [v for k, v in config.items(section)]
    except Exception as e:
        print(f"[WARNING] Failed to load commands for section {section}: {e}")
        return []

# Results dictionary
test_results = []

# Generic test runner
def run_test_case(case_id, section, device, mode="config"):
    print(f"\n===== Running Test Case {case_id}: {section.replace('_', ' ').title()} =====")
    commands = get_commands(section)

    if not commands:
        print(f"[WARNING] Test Case {case_id}: SKIPPED — No commands found")
        test_results.append((case_id, "SKIPPED"))
        return

    try:
        if mode == "config":
            run_config_commands(device, commands)
        elif mode == "show":
            run_show_commands(device, commands)
        else:
            raise Exception("Invalid mode specified")

        print(f"[INFO] Test Case {case_id}: PASSED ✅")
        test_results.append((case_id, "PASSED"))
    except Exception as e:
        print(f"[WARNING] Test Case {case_id}: FAILED ❌ — Reason: {e}")
        test_results.append((case_id, "FAILED"))

# Select device
device = devices["router1"]

# Run test cases
run_test_case("TC1", "test_case_1", device, mode="config")
run_test_case("TC2", "test_case_2", device, mode="show")
run_test_case("TC3", "test_case_3", device, mode="config")

# Final Report
print("\n==================== Test Execution Summary ====================")
print(f"{'Test Case':<10} | {'Status':<10}")
print("-" * 30)

total = len(test_results)
passed = sum(1 for _, status in test_results if status == "PASSED")
failed = sum(1 for _, status in test_results if status == "FAILED")
skipped = sum(1 for _, status in test_results if status == "SKIPPED")

for tc, status in test_results:
    print(f"{tc:<10} | {status:<10}")

print("-" * 30)
print(f"TOTAL     : {total}")
print(f"PASSED    : {passed}")
print(f"FAILED    : {failed}")
print(f"SKIPPED   : {skipped}")
print("===============================================================\n")
