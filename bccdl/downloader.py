import json
import os
from bccdl.subtitle import bcc2ass
from bccdl.utils import safe_httpget

def download_video(bvid, out_path):
	url = f'https://api.bilibili.com/x/player/pagelist?bvid={bvid}'
	r = safe_httpget(url)
	ps = [(p['cid'], p['part']) for p in json.loads(r)['data']]
	n = len(ps)
	for i, (cid, name) in enumerate(ps):
		url = f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}&cid={cid}'
		r = safe_httpget(url)
		subtitle = json.loads(r)['data']['subtitle']['list']
		if len(subtitle) > 0:
			url = subtitle[0]['subtitle_url']
			bcc = safe_httpget(url)
			print (f'Downloading {i+1}/{n}: {name}')
			bcc2ass(bcc, os.path.join(out_path, name + '.ass'))

def download_bangumi(ssid, out_path):
	url = f'https://api.bilibili.com/pgc/view/web/season?season_id={ssid}'
	r = safe_httpget(url)
	ps = [(p['aid'], p['cid'], p['long_title']) for p in json.loads(r)['result']['episodes']]
	n = len(ps)
	for i, (aid, cid, name) in enumerate(ps):
		url = f'https://api.bilibili.com/x/player/wbi/v2?aid={aid}&cid={cid}'
		r = safe_httpget(url)
		subtitle = json.loads(r)['data']['subtitle']['subtitles']
		if len(subtitle) > 0:
			url = subtitle[0]['subtitle_url']
			bcc = safe_httpget('https:'+url)
			print(f'Downloading {i+1}/{n}: {name}')
			bcc2ass(bcc, os.path.join(out_path, name + '.ass'))

