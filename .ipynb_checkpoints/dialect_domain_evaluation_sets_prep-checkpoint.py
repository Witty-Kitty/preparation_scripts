import argparse
import pandas as pd
import string
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, help="add the path to your cv corpus directory", required=True)
args = parser.parse_args()

validated = pd.read_csv(args.data + '/sw/validated.tsv', sep='\t', low_memory=False)
#taking out double quotes from the data, if not closed, they cause errors in the data preparation pipeline
validated['sentence'] = validated['sentence'].str.replace('"', '')


# filtering out data from the following PRs. These are either domain data or dialect and variant data. These subsets are intended for fine-tuning and evaluation respectively.
# so far only the variant/dialect sets have been uploaded 
# https://github.com/common-voice/common-voice/pull/3957 by Badili innovations, livestock data
# https://github.com/common-voice/common-voice/pull/3970 by Badili innovations, livestock data
# https://github.com/common-voice/common-voice/pull/3640 by Kat, Dialect/Variant data

kiunguja = pd.read_csv('experiment_data/sw-kiunguja.txt', header=None)
baratz = pd.read_csv('experiment_data/sw-baratz.txt', header=None)
kibajuni = pd.read_csv('experiment_data/sw-kibajuni.txt', header=None)
kimakunduchi = pd.read_csv('experiment_data/sw-kimakunduchi.txt', header=None)
kimvita = pd.read_csv('experiment_data/sw-kimvita.txt', header=None)
kipemba = pd.read_csv('experiment_data/sw-kipemba.txt', header=None)
kitumbatu = pd.read_csv('experiment_data/sw-kitumbatu.txt', header=None)

#we also filter out sentences/transcripts in our data which contain characters not in the standard kiswahili alphabet
sentences_with_unusual_characters = pd.read_fwf('experiment_data/sentences_with_unusual_characters.txt', header=None)

# function to save our dialect/variant evaluation sets, we want to save these in alignment with the rest of our subsets
def dialect_evaluation_sets(df):
    dialect_set = []
    for idx, value in validated['sentence'].items():
        for idx2, value2 in df[0].items():
            if value == value2:
                dialect_set.append(idx)

    df = validated[validated.index.isin(dialect_set)]

    return df    

dialect_evaluation_sets(kiunguja).to_csv(args.data + '/sw/eval_dialect_kiunguja.tsv', index=False, sep='\t')
dialect_evaluation_sets(kibajuni).to_csv(args.data + '/sw/eval_dialect_kibajuni.tsv', index=False, sep='\t')
dialect_evaluation_sets(baratz).to_csv(args.data + '/sw/eval_dialect_baratz.tsv', index=False, sep='\t')
dialect_evaluation_sets(kimakunduchi).to_csv(args.data + '/sw/eval_dialect_kimakunduchi.tsv', index=False, sep='\t')
dialect_evaluation_sets(kimvita).to_csv(args.data + '/sw/eval_dialect_kimvita.tsv', index=False, sep='\t')
dialect_evaluation_sets(kipemba).to_csv(args.data + '/sw/eval_dialect_kipemba.tsv', index=False, sep='\t')
dialect_evaluation_sets(kitumbatu).to_csv(args.data + '/sw/eval_dialect_kitumbatu.tsv', index=False, sep='\t')

dialect_evaluation_sets(kiunguja).to_csv(args.data + '/sw/eval_dialect_kiunguja.csv', index=False)
#we then filter them out of the df that we continue working with
filter_out = pd.concat([kiunguja[0],baratz[0],kibajuni[0],kimakunduchi[0],kimvita[0],kipemba[0],kitumbatu[0],sentences_with_unusual_characters[0]], ignore_index=True)
filter_out = pd.DataFrame(filter_out)

# finding the instances from the filter_out set
filter_sets = []
for idx, value in validated['sentence'].items():
    for idx2, value2 in filter_out[0].items():
        if value == value2:
            filter_sets.append(idx)

# filtering out the instances in out filter set
filtered_validated = validated[~validated.index.isin(filter_sets)]
filtered_validated.to_csv(args.data + '/sw/validated_without_dialect_domain_eval.tsv', index=False, sep='\t')

