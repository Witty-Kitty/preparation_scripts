1. the dialect_domain_evaluation_sets_prep.py script
  - this script creates evaluation sets for ouur dialect and domain data
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - it expects to find the 'experiment_data' directory with .txt files of the domain and dialect/variant data for fine-tuning and evaluation (so far only dialect/variant) data included
  - it outputs validated_without_dialect_domain_eval.tsv as well as the dialect evaluation sets into the --data directory passed to the script. 

2. the experimental_splits.py script
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - the --train, --dev, --test and --eval flags expect you to pass in the desired size of the respective set, eg. 0.6 for 60%. Default values of 0.6, 0.15, 0.15 and 0.1 respectively are passed in
  - it outputs train.tsv, dev.tsv, test.tsv and eval.tsv files into the --data directory passed to the script

3. the age_gender_evaluation_sets_prep.py script
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - it reads in the eval.tsv file and outputs age, gender and ageXgender evaluation splits into the --data directory passed to the script

4. the mp3_to_wav.sh script
  - this should be placed in the 'clips' directory within yout cv corpus directory. eg. inside /media/datasets/cv-corpus-13.0-2023-03-09/sw/clips
  - it converts all the audio .mp3 files into .wav format first with a rate of 48kHz aand then downsamples to 16kHz which is the expected for coqui.ai 
  - it them creates a 'clips_wav' directory and moves all the .wav files into it

5. the coqui_prep.py script
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - the --subset flag expects the path to the tsv for the data subset you are processing, eg. train.tsv, dev.tsv or any of the evaluation subsets created with the previous scrips
  - it outputs .csv files for each of these subsets into the --data directory passed to the script. These files are in the format that coqui STT expects
  
6. the experiment0.py script
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - the --dups flag expects you to pass in the number of duplicates allowed in each training set 
  - it outputs .tsv files with the training subsets for experiment0. (note that we do not make any changes to the dev, test and eval subsets. These are unchanged for comparability between experiments)

7. the normalise.py script
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - the --file flag expects the path to the tsv for the data subset you are processing, eg. train.tsv, dev.tsv
  - it outputs .tsv files with normalised text of the selected subset
