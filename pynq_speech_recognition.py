#!/usr/bin/env python
# coding: utf-8

# In[32]:


from pynq.overlays.base import BaseOverlay
base = BaseOverlay("base.bit")
pAudio = base.audio


# In[41]:


pAudio.record(5)
pAudio.save("voiceInput_1.pdm")


# In[42]:


pAudio.load("/home/xilinx/jupyter_notebooks/voiceInput_1.pdm") #pAudio.load("/home/xilinx/pynq/lib/tests/pynq_welcome.pdm")
pAudio.play()


# In[43]:


import time
import numpy as np

start = time.time()
af_uint8 = np.unpackbits(pAudio.buffer.astype(np.int16)
                         .byteswap(True).view(np.uint8))
end =  time.time()

print("Time to convert {:,d} PDM samples: {:0.2f} seconds"
      .format(np.size(pAudio.buffer)*16, end-start))
print("Size of audio data: {:,d} Bytes"
      .format(af_uint8.nbytes))


# In[44]:


import time
from scipy import signal

start = time.time()
af_dec = signal.decimate(af_uint8,8,zero_phase=True)
af_dec = signal.decimate(af_dec,6,zero_phase=True)
af_dec = signal.decimate(af_dec,2,zero_phase=True)
af_dec = (af_dec[10:-10]-af_dec[10:-10].mean())
end = time.time()
print("Time to convert {:,d} Bytes: {:0.2f} seconds"
      .format(af_uint8.nbytes, end-start))
print("Size of audio data: {:,d} Bytes"
      .format(af_dec.nbytes))
del af_uint8


# In[45]:


from IPython.display import Audio as IPAudio
IPAudio(af_dec, rate = 32000)


# In[46]:


from scipy.io.wavfile import write
import os


# Ensure af_dec is in int16 format, as WAV files typically store data this way
af_dec_int16 = (af_dec * 32767).astype(np.int16)

# Save as a valid PCM WAV file
output_wav = "input_pcm_converted_to_wav.wav"

file_path = "/home/xilinx/jupyter_notebooks/input_pcm_converted_to_wav.wav"

if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print(f"Previous voice recording at {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")

write(output_wav, 32000, af_dec_int16)
print(f"New audio successfully saved as {output_wav}")


# In[47]:


import speech_recognition as sr

recognizer = sr.Recognizer()


audio_file = "input_pcm_converted_to_wav.wav"   # incearca direct cu af_dec ca audio_file
with sr.AudioFile(audio_file) as source:
    print("Loading audio file...")
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Heard: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))
    


# In[48]:


from pynq.overlays.base import BaseOverlay
base_overlay = BaseOverlay("base.bit")

valid_on_commands = ["turn on the light", "turn the light on", "turn light on", "turn on light", "light on", "aprinde lumina", "aprinde"]
valid_off_commands = ["turn off the light", "turn the light off", "turn light off", "turn off light", "light off", "stinge lumina", "stinge"]


for command in valid_on_commands:
    print("Matching " + command + "with: " + text)
    if command in text:
        print("Turning light on")
        base_overlay.leds[0].on()
        break

for command in valid_off_commands:
    print("Matching " + command + "with: " + text)
    if command in text:
        print("Turning light off")
        base_overlay.leds[0].off()
        break 


# In[20]:





# In[ ]:




