
*https://github.com/nating/cs7ns1/blob/master/MODULE-FINAL-REPORT.md*

# CS7NS1/CS4400 Module Final Report

- Student name: Geoffrey Natin
- Student number: 14318196
- Date: 15/11/18

## InfernoBall team self-evaluation

- Team number: 18
- Team members: - Abhishek Jain, James Farrell, John Lincoln, Geoffrey Natin

All team members made good contributions. After initial group contact through email, we communicated through WhatsApp. For the most part, all team members were contributing to the conversation every day from the day that our InfernoBall was delivered until the day that it was finished. Communication was round the clock, from very early in the morning to very late at night. My phone was constantly buzzing with updates on hashes cracked for almost two weeks.

Some members were better at finding and narrowing down our wordlists, some members were better at running cracking constantly with almost instant turnovers with attack methods. In my opinion, each member of the team put in an admirable effort and was effective with the work that they did. As group projects go, this one went down extremely smooth. I believe myself very lucky to have been paired with the three students that I was, and I think that each of them deserves a good grade for the effort that they put into this project.

|             |  AJ|  JF|  JL|  GN|
|-------------|----|----|----|----|
|effort       |high|high|high|high|
|effectiveness|high|high|high|high|

## What I learned (1-2 pages)
TODO: Get rid of following:
*Describe what you learned from taking the module.*

## What I did (2-4 pages)

*Please note that although the story is told here, it might be easier/better followed browsing the 'practicals/practicalX' files at https://github.com/nating/cs7ns1.*

TODO: Get rid of following:
*Describe what you did during the module, i.e., how you solved the practicals. Include URLs for code/repos but not the code itself. If you have more text than fits in 4 pages, include a link to that additional text but do make the 4 pages self-contained (other than code).*

### Assignment 2

* Registered with RosettaHub.
* Created a Linux instance.
* Compiled JohnTheRipper.
* Ran a benchmarking script.

### Assignment 3

* Ran `hashid -m nating.hashes` to identify hashes as MD5 Crypt with a hashcat mode of 500.
* Ran `hashcat -m 500 nating.hashes rockyou.txt` to crack some hashes to start with (rockyou is usually a good staring place to determine some pattern).
* Noted all passwords are of 8 characters long.
* Ran `awk 'length($0)>7' rockyou.txt > temp.txt` to get rid of passwords less than 8 characters long.
* Ran `awk 'length($0)<9' temp.txt > wordlist.txt` to get rid of passwords more than 8 characters long.
* Ran `hashcat -m 500 nating.hashes wordlist.txt`.
* Personal 2012 Laptop was more than capable of cracking all 1000 hashes.

### Assignment 4

## Module evaluation (1 page)

TODO: Get rid of following:
*Say what you liked/disliked about the module and why.
There's no need to say that RosettaHub is creaky, we
know that:-)*

### What I liked

### What I disliked

* I am trying as hard as I can to get the highest grade I can for this module.
* As such, I would not like to list what I do not like about the module in case it would be detrimental to my grade.
* I would be very happy to discuss what I disliked about the module anonymously or independently from assignments that count towards my grade.
















/
