import read_file
import start_quiz

# lists containing questions and answers for the different quizzes offered in the program
port_names = ["FTP", "SSH", "SFTP", "Telnet", "SMTP", "DNS", "DHCP", "TFTP", "HTTP",
                 "POP3", "NTP", "NetBIOS", "IMAP", "SNMP", "LDAP", "HTTPS", "SMB", "Syslog",
                 "SMTP TLS", "LDAPS", "IMAP over SSL", "POP3 over SSL", "SQL Server Protocol",
                 "SQLnet Protocol", "MySQL", "RDP", "SIP"]

port_numbers = [[20, 21], 22, 22, 23, 25, 53, [67,68], 69, 80, 110, 123, 139, 143, 161, 389,
                    443, 445, 514, 587, 636, 993, 995, 1433, 1521, 3306, 3389, [5060, 5061]]

wifi_frequencies =["Frequency 5 Ghz, Bandwidth 54 Mbps", "Frequency 2.4 Ghz, Bandwidth 11Mbps",
                "Frequency 2.4Ghz, Bandwidth 54Mbps", "Frequency 2.4 and 5GHz, Bandwidth 150/600Mbps (MIMO)",
                "Frequency 5GHz, Bandwidth 3Gbps (MU-MIMO)", "Frequency 2.4, 5 and 6 GHz, Bandwidth 9.6Gbps (MU-MIMO)"]

wifi_standards = ["802.11a", "802.11b", "802.11g", "802.11n", "802.11ac", "802.11ax"]

ethernet_name = ["Link Aggregation", "Power Over Ethernet up to 15.4 Watts", "Power Over Ethernet up to 25.5 Watts",
                 "User Authentication", "Spanning Tree Protocol"]
ethernet_standard = ["802.3ad", "802.3af", "802.3at", "802.1x","802.1D"]

cat_cable = ["Cat 3", "Cat 5", "Cat 5e", "Cat 6", "Cat 6a", "Cat 7", "Cat 8"]
cat_standard = ["10Base-T/10 Mbps/100 meters", "100Base-TX/100 Mbps/100 Meters", "1000Base-T/1000 Mbps/100 Meters",
                "1000Base-T/10GBase-T/1000 Mbps/10 Gbps/100 Meters/55 Meters", "10GBase-T/10 Gbps/100 Meters",
                "10GBase-T/10 Gbps/100 Meters", "40GBase-T/40 Gbps/30 Meters"]

dns_record = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]
dns_description = ['Address Record (Ipv4)', 'Address Record (Ipv6)', 'Canonical Name Record', 
                   'Mail Exchange Record', 'Nameserver Record', 'Pointer Record', 
                   'Start Of Authority Record', 'Service Location Record', 'Text Record']

alert_level = ['0', '1', '2', '3', '4', '5','6','7']
alert_level_answer = ["Emergency", "Alert", "Critical", "Error", "Warning",
                      "Notice", "Information", "Debugging"]

def banner():
    print("######################################################")
    print("           WELCOME TO THE NETWORK+ TRAINER")
    print("######################################################")
    print()
    
def menu_choice():
    choices = ["Port Number Quiz", "Protocol Information", "802.11 Standards Quiz",
               "802.1 Standards Quiz", "Cat Cable Quiz", "DNS Records Quiz", "Log Level Quiz"]
    for c, i in enumerate(choices):
        print(f"#{c+1}: {i}")
    print(f"#{c+2}: Exit Application")
    print()
    #print("#1: Port Number Quiz")
    #print("#2: Protocol Information")
    #print("#3: 802.11 Standards Quiz")
    #print("#4: 802.1 Standards Quiz")
    #print("#5: Cat Cable Quiz")
    #print("#6: DNS Records Quiz")
    
    try:
        choice = int(input("Please enter a number: "))
    except ValueError as e:
        print("Wrong Value Entered")
    
    return choice   
    
# show the user the welcome banner and gameplay rules
banner()

while True:
    user_choice = menu_choice()
    print()
    
    match user_choice:
        case 1:
            start_quiz.start_game(port_names, port_numbers, user_choice)
        case 2:
            read_file.service_info()
        case 3:
            start_quiz.start_game(wifi_frequencies, wifi_standards, user_choice)
        case 4:
            start_quiz.start_game(ethernet_name, ethernet_standard, user_choice)
        case 5:
            start_quiz.start_game(cat_cable, cat_standard, user_choice)
        case 6:
            start_quiz.start_game(dns_description, dns_record, user_choice)
        case 7:
            start_quiz.start_game(alert_level, alert_level_answer, user_choice)
        case 8:
            print("Thank you for using Port Quizzer!")
            break
        case _:
            print("Choose a number between 1 and 7")
    # add whitespace between answers
    print()
    
    
