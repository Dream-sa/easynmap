import subprocess

class Bcolor():
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    
def banner():
    print(Bcolor.GREEN + "+[+[+[ SSH Script AUTO V1.1 ]+]+]+")
    print(Bcolor.GREEN + "+[+[+[ made by The Zero-Day Zone ]+]+]+")
    print(Bcolor.GREEN + r"""
                                    |
SSh Script AUTO V1.1                |
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

class Ftp():
    print(Bcolor.RED + r"""
        +[+[+[ Initializing Program ]+]+]+
            """)
    
    def ftpf(self):
        try:
            # Get user input for IP address
            IP = input(Bcolor.RED + "Enter your IP: ")
            # Validate IP address format if needed

            # Get user input for port
            port = input(Bcolor.RED + "Enter your port: ")
            # Validate port input if needed

            # Get user input for scan option
            print(Bcolor.YELLOW + r"""
Enter Script mode (1, 2, 3, 4 ,5 ,6 ,7 , ) 
1: ssh2-enum-algos.nse (Reports number of algorithms)    :
2: ssh-auth-methods.nse (Returns authentication methods) :
3: ssh-brute.nse (Performs brute-force)                  : 
4: ssh-hostkey.nse (Shows SSH hostkeys.)                 :  
5: ssh-publickey-acceptance.nse(publickey authentication): 
6: ssh-run.nse (Runs remote command)                     :
7: sshv1.nse ( Chack SSH Protocol Version)               : """)
            st = int(input(Bcolor.GREEN + "Enter scan option <<<: "))

            # Validate and perform the selected scan option
            if st == 1:
                subprocess.run(["sudo", "nmap", "--script", "ssh2-enum-algos", "-p", port, IP])
            elif st == 2:
                subprocess.run(["sudo", "nmap", "--script", "ssh-auth-methods", "-p", port, IP])
            elif st == 3:
                subprocess.run(["sudo", "nmap", "--script", "ssh-brute", "-p", port, IP])
            elif st == 4:
                subprocess.run(["sudo", "nmap", "--script", "ssh-hostkey", "-p", port, IP])
            elif st == 5:
                subprocess.run(["sudo", "nmap", "--script", "ssh-publickey-acceptance", "-p", port, IP])
            elif st == 6:
                subprocess.run(["sudo", "nmap", "--script", "ssh-run", "-p", port, IP])
            elif st == 7:
                subprocess.run(["sudo", "nmap", "--script", "sshv1", "-p", port, IP])
            else:
                print(Bcolor.RED + "[-] Invalid option. Please select either 1 to 7.")
        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

if __name__ == "__main__":
    ftp_scanner = Ftp()
    ftp_scanner.ftpf()
