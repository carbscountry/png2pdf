import os
from PIL import Image

def main():
    # Irresistbleディレクトリのパス
    dir_path = os.path.join(os.path.dirname(__file__), 'Irresistble')
    # p*.pngファイルを取得し、数字部分でソート
    files = [f for f in os.listdir(dir_path) if f.lower().endswith('.png') and f.lower().startswith('p')]
    files.sort(key=lambda x: int(x[1:4]))  # pXXX.png のXXX部分でソート
    images = [Image.open(os.path.join(dir_path, f)).convert('RGB') for f in files]
    if images:
        images[0].save(os.path.join(os.path.dirname(__file__), 'Irresistble.pdf'), save_all=True, append_images=images[1:])
        print('Irresistble.pdfを作成しました')
    else:
        print('画像が見つかりません')

if __name__ == "__main__":
    main()
