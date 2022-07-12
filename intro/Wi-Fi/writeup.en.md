Using wireshark we open the pcap file and put the WiFi Password in Edit\>Settings\>Protocols\>IEEE 802.11\>Add encryption key

We then filter by `http` and we see two packets, the latter of which has our flag

FCSC{60d67d7de8aadb7d1241de9a6fdf9148982d2363eab88e862bb98402ac835c8f}
