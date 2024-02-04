import subprocess

class Bcolor():
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    
def banner():
    print(Bcolor.GREEN + "+[+[+[ FTP Script AUTO V1.1 ]+]+]+")
    print(Bcolor.GREEN + "+[+[+[ made by The Zero-Day Zone ]+]+]+")
    print(Bcolor.GREEN + r"""
                                    |
FTP Script AUTO V1.1                |
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
Enter Script mode (1, 2, 3, 4 ,5 ,6 ,7 , 8,) 
1: ftp-anon.nse (anonymous logins)                      :
2: ftp-bounce.nse ( FTP bounce Chack)                   :
3: ftp-brute.nse (Performs brute force password)        : 
4: ftp-libopie.nse (FTPd is prone to CVE-2010-1938)     :  
5: ftp-proftpd-backdoor.nse(backdoor reported)          : 
6: ftp-syst.nse (SYST response of "UNIX Type)           :
7: ftp-vsftpd-backdoor.nse(CVE-2011-2523).              :
8: ftp-vuln-cve2010-4221.nse(stack-based bufferoverflow):  """)
            st = int(input(Bcolor.GREEN +"Enter scan option <<<: "))

            # Validate and perform the selected scan option
            if st == 1:
                subprocess.run(["sudo", "nmap", "--script", "ftp-anon", "-p", port, IP])
            elif st == 2:
                subprocess.run(["sudo", "nmap", "--script", "ftp-bounce", "-p", port, IP])
            elif st == 3:
                subprocess.run(["sudo", "nmap", "--script", "ftp-brute", "-p", port, IP])
            elif st == 4:
                subprocess.run(["sudo", "nmap", "--script", "ftp-libopie", "-p", port, IP])
            elif st == 5:
                subprocess.run(["sudo", "nmap", "--script", "ftp-proftpd-backdoor", "-p", port, IP])
            elif st == 6:
                subprocess.run(["sudo", "nmap", "--script", "ftp-vsftpd-backdoor", "-p", port, IP])
            elif st == 7:
                subprocess.run(["sudo", "nmap", "--script", "ftp-vuln-cve2010-4221", "-p", port, IP])
            elif st == 8:
                subprocess.run(["sudo", "nmap", "--script", "ftp-vuln-cve2010-4221", "-p", port, IP])
            else:
                print(Bcolor.RED +"[-] Invalid option. Please select either 1 to 8.")
        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

if __name__ == "__main__":
    ftp_scanner = Ftp()
    ftp_scanner.ftpf()
