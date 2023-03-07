import sys
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: <exe> <samfile>')
        sys.exit()

import pysam
file = input("file")
def parse_samentry(file):
    samfile = pysam.AlignmentFile("file", "r")     # Open the SAM file for reading
    # Iterate over the alignments in the SAM file
    for alignment in samfile:
        pos = alignment.pos  # get "POS" data from the alignment___is integer type
        print(f"Read {alignment.qname} is mapped to position {pos}")  # check that position data is right

        fields = alignment.strip().split("\t")  # split the alignment header up
        read_name = fields[0]  # first "column"/chunk of info in header is read name includes start and end of synthetic read
        readpos = ""  # get start and stop positions from the read name
        for character in read_name:  # going to produce error if ex pos = 145 readstart = 1450
            if character.isdigit():  # how to do this UNTIL finds "_" ???
                readpos += character
                readpos = int(readpos)
                print(f"Read {read_name} contains the number {readpos}")


def compute_hits():
    correct_map = 0
    incorrect_map = 0
    correct_reads = []
    incorrect_reads = []
    if int(readpos[0:len(str(pos))]) == pos:
        correct_map += 1
        correct_reads.append(read_name)  ##add read name to list
    else:
        incorrect_map += 1
        incorrect_reads.append(read_name)  ##add read name to list


def compute_error():
    start_pos = int(readpos[0:len(str(pos))])
    change_val = abs((pos - start_pos))


import matplotlib.pyplot as plt

def plot_stuff():
    x = ["correct", "incorrect"]
    y = ["correct_map", "incorrect_map"]
    plt.bar(x, y, color='green', width=0.3)
    plt.xlabel("Correct vs Incorrect Mapped Reads")
    plt.ylabel("Number of Reads")
    plt.bar("", change_val, color='blue', width=0.3)
    plt.title("Distance from True Read Start Position")
    plt.ylabel("# bases")
    plt.xlabel("Error")


    # call the functions to get the results

# Open the SAM file for reading
# with open("example.sam", "r") as samfile:
