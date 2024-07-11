  GNU nano 4.8                                                                                   mp3_to_wav.sh                                                                                   Modified  
output_directory="/data/wav_clips"
#for f in *.mp3; 
#do 
#       ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 48000 "${f%%.*}-int.wav"; 
#        sleep 1
#       rm "$f"
#done 
for f in *.wav; 
do 
        ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 16000 "${output_directory}/${f%%-*}.wav";
#        sleep 1 
#       rm "$f"
done




