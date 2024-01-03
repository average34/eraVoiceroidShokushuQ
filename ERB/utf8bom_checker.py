import os

def is_utf8_with_bom(file_path):
    """指定されたファイルがUTF-8 with BOMであるかどうかを確認する関数"""
    with open(file_path, 'rb') as file:
        first_bytes = file.read(3)
        return first_bytes == b'\xef\xbb\xbf'

def find_non_utf8_with_bom_files(start_path, extensions=('.txt', '.ERB')):
    """
    指定されたディレクトリとサブディレクトリを再帰的に走査し、
    指定された拡張子を持ち、かつUTF-8 with BOMでないファイルを探す関数
    """
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                if not is_utf8_with_bom(file_path):
                    yield file_path

start_path = '.'  # 現在のディレクトリから探索を開始する。必要に応じて変更する。

for non_utf8_file in find_non_utf8_with_bom_files(start_path):
    print(non_utf8_file)  # UTF-8 with BOMでないファイルのパスを出力する。

#最後にこれを表示
input()