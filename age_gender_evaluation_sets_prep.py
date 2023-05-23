import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, help="add the path to your cv corpus directory", required=True)
args = parser.parse_args()

evaluation = pd.read_csv(args.data + '/sw/eval.tsv', sep='\t', low_memory=False)

# save my age and gender evaluation sets
evaluation[evaluation['gender'] == 'male'].to_csv(args.data + '/sw/eval_gender_male.tsv', index=False, sep='\t')
evaluation[evaluation['gender'] == 'female'].to_csv(args.data + '/sw/eval_gender_female.tsv', index=False, sep='\t')
evaluation[evaluation['age'] == 'twenties'].to_csv(args.data + '/sw/eval_age_20s.tsv', index=False, sep='\t')
pd.concat([evaluation[evaluation['age'] == 'thirties'], evaluation[evaluation['age'] == 'fourties'], evaluation[evaluation['age'] == 'fifties'], evaluation[evaluation['age'] == 'sixties']]).to_csv(args.data + '/sw/eval_age_o30s.tsv', index=False, sep='\t')

# save my age x gender evaluation sets
evaluation.loc[(evaluation['gender'] == 'male') & (evaluation['age'] == 'twenties')].to_csv(args.data + '/sw/eval_age_gender_20s_male.tsv', index=False, sep='\t')
evaluation.loc[(evaluation['gender'] == 'female') & (evaluation['age'] == 'twenties')].to_csv(args.data + '/sw/eval_age_gender_20s_female.tsv', index=False, sep='\t')
evaluation.loc[(evaluation['gender'] == 'female') & ~(evaluation['age'] == 'twenties') & ~(evaluation['age'] == 'teens')].to_csv(args.data + '/sw/eval_age_gender_o30s_female.tsv', index=False, sep='\t')
evaluation.loc[(evaluation['gender'] == 'male') & ~(evaluation['age'] == 'twenties') & ~(evaluation['age'] == 'teens')].to_csv(args.data + '/sw/eval_age_gender_o30s_male.tsv', index=False, sep='\t')
