import requests
from PIL import ImageFilter,Image
#1素材获取
#2 图片预处理
    # 读取原始图片素材
    # 将彩色图片二值化为黑白图片
    # 去除背景噪点

#1素材获取
def downloads_pic(**kwargs):
    pic_name = kwargs.get('pic_name', None)

    url = 'https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha&nocache=1528726744320'
    res = requests.get(url, stream=True)
    with open('D:\\pythonWorkplace\\AcknowledgePoints\\Demo0base\\img\\' + pic_name+'.bmp', 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()


if __name__ == '__main__':
    for i in range(1,16):
        downloads_pic(pic_name=str(i))

