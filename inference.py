# REF: https://github.com/korakoe/StyleTTS2lib

import os 
from styletts2 import tts

checkpoint_folder = "/workspace/StyleTTS2/Models/LibriTTS"
config_path = os.path.join(checkpoint_folder, "config_ft.yml")
model_checkpoint_path = os.path.join(checkpoint_folder, "epoch_2nd_00020.pth")

text = "Friends, delegates and fellow citizens. I stand before you this evening with a message of confidence, strength and hope. Four months from now, we will have an incredible victory, and we will begin the four greatest years in the history of our country."

# Specific paths to a checkpoint and config can also be provided.
other_tts = tts.StyleTTS2(model_checkpoint_path=model_checkpoint_path, 
                          config_path=config_path)

# Specify target voice to clone. When no target voice is provided, a default voice will be used.
other_tts.inference(text=text,
                    target_voice_path=None,
                    alpha=0.3,
                    beta=0.7,
                    diffusion_steps=10,
                    embedding_scale=1,
                    output_sample_rate=24000,
                    output_wav_file="test.wav",)
