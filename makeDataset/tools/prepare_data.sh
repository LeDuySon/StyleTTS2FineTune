# create dataset folders
python makeDataset/tools/srtsegmenter.py

# add silence (Optional)
python makeDataset/tools/silencebuffer.py --input-folder dataset/audio --output-folder dataset/audio

# run transcription
bash makeDataset/tools/run_whisperx.sh dataset/audio dataset/srt

# run segmenter (need to configure the buffer time to avoid interrupt word in the end of segment)
python makeDataset/tools/srtsegmenter.py

# add padding silence into the end of segment 
python makeDataset/tools/add_padding.py --source-dir dataset/segmentedAudio --target-dir dataset/segmentedAudioPadding

