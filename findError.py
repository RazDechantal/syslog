#!/usr/bin/env python3
import subprocess
import re

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error executing command:", result.stderr.strip())
            return None
    except Exception as e:
        print("Error:", e)
        return None

def main():
    # Read the sys.log file
    with open('error.log', 'r') as file:
        log_lines = file.readlines()

    info_messages = []
    error_messages = []

    # Define regular expression patterns for INFO and ERROR messages
    info_pattern = r"ticky: INFO: ([\w ]*) "
    error_pattern = r"ticky: ERROR: ([\w ]*) "

    # Search for INFO and ERROR messages in each line
    for line in log_lines:
        info_match = re.search(info_pattern, line)
        error_match = re.search(error_pattern, line)

        if info_match:
            info_messages.append(info_match.group(1))
        if error_match:
            error_messages.append(error_match.group(1))

    # Print the extracted messages
    print("INFO messages:")
    for message in info_messages:
        print(message)

    print("\nERROR messages:")
    for message in error_messages:
        print(message)

if __name__ == "__main__":
    main()
