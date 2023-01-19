import json

# load the json file so it can be used later
with open("port_number_information.json", 'r') as openfile:
    json_object = json.load(openfile)

services_list = ["FTP", "SSH", "SFTP", "Telnet", "SMTP", "DNS", "DHCP", "TFTP", "HTTP",
                 "POP3", "NTP", "NetBIOS", "IMAP", "SNMP", "LDAP", "HTTPS", "SMB", "Syslog",
                 "SMTP TLS", "LDAPS", "IMAP over SSL", "POP3 over SSL", "SQL Server Protocol",
                 "SQLnet Protocol", "MySQL", "RDP", "SIP"]

# display the list of common ports to the user
def services_menu():
    for count, service in enumerate(services_list):
        print(f"#{count+1:<3}- {service}")
    print()

def service_info(): 
    # create a loop so the user can check multiple services
    while True:
        services_menu()
        
        # get the users choice and subtract one to get accurate entry
        user_choice = int(input("Please choose a number: "))
        user_choice -= 1
    
        # print out the name of the service followed by the information about it  
        print()
        print(f"Service Name: {services_list[user_choice]}")
        print(f"{json_object[services_list[user_choice]]}")
        print()
        
        user_exit = input("Enter q to quit or enter to continue: ")
        if user_exit.lower() == "q":
            break
        
#service_info()