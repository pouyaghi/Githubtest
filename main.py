print("my name is pouya")
# from TTS.api import TTS
# tts=TTS(model_path="https://huggingface.co/Kamtera/persian-tts-male1-vits/resolve/main/checkpoint_88000.pth",
#         config_path="https://huggingface.co/Kamtera/persian-tts-male1-vits/resolve/main/config.json")
# tts.tts_to_file(".زندگی فقط یک بار است؛ از آن به خوبی استفاده کن",file_path='output.wav')

from TTS.config import load_config
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

model_path ="../best_model_female.pth" # Absolute path to the model checkpoint.pth
config_path ="../config.json" # Absolute path to the model config.json

synthesizer = Synthesizer(
        model_path,
        config_path,
        
    )
text = "باورم نمیشه. آیا این تو هستی که به من سلام کردی؟"
wavs = synthesizer.tts(text)
synthesizer.save_wav(wavs, 'sp.wav')