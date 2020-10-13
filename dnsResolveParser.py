# Author: Aditya Gawade

import os
import sys
import re
import socket

filen = "/etc/resolv.conf"
ipRe = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
testHost = "www.google.com"

# Check IF IP addresses in resolv.conf are reachable
def checkPing(ipAddr):
    response = os.system("ping -c 1 " + ipAddr)
    if response == 0:
        print("Nameserver {} is reachable".format(ipAddr))
        return True
    else:
        print("Nameserver {} is not reachable".format(ipAddr))
        return False

# Check if FQDN can bve resolved using the nameserver in resolv.conf
def checkResolution(ipAddr):
    cmdString = "dig +short {0} @{1}".format(testHost, ipAddr)
    response = os.system(cmdString)
    if response == 0:
        print("Nameserver {0} is resolving {1}".format(ipAddr, testHost))
        return True
    else:
        print("Nameserver {0} is not resolving {1}".format(ipAddr, testHost))
        return False


# validate resolv.conf
def checkHostsFile(filen):
    nsList = []

    if not os.path.exists(filen):
        println("{} file not present".format(filen))
        sys.exit(0)

    fileh = open(filen, "r")
    lines = fileh.readlines()
    for line in lines:
        match = re.search(ipRe, line)
        if line.startswith("nameserver") and match:
            ipAddr = match.group()

            # check if IP address is valid
            try:
                socket.inet_aton(ipAddr)
                ping = checkPing(ipAddr)
                resolv = checkResolution(ipAddr)

                # If IP is valid, pingable and can resolve hosts consider the NS valid
                if ping and resolv:
                    nsList.append(ipAddr)

            except socket.error:
                print("{} is not a valid IP address".format(ipAddr))

    print("{0} valid entries in {1} file".format(len(nsList), filen))


if __name__=="__main__":
    checkHostsFile(filen)
