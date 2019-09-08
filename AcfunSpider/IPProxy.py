#coding=utf-8

import requests
import json
import random

class IPProxy(object):
    @staticmethod
    def getProxy(protocol):
        r = requests.get('http://127.0.0.1:8123/%s?count=20'%protocol)
        ip_proxylist = json.loads(r.text)

        selected_proxy = random.choice(ip_proxylist)
        # print "%s_proxy:%s"%(protocol,selected_proxy)
        ip = selected_proxy[0]
        port = selected_proxy[1]
        # ip="221.7.255.168"
        # port=80
        proxy='%s://%s:%s'%(protocol,ip,port)
        return proxy

    # proxy类似 https://117.127.16.208:8080
    @staticmethod
    def deleteProxy(proxy):
        in_start = proxy.index("//")
        in1 = proxy.index(":")
        in_end = proxy.index(":",in1+1)
        ip = proxy[in_start+2:in_end]
        r = requests.get('http://127.0.0.1:8123/delete?ip=%s'%ip)
        rslt = json.loads(r.text)
        return rslt!=None and rslt[1]==1