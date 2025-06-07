import os
from PIL import Image

_dir = 'map_of_accounting'
def main():
    # Irresistbleディレクトリのパス
    dir_path = os.path.join(os.path.dirname(__file__), _dir)
    # p*.pngファイルを取得し、数字部分でソート
    files = [f for f in os.listdir(dir_path) if f.lower().endswith('.png') and f.lower().startswith('p')]
    files.sort(key=lambda x: int(x[1:4]))  # pXXX.png のXXX部分でソート
    images = [Image.open(os.path.join(dir_path, f)).convert('RGB') for f in files]
    if images:
        images[0].save(os.path.join(os.path.dirname(__file__), f'{_dir}.pdf'), save_all=True, append_images=images[1:])
        print('pdfを作成しました')
    else:
        print('画像が見つかりません')

if __name__ == "__main__":
    main()
