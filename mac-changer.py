import subprocess
import optparse
import re

#Future improvements
#Select random MAC from specified vendor, Generate random MAC, Autorun at startup with specified MAC

def get_cmd_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change (if empty, defaults to 'wlan0'")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address  (if empty, defaults to '00:11:22:33:44:55'")
    (options, arguements) = parser.parse_args()

    if not options.interface:
        options.interface = "wlan0"
    if not options.new_mac:
        options.new_mac = "00:11:22:33:44:55"

    return options

def change_mac(interface, new_mac):
    print("[+] Setting MAC of interface " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

options = get_cmd_args()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])

print(ifconfig_result)
