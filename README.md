# PYNQ-Speech-Recognition-
Voice-enabled controls on the PYNQ-Z1 board using speech recognition. <br/>
Uses the PDW Microphone of the PYNQ board. <br/>
Converts the PDW voice input to PCM 16-bit Mono, and then finally to WAV file format. <br/>
Sends the converted WAV file to Google Spech Recognition API and matches the spoken command with the available commands. <br/>
Enables users to use their voice in order to control hardware, such as turning lights on/off, etc. <br/>
The board's microphone listens for spoken commands 5 seconds at a time, then converts it into text and matches it with the available commands. <br/>
<br/>
Requirements: <br/>
1. PYNQ Z1 board<br/>
2. 2 Ethernet cables with network connection <br/>
3. Jupyter Notebook 
![pynqboard](https://github.com/user-attachments/assets/75be85bd-c0b0-42a4-aee2-ffdddd7f30de)
