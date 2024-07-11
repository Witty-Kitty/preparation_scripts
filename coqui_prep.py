import pandas as pd
import re
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, help="add the path to your cv corpus directory", required=True)
parser.add_argument("--subset", type=str, help="add the path to the csv for the data subset you are processing, ie. train.csv", required=True)
args = parser.parse_args()

def find_audio_size(subset_dataframe):
    #   Find the size, in bits, of the .wav audio files using sox
    regex = re.compile(r'(File Size *:) ([\d|\.]*)')
    size = []
    for index, row in subset_dataframe.iterrows():
        prop = subprocess.run(["soxi", args.data + "/sw/clips/" + subset_dataframe.loc[index]['path'][:-4] + ".wav"], text=True, capture_output=True)
        match = re.search(regex, str(prop))
        if match:
            size.append([index, match.group(2)])
        else:
            print("No match found for file:", subset_dataframe.loc[index]['path'])
        #size.append([index,regex.search(str(prop)).group(2)])

    audio_sizes = pd.DataFrame(size)
    audio_sizes = audio_sizes.set_index(0)

#   Add the size column to the dataframe
    output_df = pd.concat([subset_dataframe,audio_sizes], axis=1)
    output_df['path'] = output_df['path'].str[:-4] + '.wav'
    output_df['path'] = args.data + '/sw/clips/' + output_df['path']
#   take only the columns needed for training with coqui ai STT toolkit
    output_df = output_df[['path', 1, 'sentence']]
    output_df.columns = ['wav_filename', 'wav_filesize', 'transcript']
    output_df['wav_filesize'] = output_df['wav_filesize'].astype(float).astype(int)
    output_df.to_csv(args.data + '/sw/' + args.subset[:-4] + '_for_coqui.csv', index=False, lineterminator='\n')

subset = pd.read_csv(args.data + '/sw/' + args.subset, sep='\t', low_memory=False)
find_audio_size(subset)
