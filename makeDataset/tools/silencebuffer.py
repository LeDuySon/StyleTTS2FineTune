import argparse 
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-folder", type=str, required=True)
    parser.add_argument("--output-folder", type=str, required=True)
    parser.add_argument("--silence", type=int, default=740)
    parser.add_argument("--min_silence_len", type=int, default=232)
    parser.add_argument("--silence_thresh", type=int, default=-70)
    args = parser.parse_args()
    
    audio_files = os.listdir(args.input_folder)
    
    for audio_file in audio_files:
        print(f"Process {audio_file}")
        # Load the WAV file
        audio_file_name = os.path.basename(audio_file).split(".")[0]
        audio = AudioSegment.from_wav(os.path.join(args.input_folder, audio_file))

        # Find silence. These are CRUCIAL. You need to play around with these values to get the best results. Took me about 20 min of testing.
        chunks = split_on_silence(audio,
            min_silence_len=args.min_silence_len, # minimum length of silence required for a split in ms
            silence_thresh=args.silence_thresh # volume threshold below which sound is considered silence
        )

        silence_chunk = AudioSegment.silent(duration=args.silence)  # amount of silence you want to add in milliseconds

        new_audio = AudioSegment.empty()
        for chunk in chunks:
            new_audio += chunk + silence_chunk 

        save_path = os.path.join(args.output_folder, audio_file_name + "_silenced.wav")
        new_audio.export(save_path, format="wav")