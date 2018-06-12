图像识别与文字处理
OCR:光学文字识别

Pillow
from PIL import Image,ImageFilter
kitten = Image.open("G:\\Pincure\\sdfx.png")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("G:\\Pincure\\kitten_blurred.jpg")
blurryKitten.show()

Tesseract
一个OCR库
下载地址:https://code/google.com/p/tesseract-ocr/downloads/list
#linux下载
apt-get install tesseract-ocr
#设置新的环境变量 让Tesseract知道训练的数据文件存储在哪里
export TESSDATA_PREFIX=/usr/local/share/
#NumPy 数学方法把图片组成巨大的像素组
pip install numpy
#处理格式规范的文字
tesseract text.tif textoutput 
#从网站图片中抓去文字
#读取验证码与训练Tesseract
100个样本 500个字符
a-z,A-z,0-9一共62个字符
