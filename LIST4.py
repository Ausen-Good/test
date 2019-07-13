import urllib.request
import re
import urllib.error
import requests


url = "https://blog.csdn.net/"
# 模拟浏览器
headers = ("User-Agent", "Mozilla/5.0 (Wind ows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read().decode('utf-8')
pat = '<div class="img_box"><a href="(.*?)"'
allurl = re.compile(pat).findall(data)
print(allurl)
exit()
try:
    for i in range(0, len(allurl)):
        filename = "D:/ceshi/"+str(i)+".html"
        urllib.request.urlretrieve(allurl[i], filename)

except urllib.error.URLError as ur:
    if hasattr(ur, "code"):
        print(ur.code)
    if hasattr(ur, "reason"):
        print(ur.reason)


