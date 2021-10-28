#Author: Devan Swope
#Company: Samtec, Inc.
#Date created: 10/26/2021


from winreg import HKEY_LOCAL_MACHINE
import winreg


def GetTV_ID():

    ComputerName = input("What is the name of the computer you need a TeamViewer ID for? ")

    root = winreg.ConnectRegistry(ComputerName, HKEY_LOCAL_MACHINE)

    try:
        root_key = winreg.OpenKey(root, r'SOFTWARE\TeamViewer', 0, access=winreg.KEY_READ)
        Pathname = winreg.QueryValueEx(root_key, "ClientID")
        print("\n\nFrom :  HKLM\SOFTWARE\TeamViewer\n", Pathname)
    except Exception as e:
        print("\n\nNo ID at HKLM\SOFTWARE\TeamViewer")

    try:
        root_key2 = winreg.OpenKey(root, r'SOFTWARE\WOW6432Node\TeamViewer', 0, access=winreg.KEY_READ)
        Pathname2 = winreg.QueryValueEx(root_key2, "ClientID")
        print("\n\nFrom :  HKLM\SOFTWARE\WOW6432Node\TeamViewer\n", Pathname2)
    except Exception as e:
        print("\n\nNo ID at HKLM\SOFTWARE\WOW6432Node\TeamViewer")


GetTV_ID()
