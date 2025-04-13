import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://docs.python.org')
htmlSource = r.data