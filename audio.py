from gtts import gTTS
import os

MyText = "Text to speech with python"
language = 'en'
Output_file = gTTS(text=MyText, lang=language, slow=False)
Output_file.save('output.mp3')
os.system('start output.mp3')
print(Output_file)