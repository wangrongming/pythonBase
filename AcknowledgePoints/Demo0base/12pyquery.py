#模仿jquery实现的解析工具库
#安装：pip install pyquery

from pyquery import PyQuery as pq
html = ''

#字符串初始化
doc = pq(html)
print(doc('a #lis-a .li'))

doc = pq(url='http://www.baidu.com')
doc = pq(filename='demo.html')
print(doc('head'))

#查找元素
    #子元素
    doc = pq(filename='demo.html')
    items = doc('.list')
    items.find('li')#根据css查找
    items.children()#查找所有的直接子元素
    items.children('.active')
    items.parent()#查找一个父元素
    items.parents('.wa')#所有祖先父元素
    li=doc('.list .item-0.active')
    li.siblings('.active')#获取所有兄弟元素

#遍历元素
    a = doc('li').items()#生成一个  生成器

#获取信息
    #获取属性
    a = doc('.list')
    a.attr('href')#获取属性
    a.attr.href#获取属性
    a.text()#获取文本
    a.html()#获取html

#DOM操作
    a.removeClass('active')#addclass
    a.add_class('active')
    a.attr('name','link')#有修改 无新增

#伪类选择器
    li = doc('li:first-child')#获取第一个标签
    li = doc('li:last-child')#获取最后一个标签
    li = doc('li:nth-child(2)')#获取制定下标的元素
    li = doc('li:gt(2)')#获取下标第二个以后的元素
    li = doc('li:nth-child(2n)')#获取下标为偶数的元素
    li = doc('li:contains(second)')#获取内容包含second的元素





