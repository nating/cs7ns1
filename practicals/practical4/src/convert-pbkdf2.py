
import sys
import os

#------------------ SYS ARG ERRORS ------------------

if len(sys.argv)!=2:
    print("Error: Command should look like:\n " \
        + "python convert-pbkdf2.py <path_to_hashfile>")
    sys.exit(1)

if(not os.path.isfile(sys.argv[1])):
    print("Error: %s is not a file." % sys.argv[1])
    sys.exit(1)

#------------------ MAIN CODE ------------------

# Get arguments
path_to_hashfile = sys.argv[1]

# Read in hashes
hashes = []
with open(path_to_hashfile, "r") as hashes_file:
    hashes = hashes_file.readlines()
    hashes = list(map(str.strip, hashes))

if len(hashes)==0:
    print("Error hashfile is empty.")
    sys.exit(1)

# Convert and write hashes
with open(path_to_hashfile, "w") as output:

    if hashes[0].startswith("$pbkdf2"):
        # Convert hashes to hashcat acceptable format
        for hash in hashes:
            line = hash.replace('$pbkdf2-','')
            line = line.replace('.','+')
            line = line.replace('$',':')
            output.write(line+"\n")
    else:
        # Convert hashes to Submitty acceptable format
        for hash in hashes:
            line = '$pbkdf2-' + hash
            line = line.replace('+','.')
            line = line.replace(':','$')
            output.write(line+"\n")

print("Done.")
