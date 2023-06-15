for f in *.mp3; 
do 
	ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 48000 "${f%%.*}-int.wav"; 
	rm "$f"
done 
for f in *.wav; 
do 
	ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 16000 "${f%%-*}.wav"; 
	rm "$f"
done

