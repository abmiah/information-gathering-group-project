"""
This script is the main controller for running three important modules: `ping_command`, `scanner`, and `scriptHunter`.
It starts with a welcome message for users and sets the stage for the upcoming tasks. After running the functions from
each of the three modules, the script ends with a friendly message that summarizes the completed tasks.

The script's structure ensures that if it is run directly, instead of being used in another script, the code inside a
specific block (indicated by `if __name__ == "__main__":`) will execute. This setup allows the script to be reused in
other contexts while also providing clear and organised output when run independently.

Overall, the script coordinates the interactions between different modules and improves the user experience by giving
helpful feedback during the execution.
"""

def intro_message():
    intro_message = f"""
Welcome to our educational tool design for domain search, the script will run in the following order.
{"----" * 20}
1 - Ping Command: This module allows you to ping an IP address or domain to check its reachability and network latency, providing explanations of the results for better understanding.
2 - Scanner: This module translates IP addresses and domain names, and scans for open ports on a target. It helps identify running services and understand the network configuration. 
3 - Script Hunter: This module uses the Hunter.io API to find email addresses associated with a given domain, providing valuable insights into its online presence.
{"----" * 20}
❗❗️❗Please note: This is purely for educational purposes, and we do not encourage any illegal activities.❗❗❗️
{"----" * 20}
       """
    print(intro_message)

def outro_message():
    outro_message = """
Thank you for using our program. We hope you found it useful. Have a great day!

From Akshay, Arjeta and Amrol 😀 
"""
    print(outro_message)


def main_ping():
    """
    Import the ping_command modules. Then, call a known function name if present in ping_command to execute the
    ping functionality.
    """
    import ping_command

    """ 
    Call a known function name if present in ping_command. Also the 'hasattr()' function is used to check if the 
    ping_command module has a specific function (like 'ping' or 'run_ping') before trying to call it. This prevents 
    errors if the function does not exist in the module.
    """
    if hasattr(ping_command, "ping"):
        ping_command.ping()
    elif hasattr(ping_command, "run_ping"):
        ping_command.run_ping()

def main_scanner():
    """
    Import the scanner modules.
    """
    import scanner

    """ 
    Call a known function name if present in scanner also using the 'hasattr()' function to check for the presence 
    of specific functions before calling them.
    """
    if hasattr(scanner, "scan"):
        scanner.scan()
    elif hasattr(scanner, "run_scan"):
        scanner.run_scan()

def main_hunter():
    """
    Import the scriptHunter modules.
    """
    import scriptHunter

    """
    Call a known function name if present in scriptHunter, once again using the 'hasattr()' function to check for the 
    presence of specific functions before calling them.
    """
    if hasattr(scriptHunter, "main"):
        scriptHunter.main()
    elif hasattr(scriptHunter, "run"):
        scriptHunter.run()


"""
The main block of the script is defined here. When the script is run directly, it will execute the following sequence:
"""
if __name__ == "__main__":
    intro_message()
    main_ping()
    main_scanner()
    main_hunter()
    outro_message()
