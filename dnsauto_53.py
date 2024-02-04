import subprocess

class Bcolor():
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    
def banner():
    print(Bcolor.GREEN + "+[+[+[ SMTP Script AUTO V1.1 ]+]+]+")
    print(Bcolor.GREEN + "+[+[+[ made by The Zero-Day Zone ]+]+]+")
    print(Bcolor.GREEN + r"""
                                    |
SMTP Script AUTO V1.1               |
by Zone                             |
                                  .-'-.
                                 ' ___ '
                       ---------'  .-.  '---------
       _________________________'  '-'  '_________________________
        ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                      \    /  ||/   H   \||  \    /
                       '--'   OO   O|O   OO   '--'
**====================================================================** """)
banner()

class Test():
    print(Bcolor.RED + r"""
        +[+[+[ Initializing Program ]+]+]+
            """)
    
    def cport(self):
        try:
            # Get user input for IP address
            IP = input(Bcolor.RED + "Enter your IP: ")
            # Validate IP address format if needed

            # Get user input for port
            port = input(Bcolor.RED + "Enter your port: ")
            # Validate port input if needed

            # Get user input for scan option
            print(Bcolor.YELLOW + r"""
Enter Script mode (1, 2, 3, 4 ,5 ,6 ,7 ,8 , 9 ) 
1: broadcast-dns-service-discovery.nse                          
2: dns-blacklist.nse                  
3: dns-brute.nse              
4: dns-cache-snoop.nse                     : 
5: dns-check-zone.nse          
6: dns-client-subnet-scan.nse  
7: dns-fuzz.nse            
8: dns-ip6-arpa-scan.nse            
9: dns-nsec3-enum.nse  
10:dns-nsec-enum.nse
11:dns-nsid.nse
12:dns-random-srcport.nse
13:dns-random-txid.nse 
14:dns-recursion.nse 
15:dns-service-discovery.nse
16:dns-srv-enum.nse 
17:dns-update.nse 
18:dns-zeustracker.nse
19:dns-zone-transfer.nse 
20:fcrdns.nse                     : """)
            st = int(input(Bcolor.GREEN + "Enter scan option <<<: "))

            # Validate and perform the selected scan option
            if st == 1:
                subprocess.run(["sudo", "nmap", "--script", "broadcast-dns-service-discovery", "-p", port, IP])
            elif st == 2:
                subprocess.run(["sudo", "nmap", "--script", "dns-blacklist", "-p", port, IP])
            elif st == 3:
                subprocess.run(["sudo", "nmap", "--script", "dns-brute", "-p", port, IP])
            elif st == 4:
                subprocess.run(["sudo", "nmap", "--script", "dns-cache-snoop", "-p", port, IP])
            elif st == 5:
                subprocess.run(["sudo", "nmap", "--script", "dns-check-zone", "-p", port, IP])
            elif st == 6:
                subprocess.run(["sudo", "nmap", "--script", "dns-client-subnet-scan", "-p", port, IP])
            elif st == 7:
                subprocess.run(["sudo", "nmap", "--script", "dns-fuzz", "-p", port, IP])
            elif st == 8:
                subprocess.run(["sudo", "nmap", "--script", "dns-ip6-arpa-scan", "-p", port, IP])
            elif st == 9:
                subprocess.run(["sudo", "nmap", "--script", "dns-nsec3-enum", "-p", port, IP])
            elif st == 10:
                subprocess.run(["sudo", "nmap", "--script", "dns-nsec-enum", "-p", port, IP])
            elif st == 11:
                subprocess.run(["sudo", "nmap", "--script", "dns-nsid", "-p", port, IP])
            elif st == 12:
                subprocess.run(["sudo", "nmap", "--script", "dns-random-srcport", "-p", port, IP])
            elif st == 13:
                subprocess.run(["sudo", "nmap", "--script", "dns-random-txid", "-p", port, IP])
            elif st == 14:
                subprocess.run(["sudo", "nmap", "--script", "dns-recursion", "-p", port, IP])
            elif st == 15:
                subprocess.run(["sudo", "nmap", "--script", "dns-service-discovery", "-p", port, IP])
            elif st == 16:
                subprocess.run(["sudo", "nmap", "--script", "dns-srv-enum", "-p", port, IP])
            elif st == 17:
                subprocess.run(["sudo", "nmap", "--script", "dns-update", "-p", port, IP])
            elif st == 18:
                subprocess.run(["sudo", "nmap", "--script", "dns-zeustracker", "-p", port, IP])
            elif st == 19:
                subprocess.run(["sudo", "nmap", "--script", "dns-zone-transfer", "-p", port, IP])
            elif st == 20:
                subprocess.run(["sudo", "nmap", "--script", "fcrdns", "-p", port, IP])
            else:
                print(Bcolor.RED + "[-] Invalid option. Please select either 1 to 7.")
        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

if __name__ == "__main__":
    ftp_scanner = Test()
    ftp_scanner.cport()
