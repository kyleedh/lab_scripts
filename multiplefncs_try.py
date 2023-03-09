import sys
import pysam
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def parse_samentry(sam_file):
    samfile = pysam.AlignmentFile(sam_file, "r")
    mapped_pos, read_name, ground_truth = list(), list, list()
    for a in samfile:
        read_name.append(a.query_name)
        mapped_pos.append(a.reference_start)
        ground_truth = int(read_name.split("_")[4]) + 1
    return read_name, mapped_pos, ground_truth


def compute_hits(mapped_pos, ground_truth):
    correct_map = 0
    for m, g in zip(mapped_pos, ground_truth):
        if m == g:
            correct_map += 1
    incorrect_map = len(mapped_pos) - correct_map
    return correct_map, incorrect_map


def compute_error(mapped_pos, ground_truth):
    return [abs(m-g) for m, g in zip(mapped_pos, ground_truth)]


#def plot_stuff(correct_map, incorrect_map):
#    x = ["correct", "incorrect"]
#    y = [correct_map, incorrect_map]
#    plt.bar(x, y, color='green', width=0.3)
#    plt.xlabel("Correct vs Incorrect Mapped Reads")
#    plt.ylabel("Number of Reads")
    # eventually plot change values and average error


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: <exe> <samfile>')
        sys.exit()

    _, sam_fl = sys.argv

    read_name, mapped_pos, ground_truth = parse_samentry(sam_fl)
    num_correct, num_incorrect = compute_hits(mapped_pos, ground_truth)
    mapping_error = compute_error(mapped_pos, ground_truth)
    print('num_correct', num_correct, 'num_incorrect', num_incorrect)
    print('mean error', np.mean(mapping_error), 'error sum', sum(mapping_error))

