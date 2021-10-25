from winreg import HKEY_LOCAL_MACHINE
import winreg

print()
print()
print()

def GetTV_ID():

    ComputerName = input("What is the name of the computer you need a TeamViewer ID for? ")

    root = winreg.ConnectRegistry(ComputerName, HKEY_LOCAL_MACHINE)

    try:
        root_key = winreg.OpenKey(root, r'SOFTWARE\TeamViewer', 0, access=winreg.KEY_READ)
        Pathname = winreg.QueryValueEx(root_key, "ClientID")
        print('\n\nFrom :  HKLM\SOFTWARE\TeamViewer\n')
        print(Pathname)
    except Exception as e:
        print('\n\nNo ID at HKLM\SOFTWARE\TeamViewer')
        print('\n\nError: ')
        print(e)

    try:
        root_key2 = winreg.OpenKey(root, r'SOFTWARE\WOW6432Node\TeamViewer', 0, access=winreg.KEY_READ)
        Pathname2 = winreg.QueryValueEx(root_key2, "ClientID")
        print('\n\nFrom :  HKLM\SOFTWARE\WOW6432Node\TeamViewer\n')
        print(Pathname2)
    except Exception as e:
        print('\n\nNo ID at HKLM\SOFTWARE\WOW6432Node\TeamViewer')
        print('\n\nError: ')
        print(e)

    #print()
    #print()
    #print("From :  HKLM\SOFTWARE\TeamViewer")
    #print(Pathname)
    #print()
    #print("From :  HKLM\SOFTWARE\WOW6432Node\TeamViewer")
    #print(Pathname2)
    #print()
    #print()


GetTV_ID()