#!/etc/home/Application_Main/env/bin/python3
import requests as r

if __name__ == '__main__':
    response = r.get('https://urfu.ru')
    print(response.headers)
