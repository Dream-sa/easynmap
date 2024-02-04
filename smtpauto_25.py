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
1: smtp-brute.nse (Performs brute force)                            :
2: smtp-commands.nse (use EHLO and HELP to gather)                  :
3: smtp-enum-users.nse (discover all the user accounts)             : 
4: smtp-ntlm-info.nse ( enumerates information)                     :  
5: smtp-open-relay.nse (Attempts to relay mail by issuing)          : 
6: smtp-strangeport.nse (Checks if SMTP running on a non-standard port.)  :
7: smtp-vuln-cve2010-4344.nse (overflow within versions)            :
8: smtp-vuln-cve2011-1720.nse (Checks memory corruption)            :
9: smtp-vuln-cve2011-1764.nse ( format string vulnerability)         : """)
            st = int(input(Bcolor.GREEN + "Enter scan option <<<: "))

            # Validate and perform the selected scan option
            if st == 1:
                subprocess.run(["sudo", "nmap", "--script", "smtp-brute", "-p", port, IP])
            elif st == 2:
                subprocess.run(["sudo", "nmap", "--script", "smtp-commands", "-p", port, IP])
            elif st == 3:
                subprocess.run(["sudo", "nmap", "--script", "smtp-enum-users", "-p", port, IP])
            elif st == 4:
                subprocess.run(["sudo", "nmap", "--script", "smtp-ntlm-info", "-p", port, IP])
            elif st == 5:
                subprocess.run(["sudo", "nmap", "--script", "smtp-open-relay", "-p", port, IP])
            elif st == 6:
                subprocess.run(["sudo", "nmap", "--script", "smtp-strangeport", "-p", port, IP])
            elif st == 7:
                subprocess.run(["sudo", "nmap", "--script", "smtp-vuln-cve2010-4344", "-p", port, IP])
            elif st == 8:
                subprocess.run(["sudo", "nmap", "--script", "smtp-vuln-cve2011-1720", "-p", port, IP])
            elif st == 9:
                subprocess.run(["sudo", "nmap", "--script", "smtp-vuln-cve2011-1764", "-p", port, IP])
            else:
                print(Bcolor.RED + "[-] Invalid option. Please select either 1 to 9.")
        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

if __name__ == "__main__":
    smtp_scanner = Test()
    smtp_scanner.cport()
