
*https://github.com/nating/cs7ns1/blob/master/practicals/practical4/README.md*

# Practical 4 - Crack moar hashes

## Task

* Crack [an assortment of 2000 hashes](https://github.com/nating/cs7ns1/blob/master/practicals/practical4/nating.hashes).

## Requirements

* Install [hashid](https://github.com/psypanda/hashID)
* Install [hashcat](https://hashcat.net/hashcat/)
* Install [JohnTheRipper](https://github.com/magnumripper/JohnTheRipper)
* Install [Python](https://www.python.org/downloads/)
* Download [rockyou.txt](https://wiki.skullsecurity.org/Passwords)

## Steps necessary

* Split hashes into separate files:  
  ```bash
  python src/split-hashes.py hashes/nating.hashes hashes/
  ```  
* For each file (bar argon [PBKDF2 will need to be converted, as discussed below]), run:  
  ```bash
  hashcat -m <hashcat number> -a 3 my_hashes.txt ?l?l?l?l?l
  hashcat -m <hashcat number> -a 1 my_hashes.txt 4char.txt 4char.txt
  hashcat -m <hashcat number> my_hashes.txt rockyou.txt
  ```  
* For argon passwords, run:  
  ```bash
  john --mask=?l?l?l?l?l hashes/argon.txt
  john --wordlist=wordlists/rockyou.txt hashes/argon.txt
  john --wordlist=wordlists/4char4char.txt hashes/argon.txt
  ```

## Optimizations

* Make sure not to check that hashes are of the same password twice. e.g. if a 5 letter mask attack is run on a set of hashes, do not run a wordlist attack with a wordlist that contains any 5 letter words.
* Hashcat runs faster than JohnTheRipper, but does not accept the PBKDF2 hashes as given. They can be converted to an acceptable format to work, by replacing '$pbkdf2-' with '', '.' with '+', and '$' with ':'.
* Instead of using the ?l?l?l?l?l mask, first crack more likely variations of five letters permutations.

## Hardware

* Google Cloud instance with as many NVIDIA TESLA V100 GPUs as possible.

## Steps Actually Taken

### Hash identification

* Ran `hashid -m nating.hashes` to identify hash types and hashcat modes.
* Created and ran [script](https://github.com/nating/cs7ns1/blob/master/practicals/practical4/src/split-hashes.py) to split hashes by type.

### Password identification

* Ran `hashcat -m 500 hashes/MD5.txt rockyou.txt` and `hashcat -m 500 hashes/DES.txt rockyou.txt` to crack some easy hashes to start with (rockyou.txt is usually a good staring place) to determine a password pattern.
* Noted that it seemed:
  * Many of the passwords were 5 letters long.
  * Many of the passwords were 8 letters long, and look like two words put together.
* Ran `hashcat -m hashes/MD5.txt -a 3 my_hashes.txt ?l?l?l?l?l` to get all five character passwords.
* Noted that five character passwords seem more likely to follow certain vowel-consonant patterns.
* Created [custom mask](https://github.com/nating/cs7ns1/blob/master/practicals/practical4/custom.hcmask) to get the easiest of the five character passwords.
* Split 8 letter passwords that look like two words put together into 4 letter words, put them in quotation marks and do google search to find that they are from the linux dictionary (no code necessary: `cmd+a`, `cmd+shift+l`, `right`, `"`, `cmd+left`, `backspace`, `space`, `"`, `right`, `right`, `right`, `right`, `"`, `space`, `"`  should do the trick in [Atom](https://atom.io/)).
* Cut down [the linux dictionary](https://github.com/nating/cs7ns1/blob/master/practicals/practical4/wordlists/linux-dictionary.txt) to [only 4 character words](https://github.com/nating/cs7ns1/blob/master/practicals/practical4/wordlists/4char.txt), for a combinator attack, with:
  * `cp /usr/dict/share/words > wordlists/linux-dictionary.txt`
  * `awk 'length($0)<5' wordlists/linux-dictionary.txt > temp.txt`
  * `awk 'length($0)>3' temp.txt > 4char.txt`

### Hash cracking

* Created and ran a [script](https://github.com/nating/cs7ns1/blob/master/practicals/practical4/src/convert-pbkdf2.py) to convert PBKDF2 hashes to and from a format accepted by hashcat.
* Ran the following commands to crack all but argon hashes:
  ```bash
  hashcat -m <hashcat number> -a 3 my_hashes.txt mask_file.hcmask
  hashcat -m <hashcat number> -a 3 my_hashes.txt ?l?l?l?l?l
  hashcat -m <hashcat number> my_hashes.txt rockyou.txt
  hashcat -m <hashcat number> -a 1 my_hashes.txt 4char.txt 4char.txt
  ```
* Hashcat does not crack argon hashes, so JohnTheRipper must be used instead.
* Created a [wordlist]() to mimic hashcat's combinator attack on JohnTheRipper.
* None of the JohnTheRipper attack modes gave acceptable ETAs for completion:
  * `john --mask=?l?l?l?l?l hashes/argon.txt`
  * `john --wordlist=wordlists/rockyou.txt hashes/argon.txt`
  * `john --wordlist=wordlists/4char4char.txt hashes/argon.txt`
* Left `john --mask=?l?l?l?l?l hashes/argon.txt` running until the deadline in the hope that some argon passwords could be cracked.
