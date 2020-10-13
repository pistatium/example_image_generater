import os
import sys

from PIL import Image, ImageDraw, ImageFont

"""
OS に応じてパスを変更してください
例)
  WSL2: "/mnt/c/Windows/Fonts/YuGothB.ttc"
"""
FONT_PATH = os.environ.get("FONT_PATH", "/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc")


class Canvas:
    def __init__(self, width=1024, height=512):
        self.width = width
        self.height = height
        self.canvas = self._get_canvas()

    def draw_text(self, text: str, top: int = 0, left: int = 0, font_size: int = 64, text_color='#020011') -> 'Canvas':
        drawer = ImageDraw.Draw(self.canvas)
        drawer.text((top, left), text, fill=text_color, font=self._get_font(font_size))
        return self

    def get_canvas(self) -> Image:
        return self.canvas

    def save(self, path: str, file_name: str) -> str:
        write_to = os.path.join(path, file_name)
        self.canvas.save(write_to, 'PNG')
        return write_to

    def _get_canvas(self, background_color=(0, 0, 0, 0)) -> Image:
        return Image.new('RGBA', (self.width, self.height), background_color)

    def _get_font(self, font_size) -> ImageFont:
        return ImageFont.truetype(FONT_PATH, font_size)


def main():
    params = sys.argv
    if len(params) != 2:
        print("""使い方:
 引数に渡した文字が描写された画像を生成するコマンドです
 
 例) python3 {} '山路を登りながら'
        """.format(params[0]))
        return
    text = params[1]

    canvas = Canvas()
    canvas = canvas.draw_text(text)
    canvas.save(os.getcwd(), '{}.png'.format(text))
    print("{}.png を作成しました。".format(text))


if __name__ == '__main__':
    main()
