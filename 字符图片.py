from PIL import Image # PIL 是一个 Python 图像处理库


codelib = """"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."""
count = len(codelib)
# 是我们的字符画所使用的字符集，一共有 70 个字符，字符的种类与数量可以自己根据字符画的效果反复调试的
def transform(image_file):
    img = image_file.convert('L')
    codepic=''
    for h in range(0,img.size[1]):
        for w in range(0,img.size[0]):
            gray = img.getpixel((w,h))
            codepic=codepic+codelib[int((count*gray)/256)]
        codepic = codepic+'\n'
    return codepic

image_file=Image.open('1.jpg')
image_file=image_file.resize((int(image_file.size[0]*0.5),int(image_file.size[1]*0.25)))
# image_file=image_file.resize((200,200))
txt = open('demo.txt','w')
txt.write(transform(image_file))
txt.close()