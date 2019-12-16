Quick analysis for the pcap

```tshark -r ayah-peng.pcapng | awk '{print $6}' | sort | uniq -c | sort -n
    4 HTTP
    6 TLSv1
   12 IGMPv3
   15 MDNS
   28 TLSv1.3
   40 ARP
   66 ICMPv6
   98 DNS
  164 SSH
  174 NTP
  184 STP
  804 TLSv1.2
 1030 OpenVPN
 1148 TCP
 1362 ICMP
 8009 UDP```

There are a lot of ICMP packets (could be using for transfering data)
Filter ICMP packets only in wireshark (001.png)
Notice large data length in each ICMP packet -> notice each string in data (looks like b64), after decoding b64 string of the first packet, resulted in (002.png). 
PNG header bytes appeared, but it got repeated 3 times & i think other packets will be the same
So just need to remove duplicate ones and append data will result in correct b64 -> decode b64 (python solve.py | base64 -d > flag.png) -> image containing QR code with password, after reading the QR will give us a path "/ctf-should-be-free-like-wgmy/flag.zip"
The hint said "old server" ..so a quick subdomains enumeration + appending the given path. Then only 1 result gave us the real zip (http://rahsia.wargames.my/). Unzipped with password and got the flag ;)
