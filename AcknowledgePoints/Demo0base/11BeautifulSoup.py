#beautiful安装
#pip install beautifulsoup4
#用法讲解
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())#代码格式化
print(soup.title)
print(soup.head)
print(soup.p)#获取标签
print(soup.p.attrs['name'])#获取标签属性名称
#嵌套选择
print(soup.head.title.string)#获取title里面的内容

#标签选择器
    #获取子节点 子孙节点
    print(soup.p.contents)
    print(soup.p.children)#子节点
    print(soup.p.descendants)#获取所有子、孙节点
    print(soup.a.parent)#父节点
    print(soup.a.parents)#父节点、祖先节点
    print(soup.a.next_siblings)#后面兄弟节点
    print(soup.a.previous_siblings)#前面兄弟节点

#标准选择器
    #name：标签名字
    find_all(name,attrs,recursive,text,**kwargs)
    soup.find_all('url')#输出为列表形式
    #attrs:标签属性
    soup.find_all(attrs={'id':list-1})
    soup.find_all(class_={'id':list-1})#直接写class 会识别失败
    soup.find_all(text='Foo')
    #查找不存在的标签返回None


#css选择器
    print(soup.select('.panel .panel-heading'))
    print(soup.select('url li'))
    print(soup.select('#list-2 .element'))
    for ul in soup.select('url'):
        print(ul['id'])
        print(ul.attrs['id'])#获取属性
        print(ul.get_text())#获取内容
