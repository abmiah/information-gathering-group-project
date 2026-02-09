import os       # Used to run the ping command
import socket   # Used to get IP address from domain
import time     # Used to add delays for better user experience

while True:
    # Ask for user input(target)
    target = input("\nEnter IP address or Domain: ")

    # Resolve IP address
    try:
        ip_address = socket.gethostbyname(target)
        print("[+] IP Address:", ip_address)
    except:
        print("[-] Could not resolve IP address. Try again.")
        continue

    # Ping the target
    print("\n[*] Pinging target...\n")
    response = os.system("ping -c 4 " + ip_address)

    # Giving user explanations
    print("\nPacket explanation:")

    if response == 0:
        print("The target responded to the request, confirming it is reachable over the network.")
    else:
        print("The target did not respond. This can indicate packet loss,firewall filtering, or an offline host.")

    # Giving user the option to try anothr target or exit
    choice = input("\nType 'exit' to quit or press Enter to try another target: ")

    if choice.lower() == "exit":
        print("\nThank you for using our program.Have a great day!.")
        time.sleep(0.5)
        print("====" * 20)
        time.sleep(0.5)
        break

if __name__ == "__main__":
    pass
