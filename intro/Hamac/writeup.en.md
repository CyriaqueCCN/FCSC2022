We need to write a little python script to reverse the function used

First, we hashcat the 'h' variable with rockyou.txt wordlist to get back the password

`hashcat -m 1450 --force h.txt ~/rockyou.txt`

h.txt is "<value of h in output.txt>:FCSC2022"

We get a candidate : `omgh4xx0r`. Of course.

Now we just edit the original hamac.py (in solve.py) to reverse the encryption, which gives us the flag

FCSC{5bb0780f8af31f69b4eccf18870f493628f135045add3036f35a4e3a423976d6}
