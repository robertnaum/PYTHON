from gtts import gTTS
import os

def create_audiobook(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    tts = gTTS(text=text,lang='en')
    tts.save(output_file)
    print(f"Audiobook saved as {output_file}")

base_dir = os.path.dirname(__file__)
text_file = os.path.join(base_dir, 'texts', 'audiobook.txt')
output_file = 'audiobook.mp3'
create_audiobook(text_file, output_file)
# os.system(f'start {output_file}')
print (__file__)