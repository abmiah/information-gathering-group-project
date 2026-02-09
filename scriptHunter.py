"""
Install the `pyhunter` library to use this script: 'pip install pyhunter' from
https://github.com/VonStruddle/PyHunter
"""
import time     # Used to add delays for better user experience
from pyhunter import PyHunter   # Used to interact with the Hunter.io API

"""
This script helps users find email information linked to a specific domain using the Hunter.io API. 
You will need to enter a domain name, and the script will fetch the related email information from 
the Hunter.io API. The results will show up in the console.

To use this script, make sure you have a valid Hunter.io API key. You can get one by signing up on the 
Hunter.io website.
"""

"""
This is api key obtained from Hunter.io, you can replace it with your own API key if you have one.
"""
API_KEY = "c1673e23e114866d998cad155a4a8fc468447519"

def breaker_and_sleep():
    """
    This function prints a separator line and then pauses the execution for x second.
    It is used to create a visual break in the console output and to add a short delay between actions.
    """
    time.sleep(0.5)
    print("----" * 20)
    time.sleep(0.5)


def user_input(prompt="Please enter the domain name to search: "):
    """
    This function asks the user to enter a domain name and returns that name.
    If the user does not enter anything, it returns None.
    """
    domain = input(prompt).strip()
    print(f"You have entered: {domain}")
    return domain or None


def check_domain(domain):
    """
    This function takes a domain name as input and uses the Hunter.io API to
    find email information related to that domain. It prints the results to the console.
    If no information is found, it informs the user.
    """
    hunter_api_key = API_KEY
    if domain == None:
        print("No domain provided.")
        return False

    """
    Initialize the PyHunter object with your API key to perform two searches:
    1. `email_count(domain)`: Retrieves the number of email addresses for the specified domain.  
    2. `domain_search(domain)`: Provides detailed information about the domain, including associated 
    email addresses and their sources.    
    """

    hunter = PyHunter(api_key=hunter_api_key)

    """
    Use the Hunter.io API to count emails and search domains. Save the email results in the 
    `result_email` variable and the domain results in the `result_domain` variable.
    """
    result_email = hunter.email_count(domain)
    result_domain = hunter.domain_search(domain)


    """
    Check if email results are None. If so, print a message stating that no email information was 
    found for the domain and return False. Otherwise, display the email results.
    """
    if result_email is None:
        print(f"No email information found for domain: `{domain}`.")
        return False

    print(f"Domain `{domain}` has found the following email results:\n`{result_email}`.")

    time.sleep(1)
    if result_domain is None:
        print(f"No account information found for domain: `{domain}`.")
        return False

    print("----" * 20)
    print(f"Domain `{domain}` has found the following account information:\n`{result_domain}`.")


def main():
    breaker_and_sleep()
    print("Hunter.io API is being used to search for email information related to the domain you provide.")
    breaker_and_sleep()
    domain = input("Please enter the domain name to search: ").strip()
    breaker_and_sleep()
    print(f"You have entered: {domain}")
    breaker_and_sleep()
    check_domain(domain)
    breaker_and_sleep()

"""
# This line is commented out to prevent the main function from running immediately when the script is imported as a 
module. Instead, it will only run when the script is executed directly, and for testing purposes, you can uncomment it 
to run the main function directly.
"""
# run_main = main()

"""
The expression `if __name__ == "__main__":` is a common Python idiom that checks if a script is being run 
directly, as opposed to being imported as a module. If true, it executes the code block within it, serving 
as the script's entry point for direct user interaction.
"""
if __name__ == "__main__":
    main()
