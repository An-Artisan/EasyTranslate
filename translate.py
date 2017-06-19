import urllib.request
import urllib.parse
import json
import easygui as g
# response = urllib.request.urlopen("http://imgsrc.baidu.com/imgad/pic/item/5fdf8db1cb1349547059c0755c4e9258d1094a5f.jpg")
# img = response.read()
# with open('img.jpg','wb') as f:
#     f.write(img)
content = g.enterbox("请输入你要翻译的内容")
# 定义百度翻译链接
url = "http://fanyi.baidu.com/v2transapi"
# 伪造formData数据
data = {}
data["from"] = "zh"
data["to"] = "en"
data["query"] = content
data["transtype"] = "translang"
data["simple_means_flag"] = "3"
# 设置编码utf-8，以免出错
data = urllib.parse.urlencode(data).encode("utf-8")
# 发起请求，第二个参数有时，代表是POST提交
response = urllib.request.urlopen(url,data)
# 获取数据，解码utf-8
html = response.read().decode("utf-8")
# json解码
html = json.loads(html)
# 获取翻译内容
tr_content = html['trans_result']['data'][0]['dst']
# 写入GUI界面
g.textbox(content + "的英语翻译为：",text= tr_content)