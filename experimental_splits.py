import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

# considerations in creating the train, dev, test sets
# repeated instances of sentences should only be in one set
# repeated audios contributed by a single speaker should also all only be in one set
# we also drop duplicates where a user may have contributed to an individual sentence more than once
# we split out data into 4 subsets with the following ratio; 60:15:15:10
# the final 10% will create evaluation sets to help us quantify gender and age bias
# you can select your own sizes for the experimental sets by passing in their ratios using the flags defined below

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, help="add the path to your cv corpus directory", required=True)
parser.add_argument("--train", type=float, help="desired size of your training set, eg. 0.6 for 60%", required=False, default=0.6)
parser.add_argument("--dev", type=float, help="desired size of your development set, eg. 0.6 for 60%", required=False, default=0.15)
parser.add_argument("--test", type=float, help="desired size of your evaluation set, eg. 0.6 for 60%", required=False, default=0.15)
parser.add_argument("--eval", type=float, help="desired size of your test set, eg. 0.6 for 60%", required=False, default=0.1)
args = parser.parse_args()

def split_data(df, train_size, dev_size, test_size, eval_size, random_state=42):
    # Group by sentence and client_id
    grouped = df.groupby(['sentence', 'client_id'], as_index=False)

    # Get the first index of each group
    idxs = grouped.first().index

    # Split indices into train, validation, and test sets
    train_idxs, remaining_idxs = train_test_split(idxs, test_size=(1 - train_size), random_state=random_state)
    dev_idxs, test_eval_idxs = train_test_split(remaining_idxs, test_size=((test_size + eval_size) / (1 - train_size)), random_state=random_state)
    test_idxs, eval0_idxs = train_test_split(test_eval_idxs, test_size=(eval_size / (1 - train_size - dev_size)), random_state=random_state)
    eval_idxs = test_idxs[:int(eval_size / (1 - train_size) * len(remaining_idxs))]

    # Get the corresponding sentences and client_ids for each set of indices
    train = df.loc[df.index.isin(train_idxs)]
    dev = df.loc[df.index.isin(dev_idxs)]
    test = df.loc[df.index.isin(test_idxs)]
    eval = df.loc[df.index.isin(eval_idxs)]

    return train, dev, test, eval

filtered_validated = pd.read_csv(args.data + '/sw/validated_without_dialect_domain_eval.tsv', sep='\t', low_memory=False)
train, dev, test, eval = split_data(filtered_validated, args.train, args.dev, args.test, args.eval)


# save my train, dev and test sets
train.to_csv(args.data + '/sw/train.tsv', index=False, sep='\t')
dev.to_csv(args.data + '/sw/dev.tsv', index=False, sep='\t')
test.to_csv(args.data + '/sw/test.tsv', index=False, sep='\t')
eval.to_csv(args.data + '/sw/eval.tsv', index=False, sep='\t')
