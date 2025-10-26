import os
import zipfile
import subprocess


class ZipManager:
    def __init__(self):
        pass


    def run_compress(self, source_path, output_path):
        """
        Compacta um arquivo ou pasta em um arquivo zip.
        :param source_path: caminho do arquivo ou pasta a ser compactada
        :param output_path: caminho onde será salvo o arquivo zip
        """
        source_path = os.path.abspath(source_path)
        output_path = os.path.abspath(output_path)

        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isdir(source_path):
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, source_path)
                        zipf.write(full_path, arcname)
            else:
                zipf.write(source_path, os.path.basename(source_path))

        print(f"Compressed '{source_path}' to '{output_path}'")



    def run_extract(self, zip_path, extract_to):
        """
        Descompacta um arquivo ZIP.
        :param zip_path: Caminho para o arquivo ou pasta a ser descompactado
        :param extract_to: Caminho para salvar o descompactado
        """
        zip_path = os.path.abspath(zip_path)
        extract_to = os.path.abspath(extract_to)
        os.makedirs(extract_to, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_to)

        print(f"Extracted '{zip_path}' to '{extract_to}'")
