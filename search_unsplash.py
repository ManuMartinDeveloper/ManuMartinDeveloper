import urllib.request
import re

url = "https://unsplash.com/s/photos/dark-minimalist-galaxy"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = re.findall(r'https://images.unsplash.com/photo-[a-zA-Z0-9\-]+', html)
    for img in list(set(images))[:5]:
        print(img)
except Exception as e:
    print(e)
