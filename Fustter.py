# scoop as browser to login in QUST

import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse

#disgzip
def disgzip(data):
    try:
        print("trying dis-gzip")
        data=gzip.decompress(data)
        print("Finished disgizp")
    except:
        print("no necessary to disgzip")
    return data

def getQueryStr(data):
    cer = re.compile('name="queryString" value="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': '211.87.157.37',
    'DNT': '1'
}#Chrome

url="http://211.87.157.37"
opener=getOpener(header)
op=opener.open(url)                     #interactive warns here
data=disgzip(data)
queryStr=getQueryStr(data.decode())

url+="eportal/InterFace.do?method=login"


user_id=input("please input your id:\n")
print("your id is:  "+user_id)
user_password=input("please input your password:\n")
print("your id password is:  "+user_password)

postDict={
    "userId":user_id,
    "password":user_password,
    "queryString":queryStr

    }

postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())
