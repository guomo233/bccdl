import requests
import time
requests.packages.urllib3.disable_warnings()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'}
def safe_httpget(url):
	r = requests.get (url, headers=headers, verify=False)
	time.sleep(1)
	return r.text