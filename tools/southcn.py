import requests


url = "https://msearch.southcn.com/api/v1/token"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'text/css; charset=utf-8'}

r = requests.post(url, headers, verify=False)

print(r.status_code, r.history)