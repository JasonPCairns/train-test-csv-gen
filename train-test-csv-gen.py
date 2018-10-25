import sys
import csv


def main():
    """Take dataframe .csv as second command line argument,
    first argument being n-propotion to cut to training, remainder implicitly as testing
    output random training and testing .csv's"""
    try:
        n_prop = int(sys.argv[1])
        csv_path = sys.argv[2]
        in_csv = import_csv(csv_path)
        out_csvs = pull_random(in_csv, n_prop)
        write_out(out_csvs)
    except IndexError:
        print("Multiple editing to be made available later")


def import_csv(csv_path):
    pass


def pull_random(in_csv, n_prop):
    pass


def write_out(out_csvs):
    pass


if __name__ == '__main__':
    main()
