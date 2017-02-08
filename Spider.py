import urllib
import urllib.request

def saveFile(data):
    save_path = "E:\\tempOut.html"
    f_obj = open(save_path, "wb")#wb means open measure,w means write and b means binary
    f_obj.write(data)
    f_obj.close()

fp = urllib.request.urlopen("https://www.douban.com").read()
mybytes = fp
mystr = mybytes.decode("UTF-8")#gb18030is china national standard,"GuojiaBiaozhun"

saveFile(mybytes)
print ("save ok")