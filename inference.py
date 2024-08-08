# REF: https://github.com/korakoe/StyleTTS2lib

import os 
from styletts2 import tts

experiment_name = "Parrot_Trump_1hour30mins"
model_name = "epoch_2nd_00015.pth"

checkpoint_folder = f"/workspace/StyleTTS2/Models/{experiment_name}"
config_path = os.path.join(checkpoint_folder, "config_ft.yml")
model_checkpoint_path = os.path.join(checkpoint_folder, model_name)

ref_voice_path = "all_audios/trump1.wav"

output_folder = os.path.join("outputs", experiment_name, model_name.split(".")[0])
os.makedirs(output_folder, exist_ok=True)

test_texts = ["Friends, delegates and fellow citizens. I stand before you this evening with a message of confidence, strength and hope. Four months from now, we will have an incredible victory, and we will begin the four greatest years in the history of our country.",
              "Getting fired from Apple was the best thing that could have ever happened to me. The heaviness of being successful was replaced by the lightness of being a beginner again. It freed me to enter one of the most creative periods of my life."]

for idx, text in enumerate(test_texts):
    # Specific paths to a checkpoint and config can also be provided.
    other_tts = tts.StyleTTS2(model_checkpoint_path=model_checkpoint_path, 
                            config_path=config_path)

    # Specify target voice to clone. When no target voice is provided, a default voice will be used.
    save_path = os.path.join(output_folder, f"{idx}.wav")
    other_tts.inference(text=text,
                        target_voice_path=ref_voice_path,
                        alpha=0.3,
                        beta=0.7,
                        diffusion_steps=20,
                        embedding_scale=1,
                        output_sample_rate=24000,
                        output_wav_file=save_path,)
