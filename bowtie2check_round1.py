import re
import pysam
import sys

def global_aligns_correct(filename):
    count_cor = 0
    map_correct = []  # value of correct counts and make list for correct mapped reference names
    count_incor = 0
    map_incorrect = []  # value of incorrect counts and make list for incorrect mapped reference names
    for reference in filename:
        test_string = "reference" # initializing string
###use something not re
    temp = re.findall(r'\d+', test_string)  # using re.findall(); getting numbers from string
    res = list(map(int, temp))
    print(int(res[4])) # check res selected start value number in reference name
    if (int(res[4])+1) == int(reference_start):
        count_cor += 1, map_correct.append("reference")
    else:
         count_incor += 1,  map_incorrect.append("reference")
         ###return print(map_correct, map_incorrect)

def parse_samentry():
    pass
import pysam

# Open the SAM file for reading
samfile = pysam.AlignmentFile("example.sam", "r")

# Iterate over the alignments in the SAM file
for alignment in samfile:
    # Extract the "POS" data from the alignment
    pos = alignment.pos
    print(f"Read {alignment.qname} is mapped to position {pos}")

# Iterate over the alignments in the SAM file
for alignment in samfile:
    fields = alignment.strip().split("\t")
    read_name = fields[0]

    # Extract numbers from the read name using string manipulation
    numbers = ""
    for character in read_name:
        if character.isdigit():
            numbers += character

    if numbers:
        numbers = int(numbers)
        print(f"Read {read_name} contains the number {numbers}")


def compute_hits():
    pass

def compute_error():
    pass

def plot_stuff()
    pass

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: <exe> <samfile>')
        sys.exit()

    # call the functions to get the results


# Open the SAM file for reading
#with open("example.sam", "r") as samfile: