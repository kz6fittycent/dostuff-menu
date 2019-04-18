#!/usr/bin/env python3

import subprocess
import time
 
print()
def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Update your system")
    print ("2. Refresh all snaps")
    print ("3. Install Chrome Browser")
    print ("4. Install Skype")
    print ("5. Install Telegram")
    print ("6. Install Minecraft")
    print ("7. Reboot system")
    print ("8. Exit")
    print (67 * "-")
    print()
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = str(input("Enter your choice: "))
    
    choice = int(choice)
    
    if choice == 1:     
        print ("Updating system...")
        subprocess.call(['sudo','eopkg','up'])
    elif choice == 2:
        print ("Refreshing snaps...")
        subprocess.call(['sudo','snap','refresh'])
    elif choice == 3:
        print ("Installing Chrome...")
        subprocess.call(['sudo','eopkg','bi','--ignore-safety','https://raw.githubusercontent.com/getsolus/3rd-party/master/network/web/browser/google-chrome-stable/pspec.xml'])
        subprocess.call(['sudo','eopkg','it','google-chrome-*.eopkg;','sudo','rm','google-chrome-*.eopkg'])
    elif choice == 4:
        print ("Installing Skype...")
        subprocess.call(['sudo','snap','install','skype','--classic'])
    elif choice == 5:
        print ("Installing Telegram...")
        subprocess.call(['sudo','eopkg','it','telegram'])
    elif choice == 6:
        print ("Installing Minecraft...")
        subprocess.call(['sudo','snap','install','mc-installer'])
    elif choice == 7:
        print ("Rebooting system...")
        subprocess.call(['sudo','reboot'])
    elif choice == 8:
        print ("Exiting. Goodbye!")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Invalid choice, please choose 1-5")
