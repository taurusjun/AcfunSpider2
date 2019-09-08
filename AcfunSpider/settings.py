# -*- coding: utf-8 -*-

# Scrapy settings for AcfunSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import logging

BOT_NAME = 'AcfunSpider'

SPIDER_MODULES = ['AcfunSpider.spiders']
NEWSPIDER_MODULE = 'AcfunSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AcfunSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
   'Accept-Language': "zh-CN,zh;q=0.9",
   "Accept-Encoding": "gzip, deflate",
   "Connection": "keep-alive",
   "Referer": "https://www.acfun.cn/v/list63/index.htm",
   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
   "Origin": "https://www.acfun.cn",
   'Upgrade-Insecure-Requests': '1',
   'Content-Type': 'application/x-www-form-urlencoded'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'AcfunSpider.middlewares.AcfunspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'AcfunSpider.middlewares.MyRetryMiddleware': 200,
   'AcfunSpider.middlewares.MyProxyMiddleware': 201,
   'scrapy.downloadermiddlewares.retry.RetryMiddleware':None
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'AcfunSpider.pipelines.AcfunspiderPipeline': 300,
   'AcfunSpider.pipelines.CachePipeline': 300,
   'AcfunSpider.pipelines.DBPipeline': 400,
   'AcfunSpider.pipelines.MyImagesPipeline': 500
}

IMAGES_STORE='/tmp/img'

IMAGES_URLS_FIELD='userImg'

IMAGES_RESULT_FIELD='localImgPath'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DATABASE = {'drivername': 'mysql',
            'host': 'localhost',
            'port': '3306',
            'username': 'root',
            'password': 'r123456',
            'database': 'actest2',
            'query': {'charset': 'utf8mb4'}
            }

LOG_ENABLED = True
LOG_ENCODING = "utf-8"
LOG_LEVEL = logging.INFO
LOG_FILE = "Spider.log"
# LOG_STDOUT = True # 这一句在scrapyd-deploy的时候必须注释掉
# LOG_FORMATTER = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
LOG_FORMATTER = 'AcfunSpider.PoliteLogFormatter.PoliteLogFormatter'
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"

###### 防止爬虫被ban ######
# 绕过robots策略
ROBOTSTXT_OBEY = False
# # 禁用Cookie
# COOKIES_ENABLED = False
# # 限制爬取速度
# DOWNLOAD_DELAY = 5
# # 禁止重定向
# REDIRECT_ENABLED = False
# # 全局并发数
# CONCURRENT_REQUESTS = 500
# # 禁止重试
# RETRY_ENABLED = False
# # 减小下载超时
# DOWNLOAD_TIMEOUT = 15

####测试模式，不读写数据库#####
TEST_MODE = False
