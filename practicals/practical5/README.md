
*https://github.com/nating/cs7ns1/blob/master/practicals/practical5/README.md*

# Practical 5 - InfernoBall

<p align="center">
<img width="250" alt="InfernoBall" src="https://github.com/nating/cs7ns1/blob/master/assets/img/infernoball.png?raw=true">
</p>

## Task

* Hash crack [the InfernoBall](https://github.com/nating/cs7ns1/blob/master/practicals/practical5/layer-01/infernoball.json).

This involves cracking K of N hashes, 10 times.

## Requirements

* Install [hashid](https://github.com/psypanda/hashID)
* Install [hashcat](https://hashcat.net/hashcat/)
* Install [Python](https://www.python.org/downloads/)
* Download [rockyou.txt](https://wiki.skullsecurity.org/Passwords)

## Outset Steps taken

* Created [a script](https://github.com/nating/cs7ns1/blob/master/practicals/practical5/src/) for reading in an InfernoBall and a potfile and checking if the secret to crack the InfernoBall's outer layer could be found.
* Created [a script](https://github.com/nating/cs7ns1/blob/master/practicals/practical5/src/) to crack an InfernoBall's outer layer and generate a new layer with a new directory and infernoball.json & hash type files.

This way, whenever more hashes were cracked, we could skip over most manual work involved in changing layers with a simple command.

## Hardware

* Google Cloud instance with as many NVIDIA TESLA V100 GPUs as possible.

## Layer 1

* Ran `hashcat -m 15100 layer-01/hashes/sha1crypt.txt rockyou.txt` to crack some hashes to start with (rockyou.txt is usually a good starting place to determine some pattern).
* Noted that every password was found in rockyou.txt.
* Ran a wordlist attack with rockyou.txt on PBKDF2 and SHA512 hashes as well.

## Layer 2

**Easter Egg**: *"xk or cd but not xkcd, as before"*.

* To to crack some hashes to start with (rockyou.txt is usually a good starting place to determine some pattern), ran:
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt rockyou.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt rockyou.txt`
  * `hashcat -m 10900 layer-01/hashes/PBKDF2.txt rockyou.txt`
* Noted that all passwords were two 4 letter words appended together, the second word was always uppercase and that no words contained non-alphabetical characters.
* Added combinator wordlist creation code to run.py.
* Created a combinator style wordlist of uppercase four letter words words from the linux dictionary appended to four letter words from the linux dictionary.
* Ran:
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt 4-letter-combinator.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt 4-letter-combinator.txt`
  * `hashcat -m 10900 layer-01/hashes/PBKDF2.txt 4-letter-combinator.txt`

## Layer 3

**Easter Egg**: *"abcde, as before"*.

* To to crack some hashes to start with (rockyou.txt is usually a good starting place to determine some pattern), ran:
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt rockyou.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt rockyou.txt`
  * `hashcat -m 10900 layer-01/hashes/PBKDF2.txt rockyou.txt`
* Noted that format was five character passwords with a digit occurring in one of the last three positions and alphabetical characters making up the rest of the password.
*  Ran `?l?l?l?l?d`,`?l?l?l?d?l` and `?l?l?d?l?l` mask attacks for sha1crypt, SHA512 and PBKDF2 passwords.

## Layer 4

**Easter Egg**: *"SCSS and tcd.ie websites were cewl'd"*.

* Took the hint, and used [CeWL](https://github.com/digininja/CeWL) to run `cewl --write wordlists/cewl-scss.txt https://www.scss.tcd.ie/` and `cewl --write wordlists/cewl-tcd.txt https://www.tcd.ie/`.
* Ran:  
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt wordlists/cewl-scss.txt`
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt wordlists/cewl-tcd.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt wordlists/cewl-scss.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt wordlists/cewl-tcd.txt`

## Layer 5

**Easter Egg**: *submitty usernames*.

* Remembered that at one stage, I had access to all submitty usernames due to a period where students could 'pick' their teammates but not really.
* Found that all usernames are presented in a script tag on [the team page](https://cs2014.scss.tcd.ie/index.php?semester=f18&course=cs7ns1&component=student&gradeable_id=as5&page=team).
* Extracted student usernames from JSON array on submitty.
* Ran:  
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt wordlists/usernames`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt wordlists/usernames`
  * `hashcat -m 10900 layer-01/hashes/PBKDF2.txt wordlists/usernames`

## Layer 6

**Easter Egg**: *another rockyou?*.

* To to crack some hashes to start with (plain rockyou.txt is usually a good starting place to determine some pattern), ran:
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt rockyou.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt rockyou.txt`
  * `hashcat -m 10900 layer-01/hashes/PBKDF2.txt rockyou.txt`
* Noted that all passwords seemed to be between 6 to 8 characters long.
* Cut rockyou.txt down to only passwords that are between 6 and 8 characters long:
  * Ran `awk 'length($0)>5' rockyou.txt > temp.txt` to get rid of passwords less than 6 characters long.
  * Ran `awk 'length($0)<9' temp.txt > wordlists/rockyou-subset.txt` to get rid of passwords more than 8 characters long.
* Ran:
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt rockyou-subset.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt rockyou-subset.txt`

## Layer 7

**Easter Egg**: *keyboard patterns*.

* Searched the internet for "keyboard patterns wordlist" and downloaded a [wordlist](https://github.com/danielmiessler/SecLists/blob/5c9217fe8e930c41d128aacdc68cbce7ece96e4f/Passwords/Keyboard-Combinations.txt) from danielmiessler/SecLists/Passwords/Keyboard-Combinations.txt.
* Ran:
  * `hashcat -m 15100 layer-07/hashes/sha1crypt.txt wordlists/keyboard-patterns.txt`
  * `hashcat -m 1800 layer-07/hashes/SHA512.txt wordlists/keyboard-patterns.txt`
  * `hashcat -m 10900 layer-07/hashes/PBKDF2.txt wordlists/keyboard-patterns.txt`

## Layer 8

**Easter Egg**: *bleedin' rockyou again*.

* To to crack some hashes to start with (plain rockyou.txt is usually a good starting place to determine some pattern), ran:
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt rockyou.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt rockyou.txt`
  * `hashcat -m 10900 layer-01/hashes/PBKDF2.txt rockyou.txt`
* Noted that all passwords seemed to be the same format as layer 6, so decided to use the same wordlist.
* Ran:
  * `hashcat -m 15100 layer-01/hashes/sha1crypt.txt rockyou-subset.txt`
  * `hashcat -m 1800 layer-01/hashes/SHA512.txt rockyou-subset.txt`
  * `hashcat -m 10900 layer-01/hashes/PBKDF2.txt rockyou-subset.txt`

## Layer 9

**Easter Egg**: *crackstation.txt*.

* Downloaded human passwords version of [crackstation.txt](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) to start with.
* Ran:
  * `hashcat -m 15100 layer-07/hashes/sha1crypt.txt wordlists/human-crackstation.txt`
  * `hashcat -m 1800 layer-07/hashes/SHA512.txt wordlists/human-crackstation.txt`
  * `hashcat -m 10900 layer-07/hashes/PBKDF2.txt wordlists/human-crackstation.txt`
* Noted that:
  * All passwords seemed to be between 5 and 8 characters in length.
  * There were a few 7 or 8 digit passwords.
  * Perhaps we should move on to using the entire crackstation.txt wordlist.
* Cut crackstation.txt down to only digit passwords that are between 6 and 8 digits long:
  * Ran `awk 'length($0)>4' crackstation.txt > gt-5.txt` to get rid of passwords less than 5 characters long.
  * Ran `awk 'length($0)<9' gt-5.txt > lt-9.txt` to get rid of passwords more than 8 characters long.
  * Ran `grep '^[0-9][0-9]*$' lt-9.txt > wordlists/5-8-digits.txt` to get rid of passwords that were not made up entirely of digits.
* Ran:
    * `hashcat -m 15100 layer-07/hashes/sha1crypt.txt wordlists/5-8-digits.txt`
    * `hashcat -m 1800 layer-07/hashes/SHA512.txt wordlists/5-8-digits.txt`
    * `hashcat -m 10900 layer-07/hashes/PBKDF2.txt wordlists/5-8-digits.txt`
* Randomised the order crackstation.txt's contents and split it into multiple files to be run:
  * Ran `gshuf crackstation.txt > rand.txt` randomise the order of the contents of crackstation.txt.
  * Ran `split -l 10000000 -d --additional-suffix=rand.txt rand.txt file` to split the shuffled wordlist into separate files.
* For X in 0->4 ran `hashcat -m 10900 layer-07/hashes/PBKDF2.txt wordlists/file0X.txt`.

## Layer 10

**Easter Egg**: *Dante's text, Norton translation*.

* Downloaded [Charles Eliot Norton's translation of Dante's Inferno](http://onlinebooks.library.upenn.edu/webbin/gutbook/lookup?num=1995).
* Ran `echo "$(cat dantes-inferno.txt" | tr " " "\n" | sort | uniq > dante-wl.txt` to create a wordlist from the epic poem.
* Ran:
  * `hashcat -m 15100 layer-07/hashes/sha1crypt.txt wordlists/dante-wordlist.txt`
  * `hashcat -m 10900 layer-07/hashes/PBKDF2.txt wordlists/dante-wordlist.txt`
