import urllib.request
import re

url = "https://www.google.com/maps/place/Madeireira+S%C3%A3o+Luiz/@-29.4926384,-51.4172739,17z/data=!3m1!4b1!4m6!3m5!1s0x951c00c151a87a41:0xf48423b2ef35310!8m2!3d-29.4926431!4d-51.414699!16s%2Fg%2F11b890t71s?hl=pt-BR"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.findall(r'\"([^\"]+)\"', html)
    for m in matches:
        if "Madeireira" in m or "Madeira" in m or "R." in m or "Av." in m:
            print(m)
except Exception as e:
    print(e)
