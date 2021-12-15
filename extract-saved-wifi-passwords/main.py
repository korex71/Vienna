import subprocess
import os
import re
from collections import namedtuple
import configparser


def get_windows_saved_ssids():
    """Returns a list of saved SSIDs in a Windows machine using netsh command"""
    # get all saved profiles in the PC
    saved_profiles = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='replace')
    # get the SSID of each profile
    ssids = re.findall("(?:Profile\s*:\s)(.*)", saved_profiles)
    # remove duplicates
    ssids = list(set(ssids))
    # remove empty strings
    ssids = list(filter(None, ssids))
    # remove the word "All User Profile"
    ssids = list(filter(lambda x: x != "All User Profile", ssids))
    # remove the word "Temporary Profile"
    ssids = list(filter(lambda x: x != "Temporary Profile", ssids))

    print(ssids)

    return ssids

    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s(.*)", output)
    for profile in profiles:
        # for each SSID, remove spaces and colon
        ssid = profile.strip().strip(":").strip()
        # add to the list
        ssids.append(ssid)
    return ssids

print(get_windows_saved_ssids())    