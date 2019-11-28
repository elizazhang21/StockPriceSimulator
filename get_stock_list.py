import bs4 as bs
import requests
import pickle


def GetHuStock():
	res = requests.get('https://www.banban.cn/gupiao/list_sh.html')
	# 防止中文乱码
	res.encoding = res.apparent_encoding
	# 使用bsoup的lxml样式
	soup = bs.BeautifulSoup(res.text, 'lxml')
	 # 从html内容中找到类名为'u-postcontent cz'的div标签
	content = soup.find('div', {'class': 'u-postcontent cz'})
	result = []
	for item in content.findAll('a'):
		result.append(item.text)
	with open('huStock.pickle', 'wb') as f:
		pickle.dump(result, f)
