from pydub import AudioSegment
import os
import glob
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add padding to segmented audio files.")
    parser.add_argument(
        "--source-dir",
        type=str,
        required=True,
        help="Path to segmented audio folder.",
    )
    parser.add_argument(
        "--target-dir",
        type=str,
        required=True,
        help="Path to save padded audio.",
    )
    args = parser.parse_args()

    # input path to segmentedAudio folder here and create the paddedAudio folder and put its path here as well.
    source_dir = args.source_dir
    target_dir = args.target_dir

    os.makedirs(target_dir, exist_ok=True)

    wav_files = glob.glob(os.path.join(source_dir, "*.wav"))

    for wav_file in wav_files:
        audio = AudioSegment.from_wav(wav_file)

        # duration of silence in ms
        silence = AudioSegment.silent(
            duration=400
        )  # This is length of silence to pad beginning and end of segments. You can change this to whatever you want.
        new_audio = silence + audio + silence
        new_file_path = os.path.join(target_dir, os.path.basename(wav_file))
        new_audio.export(new_file_path, format="wav")

    print("Processing complete. Modified files are saved in:", target_dir)
