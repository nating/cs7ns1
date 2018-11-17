
import sys
import os

#------------------ SYS ARG ERRORS ------------------

if len(sys.argv)!=3:
    print("Error: Command should look like:\n " \
        + "python create-combinator-wordlist.py <path_to_input_file> <path_to_output_file>")
    sys.exit(1)

if(not os.path.isfile(sys.argv[1])):
    print("Error: %s is not a file." % sys.argv[1])
    sys.exit(1)

#------------------ MAIN CODE ------------------

# Get arguments
path_to_input_file = sys.argv[1]
path_to_output_file = sys.argv[2]

# Read in lines of file
lines = []
with open(path_to_input_file, "r") as input_file:
    lines = input_file.readlines()
    lines = list(map(str.strip, lines))

# Write lines to output file
with open(path_to_output_file, "w") as output_file:
    for start in lines:
        for end in lines:
            output_file.write("%s%s\n" % (start,end))

print("Done.")
