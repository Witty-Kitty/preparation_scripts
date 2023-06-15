import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, help="add the path to the directory of your cv data, where the output file should be saved", required=True)
parser.add_argument("--dups", type=int, help="number of duplicates allowed", required=True)
args = parser.parse_args()

train = pd.read_csv(args.data + '/sw/train.tsv', sep='\t', low_memory=False)


# dictionary where we will track sentences and their duplicates
duplicates = {}

# loop through every unique sentence in the  training set
for sentence in train['sentence'].unique():

    # get the indices of the rows where this sentence occurs
    indices = train.index[train['sentence'] == sentence].tolist()

    # add the sentence and its corresponding indices to the dictionary
    duplicates[sentence] = indices

# we create the experiment training sets with the repeated instances of each item 
one2dups = []

for dups in duplicates.values():
    one2dups.append(dups[0:args.dups])

one2dups = [item for sublist in one2dups for item in sublist]

# save csv files of our experiment training sets
train.iloc[one2dups].to_csv(args.data + '/sw/one_to_' + str(args.dups) + '_train.tsv', index=False, sep='\t')
