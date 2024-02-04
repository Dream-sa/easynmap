import subprocess

class Bcolor():
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    
def banner():
    print(Bcolor.GREEN + "+[+[+[ TFTP Script AUTO V1.1 ]+]+]+")
    print(Bcolor.GREEN + "+[+[+[ made by The Zero-Day Zone ]+]+]+")
    print(Bcolor.GREEN + r"""
                                    |
TFTP Script AUTO V1.1               |
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
            IP = input(Bcolor.RED +"Enter your IP: ")
            # Validate IP address format if needed

            # Get user input for port
            port = input(Bcolor.RED +"Enter your port: ")
            # Validate port input if needed

            # Get user input for scan option
            print(Bcolor.YELLOW + r"""
Enter Script mode (1, 2,) 
1: tftp-enum.nse (Enumerates TFTP filenames)        :
2: tftp-version.nse                                 : """)
            
            st = int(input(Bcolor.GREEN +"Enter scan option <<<: "))

            # Validate and perform the selected scan option
            if st == 1:
                subprocess.run(["sudo", "nmap", "--script", "tftp-enum", "-p", port, IP])
            elif st == 2:
                subprocess.run(["sudo", "nmap", "--script", "tftp-version", "-p", port, IP])
            else:
                print(Bcolor.RED +"[-] Invalid option. Please select either 1 or 2.")
        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

if __name__ == "__main__":
    ftp_scanner = Ftp()
    ftp_scanner.ftpf()
