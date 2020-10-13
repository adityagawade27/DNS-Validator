<h4> DNS Validator - Python </h4>
Reads cat /etc/resolv.conf and identifies the IP addresses inside
Performs the foll checks:
1. Identifies the IP addresses from /etc/resolv.conf
2. Checks if the IP addresses are valid
3. Checks if the IP addresses or nameservers are reachable
4. Checks if queries to www.google.com can be resolved using the nameservers

Example:

[root@centos dns_parser]# python dnsResolveParser.py
PING 67.207.67.3 (67.207.67.3) 56(84) bytes of data.
64 bytes from 67.207.67.3: icmp_seq=1 ttl=61 time=0.973 ms

--- 67.207.67.3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.973/0.973/0.973/0.000 ms
Nameserver 67.207.67.3 is reachable
172.217.164.100
Nameserver 67.207.67.3 is resolving www.google.com
PING 67.207.67.2 (67.207.67.2) 56(84) bytes of data.
64 bytes from 67.207.67.2: icmp_seq=1 ttl=61 time=0.220 ms

--- 67.207.67.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.220/0.220/0.220/0.000 ms
Nameserver 67.207.67.2 is reachable
216.58.195.68
Nameserver 67.207.67.2 is resolving www.google.com
2 valid entries in /etc/resolv.conf file
[root@centos dns_parser]#
