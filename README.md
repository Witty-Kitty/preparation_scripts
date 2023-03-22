1. the dataset_splits_evaluation_sets_prep.py script
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - it expects to find the 'experiment_data' directory with .txt files of the domain and dialect/variant data for fine-tuning and evaluation (so far only dialect/variant) data included
  - it outputs train, dev and test sets as well as evaluation sets into the 'experiment_data' directory.
  - to-do: not yet sure how to add new data to this split with CV versions beyond 13. 

2. the mp3_to_wav.sh script
  - this should be places in the 'clips' directory within yout cv corpus directory. eg. inside /media/datasets/cv-corpus-13.0-2023-03-09/sw/clips
  - it converts all the audio .mp3 files into .wav format
  - it them creates a 'clips_wav' directory and moves all the .wav files into it

3. the coqui_prep.py script
  - the --data flag expects you to pass the path to your cv corpus directory eg. /media/datasets/cv-corpus-13.0-2023-03-09
  - the --subset flag expects the path to the csv for the data subset you are processing, eg. train.csv, dev.csv or any of the evaluation subsets created with the previous scrips
  - it outputs, into the 'experiment_data' directory, .csv files for each of these subsets in the format that coqui STT expects
  
  4. the experiment0.py script
    - the --train flag expects the path to the csv for the training data ie. train.csv (this is in the experiment_data directory)
    - it outputs .csv files with the training subsets for experiment0. 
