import requests

#print(requests.__version__)
 
resp = requests.get("https://github.com/JingtongYang/lab1-cmput404/edit/main/lab1_404.py")
print(resp.text)

