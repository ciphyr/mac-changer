#  Created 2019. by Ciphyr - (ciphyr[at]protonmail.com)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.

import subprocess
import optparse
import re

# Future improvements
# Select random MAC from specified vendor, Generate random MAC, Autorun at startup with specified MAC

def get_cmd_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change (defaults to 'wlan0'")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address (defaults to '00:11:22:33:44:55'")
    (options, arguements) = parser.parse_args()

    if not options.interface:
        options.interface = "wlan0"

    if not options.new_mac:
        options.new_mac = "00:11:22:33:44:55"
    else:
        options.new_mac = str(options.new_mac.lower())
        if not re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", options.new_mac):
            parser.error("Please enter a valid MAC address in the form 0A:1B:2C:3D:4E:5F")

    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC of interface " + interface + ", currently " + old_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_regex_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    return mac_address_regex_search_result.group(0)

options = get_cmd_args()
old_mac = get_current_mac(options.interface)
change_mac(options.interface, options.new_mac)

if get_current_mac(options.interface) == options.new_mac:
    print("[=] Success! MAC of interface " + options.interface + " changed to " + get_current_mac(options.interface))
else:
    print("[-] Error, use --help for usage info")
