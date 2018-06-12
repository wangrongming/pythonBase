http://scrapy-chs.readthedocs.io/zh_CN/latest/#最新的scrapy文档
#scrapy安装
#scrapy流程框架
#scrapy命令
#scrapy选择器的使用
#scrapy中spider用法
#scrapy中itemline的使用


#scrapy安装

    # windows
    # 1 pip install wheel
    # 2 lxml
    # www.lfd.uci.edu/~gohlke/pythonlibs/#lxml(pip install 下载好的文件)
    # 3 pyopenssl
    # http://pypi.python.org/pypi/pyOpenSSL#downloads
    # 4 Twisted
    # http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    # 5 pywin32
    # https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220
    # 6 scrapy安装
    # pip install scrapy

#anaconda下载安装  进行scrapy安装
    #conda install scrapy


#linux
#首先安装python3
    # sudo apt-get install python3-dev
    # sudo apt-get install bulid-essentail
    # sudo apt-get install libssl-dev
    # sudo apt-get install libffi-dev
    # sudo apt-get install libxml2
    # sudo apt-get install libxml2-dev
    # sudo apt-get install libxslt1-dev
    # sudo apt-get install zlib1g-dev
    # sudo apt-get install python3
    # sudo apt-get install python-pip
    #
    # pips install scrapy


#scrapy流程框架
    #抓取第一页
    #获取内容和下一页链接
    #保存爬取结果
    #翻页爬取

    #利用scrapy新建项目
        #scrapy startproject quotetutorial
        #scrapy genspider quotes quotes.toscrape.com
        #scrapy crawl quotes #执行爬虫 输出调试信息
        #scrapy crawl quotes -o quotes.json 输出结果进行保存
        #scrapy crawl quotes -o quotes.csv
        
        #scrapy shell quotes.toscrape.com #命令行交互模式
        
#scrapy命令
    genspider
        scrapy genspider [-t template] <name> <domain>
        scrapy genspider -t basic example example.com
    crawl
        scrapy crawl <spider>
        scrapy crawl myspider
    check
        scrapy check [-l] <spider>
    list#列出当前项目中所有可用的spider。每行输出一个spider。
        scrapy list
    scrapy fetch <url>
        scrapy fetch --nolog --headers http://www.example.com/ #使用Scrapy下载器(downloader)下载给定的URL，并将获取到的内容送到标准输出。
    scrapy view <url>
        #在浏览器中打开给定的URL，并以Scrapy spider获取到的形式展现。
    scrapy shell [url]
        #以给定的URL(如果给出)或者空(没有给出URL)启动Scrapy shell。
    scrapy settings [options]
        #在项目中运行时，该命令将会输出项目的设定值，否则输出Scrapy默认设定。
        scrapy settings --get BOT_NAME
    scrapy runspider <spider_file.py>
        #在未创建项目的情况下，运行一个编写在Python文件中的spider。
    scrapy version [-v]
        #输出Scrapy版本
    scrapy bench

#scrapy选择器的用法
    #css、xpath、re
    使用选择器(selectors)
    >>> response.xpath('//base/@href').extract()
    [u'http://example.com/']
    >>> response.css('base::attr(href)').extract()
    [u'http://example.com/']
    >>> response.xpath('//a[contains(@href, "image")]/@href').extract()
    [u'image1.html',
     u'image2.html',
     u'image3.html',
     u'image4.html',
     u'image5.html']
    >>> response.css('a[href*=image]::attr(href)').extract()
    response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')

#scrapy中spider用法
    #custom_settings：覆盖setting配置信息
    #from_crawler 方法类
    #start_requests 调用start_url是的方法
    #make_requests_from_url 被默认start_requests运行时调用
    #parse 在spider中 进行解析爬取到的数据
    #log self.logger.info()
    #closed 当spider关闭时，该函数被调用。
    #scrapy crawl zhihu -a hello :定义传入参数进行调用
    
#scrapy中itemline的使用
    将item写入JSON文件：JsonWriterPipeline
    Write items to MongoDB：MongoPipeline
    去重：DuplicatesPipeline
    
#scrapy中download Middleware用法
     scrapy settings --get=DOWNLOADER_MIDDLEWARES_BASE
    
            
 