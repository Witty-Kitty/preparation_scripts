import argparse
import pandas as pd
import string

# Text normalisation function
# 1. we lower all letters
# 2. we get rid of leading and trailing spaces
# 3. we get rid of extra spaces
# 4. remove punctuation
# 5. dropping all the sentences which have digits, these look quite problematic!!
# 6. remove all characters not in my 'allowed' list

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="add the path to your file", required=True)
args = parser.parse_args()

def normalise_text(df):
    df.loc[:,'sentence'] = df['sentence'].apply(lambda s: s.lower())
    df.loc[:,'sentence'] = df['sentence'].apply(lambda s: s.strip())
    df.loc[:,'sentence'] = df['sentence'].apply(lambda s: " ".join(s.split()))
    df.loc[:,'sentence'] = df['sentence'].apply(lambda s: s.translate(str.maketrans('', '', string.punctuation)))
    df = df[~df['sentence'].str.contains('\d')]
    characters_allowed = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    df.loc[:,'sentence'] = df['sentence'].apply(lambda s: ''.join(char for char in s if char in characters_allowed or char == ' '))

    return df

df0 = pd.read_csv(args.file, sep='\t', low_memory=False)
df = normalise_text(df0)
df.to_csv(args.file[:-4] + '_normalised.tsv', index=False, sep='\t')
