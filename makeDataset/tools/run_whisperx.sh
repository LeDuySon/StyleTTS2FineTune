#!/bin/bash

# Check if the input folder is provided
if [ -z "$1" ]; then
    echo "Please provide the input folder."
    exit 1
fi

input_folder="$1"
output_folder=${2:-srt}

num_speakers=1

# Process each .wav file in the input folder
for i in "$input_folder"/*.wav; do
    whisperx "$i" --model large-v3 \
        --language en \
        --output_format srt \
        --condition_on_previous_text True \
        --max_line_count 1 \
        --segment_resolution sentence \
        --batch_size 64 \
        --max_speakers ${num_speakers} \
        --output_dir ${output_folder} \
        --print_progress True 
done
