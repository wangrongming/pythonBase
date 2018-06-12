#非python独有  re模块实现
    import re
    result = re.match('^(.*?)$','hello',re.S)#匹配模式  直会从第一个字符开始去匹配
    print(result)
    print(result.group(1))
    print(result.span())

    #转义
    #$ .  等特殊字符配置需要进行转义才可以


    #re.search 扫描整个字符串并返回第一个成功的匹配
    #re.findall()#搜索字符串，一列表形式返回全部能匹配的字符串
    #re.sub #替换字符串中每一个匹配的子串后，返回替换后的字符串
    re.sub('\d+','',content)

    #通常sub替换掉无用的，用findall进行匹配

    #re.compile 预编译
