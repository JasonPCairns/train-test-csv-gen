import sys
import csv
import random
import math


def main():
    """Take dataframe .csv as second command line argument,
    first argument being n-proportion to cut to training, remainder implicitly as testing
    output random training and testing .csv's"""
    try:
        n_prop = float(sys.argv[1])
        csv_name = sys.argv[2]
        head_csv_list = import_csv(csv_name)
        out_csvs = pull_random(head_csv_list, n_prop)
        write_out(out_csvs)
    except IndexError:
        print("Multiple editing to be made available later")


def import_csv(csv_name):
    """From csv_path import file and return csv list"""
    with open(csv_name, newline='') as my_csv:
        csv_list = csv.reader(my_csv)
        head_csv_list = [row for row in csv_list]
    return head_csv_list


def pull_random(head_csv_list, n_prop):
    """Take csv list and, while respecting header info,
    randomly samples n_prop of it to a training csv,
    the remainder going to a testing csv"""
    header = head_csv_list.pop(0)
    train_list = list()
    prop = math.floor(len(head_csv_list) * n_prop)
    for row in range(prop):
        randindex = random.randrange(len(head_csv_list))
        train_list.append(head_csv_list.pop(randindex))
    test_list = head_csv_list
    train_list = train_list
    return header, train_list, test_list


def write_out(out_csvs):
    """Takes a tuple of out_csv with header at index 0,
    training list at index 1, testing list at index 2,
    and writes them out to csv files"""
    header = out_csvs[0]
    train_list = out_csvs[1]
    test_list = out_csvs[2]
    with open('training.csv', 'w+', newline='') as trainingfile:
        trainwriter = csv.writer(trainingfile)
        trainwriter.writerow(header)
        for row in train_list:
            trainwriter.writerow(row)
    with open('testing.csv', 'w+', newline='') as testingfile:
        testwriter = csv.writer(testingfile)
        testwriter.writerow(header)
        for row in test_list:
            testwriter.writerow(row)


if __name__ == '__main__':
    main()
