
*https://github.com/nating/cs7ns1/blob/master/practicals/practical3/README.md*

# Practical 3 - Crack some hashes

## Task

* Crack [1000 MD5 Crypt hashes](https://github.com/nating/cs7ns1/blob/master/practicals/practical3/nating.hashes).

## Requirements

* Install [hashid](https://github.com/psypanda/hashID)
* Install [hashcat](https://hashcat.net/hashcat/)
* Download [rockyou.txt](https://wiki.skullsecurity.org/Passwords)

## Steps necessary

* Run `hashcat -m 500 nating.hashes rockyou.txt`.

## Optimizations

* Remove lines of rockyou.txt that are not 8 characters long.

## Hardware

* Personal 2012 laptop more than capable of cracking all the hashes.

## Steps Actually Taken

* Run `hashid -m nating.hashes` to identify hashes as MD5 Crypt with a hashcat mode of 500.
* Run `hashcat -m 500 nating.hashes rockyou.txt` to crack some hashes to start with (rockyou is usually a good staring place to determine some pattern).
* Note all passwords are of 8 characters long.
* Run `awk 'length($0)>7' rockyou.txt > temp.txt` to get rid of passwords less than 8 characters long.
* Run `awk 'length($0)<9' temp.txt > wordlist.txt` to get rid of passwords more than 8 characters long.
* Run `hashcat -m 500 nating.hashes wordlist.txt`.
