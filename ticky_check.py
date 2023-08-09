#!/usr/bin/env python3
import subprocess
import re
import csv
from collections import defaultdict

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

def extract_user(line):
    user_match = re.search(r"\((.*?)\)", line)
    if user_match:
        return user_match.group(1)
    return None

def main():
    # Read the sys.log file
    with open('syslog.log', 'r') as file:
        log_lines = file.readlines()

    error = defaultdict(int)
    per_user = defaultdict(lambda: {'INFO': 0, 'ERROR': 0})

    # Define regular expression patterns for INFO and ERROR messages
    info_pattern = r"INFO ([^\[]+) "
    error_pattern = r"ERROR (.*) \("

    # Process log lines to populate error and per_user dictionaries
    for line in log_lines:
        info_match = re.search(info_pattern, line)
        error_match = re.search(error_pattern, line)
        user = extract_user(line)
        #print("========= User: " + user + " =========")

        if info_match:
            if user:
                #print("INFO case: "+user)
                info_msg = info_match.group(1)
                #print(info_msg)
                per_user[user]['INFO'] += 1
                error[info_msg] += 1

        if error_match:
            #print("Error msg: " +error_msg)
            error_msg = error_match.group(1)
            error[error_msg] += 1
            if user:
                #print("ERROR case: "+user)
                error_msg = error_match.group(1)
                error[error_msg] += 1

                per_user[user]['ERROR'] += 1

    # Sort error dictionary and generate error_message.csv
    sorted_error = sorted(error.items(), key=lambda item: item[1], reverse=True)
    #print(sorted_error)
    sorted_error.insert(0, ("Error", "Count"))
    with open("error_message.csv", "w", newline="") as error_file:
        error_writer = csv.writer(error_file)
        error_writer.writerows(sorted_error)

    # Sort per_user dictionary and generate user_statistics.csv
    sorted_per_user = sorted(per_user.items())
    sorted_per_user.insert(0, ("Username", "INFO", "ERROR"))
    with open("user_statistics.csv", "w", newline="") as user_file:
        user_writer = csv.writer(user_file)
        user_writer.writerow(sorted_per_user[0])
        for user, stats in sorted_per_user[1:]:
            user_writer.writerow([user, stats['INFO'], stats['ERROR']])




if __name__ == "__main__":
    main()
