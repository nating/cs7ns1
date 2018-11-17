
import sys
import os

#------------------ SYS ARG ERRORS ------------------

if len(sys.argv)!=3:
    print("Error: Command should look like:\n " \
        + "python split.py <path_to_hashfile> <path_to_hashes_folder>")
    sys.exit(1)

if(not os.path.isfile(sys.argv[1])):
    print("Error: %s is not a file." % sys.argv[1])
    sys.exit(1)

if(not os.path.isdir(sys.argv[2])):
    print("Error: %s is not a directory." % sys.argv[2])
    sys.exit(1)

#------------------ MAIN CODE ------------------

# Get arguments
path_to_hashfile = sys.argv[1]
path_to_hashes_folder = sys.argv[2]

# Create lists for hash-types
md5_hashes = []
des_hashes = []
sha256_hashes = []
sha512_hashes = []
pbkdf2_hashes = []
argon_hashes = []

# Populate hash-type lists
with open(path_to_hashfile, "r") as hashes_file:

    # Read in hashes
    hashes = hashes_file.readlines()
    hashes = list(map(str.strip, hashes))

    # Put hashes in appropriate lists
    for hash in hashes:
        if hash.startswith("$1$"):
            md5_hashes.append(hash)
        elif hash.startswith("$5$"):
            sha256_hashes.append(hash)
        elif hash.startswith("$6$"):
            sha512_hashes.append(hash)
        elif hash.startswith("$pbkdf2"):
            pbkdf2_hashes.append(hash)
        elif hash.startswith("$argon2"):
            argon_hashes.append(hash)
        else:
            des_hashes.append(hash)

# MD5 Hashes
with open(path_to_hashes_folder + "MD5.txt", "w") as file:
    [file.write(hash+"\n") for hash in md5_hashes]

# SHA256 Hashes
with open(path_to_hashes_folder + "SHA256.txt", "w") as file:
    [file.write(hash+"\n") for hash in sha256_hashes]

# SHA512 Hashes
with open(path_to_hashes_folder + "SHA512.txt", "w") as file:
    [file.write(hash+"\n") for hash in sha512_hashes]

# PBKDF2 Hashes
with open(path_to_hashes_folder + "PBKDF2.txt", "w") as file:
    [file.write(hash+"\n") for hash in pbkdf2_hashes]

# argon Hashes
with open(path_to_hashes_folder + "argon.txt", "w") as file:
    [file.write(hash+"\n") for hash in argon_hashes]

# DES Hashes
with open(path_to_hashes_folder + "DES.txt", "w") as file:
    [file.write(hash+"\n") for hash in des_hashes]

print("Done.")
