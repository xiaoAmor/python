from PIL import Image
import argparse
#字符画所使用的字符集 70个
#灰度值小的用前面的字符
parser=argparse.ArgumentParser()
parser.add_argument("file")#输入文件
parser.add_argument('-o', '--output')#输出文件
parser.add_argument('--width', type=int, default=80)#输出字符宽度
parser.add_argument('--height', type=int, default=80)#输出字符画高
#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
#必须不同的字母
#ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

ascii_char = list("123456789hkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return ' '
    length=len(ascii_char)
    #灰度值公式
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]
    #return ascii_char[0]
if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt=""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w')as f:
            f.write(txt)


