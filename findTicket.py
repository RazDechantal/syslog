#!/usr/bin/env python3
import subprocess

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
    error = input("What is the error? ")

    # Read the sys.log file
    with open('sys.log', 'r') as file:
        log_content = file.read()

    # Use tr to replace '  ' with '\n'
    tr_command = f"echo '{log_content}' | tr '  ' '\n'"
    tr_result = run_command(tr_command)

    if tr_result is not None:
        # Use uniq -c to get the counts of each unique line
        uniq_command = f"echo '{tr_result}' | uniq -c"
        uniq_result = run_command(uniq_command)

        if uniq_result is not None:
            # Use sort -nr to sort numerically in reverse order
            sort_command = f"echo '{uniq_result}' | sort -nr"
            sort_result = run_command(sort_command)

            if sort_result is not None:
                # Use head to get the top lines
                head_command = "echo '{}' | head".format(sort_result)
                head_result = run_command(head_command)

                if head_result is not None:
                    print(head_result)
                else:
                    print("Error executing head command.")
            else:
                print("Error executing sort command.")
        else:
            print("Error executing uniq command.")
    else:
        print("Error executing tr command.")

if __name__ == "__main__":
    main()
