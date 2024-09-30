#voice recorder
import sounddevice as sd
from scipy.io.wavfile import write

duration=15
sample_rate=44100

def record_voice(duration,sample_rate):
    print("READING")
    audio=sd.rec(int(duration* sample_rate),samplerate=sample_rate,channels=2)
    sd.wait()
    return audio


audio=record_voice(duration,sample_rate)

#save the recorded voice to a file

file_name='pro.wav'
write(file_name,sample_rate,audio)
print(f"audio saved as{file_name}")


