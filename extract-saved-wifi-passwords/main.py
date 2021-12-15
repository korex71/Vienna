import subprocess
import os
import re
from collections import namedtuple
import configparser


def get_windows_saved_ssids():
    """Retorna uma lista de ssids salvos"""
    
    saved_profiles = subprocess.check_output(
        ["netsh", "wlan", "show", "profiles"]
    ).decode("utf-8", errors="backslashreplace")

    ssids = re.findall("(?:Profile\s*:\s)(.*)", saved_profiles)

    ssids.remove("all user profiles")

    return ssids

print(get_windows_saved_ssids())    