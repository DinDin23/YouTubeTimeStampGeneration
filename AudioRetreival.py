import feedparser
import requests
import os
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context
csv.field_size_limit(100000000)  

def extract_rss_urls(files):
    rss_urls = []
    for filename in files:
        file_path = os.path.join('all-podcasts-dataset', filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                tsv_reader = csv.reader(file, delimiter='\t')
                for row in tsv_reader:
                    for value in row:
                        if value.startswith('http') and ('/rss' in value or '/feed' in value):
                            rss_urls.append(value)
    return rss_urls

directory = 'all-podcasts-dataset'
files = os.listdir(directory)
rss_url_list = extract_rss_urls(files)

for rss_url in rss_url_list:
    feed = feedparser.parse(rss_url)
    download_dir = "audio_files"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Iterate through the feed entries
    for entry in feed.entries:
        if "enclosures" in entry:
            for enclosure in entry.enclosures:
                # Check if the enclosure is an MP3 file
                if enclosure.type == "audio/mpeg":
                    # Construct the file name from the entry title
                    file_name = entry.title.replace("/", "_") + ".mp3"
                    file_path = os.path.join(download_dir, file_name)

                    # Download the MP3 file
                    print(f"Downloading: {file_name}")
                    response = requests.get(enclosure.href)
                    with open(file_path, "wb") as f:
                        f.write(response.content)

