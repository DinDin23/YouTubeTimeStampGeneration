import whisper
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("base")

directoryRead = 'audio_files'
directoryWrite = 'transcript_files'
files = os.listdir(directoryRead)

for filename in files:
    file_path_read = os.path.join(directoryRead, filename)
    if os.path.isfile(file_path_read):
        resultT = model.transcribe(file_path_read)['text']
        fileNameWrite = filename[:-4] + '.txt'
        file_path_write = os.path.join(directoryWrite, fileNameWrite)
        with open(file_path_write, 'w') as fileWrite:
            fileWrite.write(resultT)
            