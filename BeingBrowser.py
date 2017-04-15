#simulate as a browser to spider

import urllib.request

#main 
url = 'http://www.douban.com/'
req = urllib.request.Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})#simulate IE
oper = urllib.request.urlopen(req).read()
print('spider ok')

#save html to local
def saveFile(data):
    save_path = "E:\\tempOut.html"
    f_obj = open(save_path, "wb")#wb means open measure,w means write and b means binary
    f_obj.write(data)
    f_obj.close()

saveFile(oper)
print ("save ok")