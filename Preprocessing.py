import re
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def process_text(transcript_file):
    with open(transcript_file, 'r') as file:
        text = file.read()

    text = re.sub(r'[\W_]+', ' ', text)
    word_tokens = nltk.word_tokenize(text.lower())
    processed_words = [lemmatizer.lemmatize(word) for word in word_tokens if word not in stop_words]
    processed_text = ' '.join(processed_words)

    return processed_text

directoryRead = 'transcript_files'
directoryWrite = 'transcript_files_processed'

files = os.listdir(directoryRead)
for filename in files:
    file_path_read = os.path.join(directoryRead, filename)
    if os.path.isfile(file_path_read):
        processed_transcript = process_text(file_path_read)
        file_path_write = os.path.join(directoryWrite, filename)
        with open(file_path_write, 'w') as file:
            file.write(processed_transcript)