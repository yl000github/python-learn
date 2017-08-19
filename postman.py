import requests

url = "http://img.mmjpg.com/2015/70/4.jpg"

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'accept': "image/webp,image/apng,image/*,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'Connection': "keep-alive",
    'Referer': "http://www.mmjpg.com/mm/70"
}
# headers = {
    # 'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    # 'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # 'accept-encoding': "gzip, deflate",
    # 'accept-language': "zh-CN,zh;q=0.8",
    # 'cache-control': "no-cache",
    # 'postman-token': "24760965-cce4-e3b4-1e93-ad8c7dfaf5c3"
    # }
img = requests.request("GET", url, headers=headers)
# img = requests.get(pic_src, headers=headers, timeout=10)
imgname = "f:/pic_cnt_{}.jpg".format( 1)
with open(imgname, 'wb+') as f:
	f.write(img.content)
	print(imgname)
# print(response.text)


# GET /2015/7/1.jpg HTTP/1.1
# Host: img.mmjpg.com
# Connection: keep-alive
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
# Accept: image/webp,image/apng,image/*,*/*;q=0.8
# Referer: http://www.mmjpg.com/mm/7
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.8