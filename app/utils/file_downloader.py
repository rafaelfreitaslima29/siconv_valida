import os
import requests
from urllib.parse import urlparse

class FileDownloader:


    def __init__(self) :
        self.url = 'https://repositorio.dados.gov.br/seges/detru/siconv.zip'
        self.file_name = 'arquivos.zip'
        self.dest_folder = 'files/csv'
        self.file_path = None


    def set_url(self, url):
        self.url = url
        if not self.file_name:
            self.file_name = os.path.basename(urlparse(url).path)
        self._update_file_path()


    def set_file_name(self, name):
        self.file_name = name
        self._update_file_path()


    def set_dest_folder(self, folder):
        self.dest_folder = folder
        self._update_file_path()


    def _update_file_path(self):
        if self.url and self.file_name:
            os.makedirs(self.dest_folder, exist_ok=True)
            self.file_path = os.path.join(self.dest_folder, self.file_name)


    def run_download(self):
        if not self.url or not self.file_path:
            raise ValueError("URL and file path must be set before downloading.")

        print(f"Downloading from: {self.url}")
        print(f"Saving to: {self.file_path}")

        try:
            with requests.get(self.url, stream=True, timeout=60, headers={'User-Agent': 'Mozilla/5.0'}) as r:
                r.raise_for_status()
                with open(self.file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            print("Download completed successfully!")

        except requests.exceptions.ChunkedEncodingError as e:
            print(f"Connection error during download: {e}")
            print("Try again or use a download manager like wget/curl.")

        except requests.exceptions.RequestException as e:
            print(f"Download error: {e}")


    def get_file_path(self):
        return self.file_path
