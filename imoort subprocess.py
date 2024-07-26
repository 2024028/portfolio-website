from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, this is a text-to-speech example."

# Create a gTTS object
tts = gTTS(text)

# Save the speech to an audio file
tts.save("output.mp3")

# Play the audio file
os.system("mpg321 output.mp3")  # This command may vary depending on your system


