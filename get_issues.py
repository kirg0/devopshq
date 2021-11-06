import requests
import os
from pprint import pprint
import json

'''Закоментированные строки позволяют авторизироватся на GitHub, необходимо получить и добавить token. Иначе количество обращений ограничено'''

'''token = '''''
org = "devopshq"
repo = ''
get_repo_query_url = f"https://api.github.com/orgs/{org}/repos"
params = {
    "state": "all",
}
i=0
'''headers = {'Authorization': f'token {token}'}'''
try:
    '''r = requests.get(get_repo_query_url, headers=headers)'''
    r = requests.get(get_repo_query_url)
    output = r.json()
    while i < len(output):
        repo = output[i]['name']
        print(repo)
        get_issues_query_url = f"https://api.github.com/repos/{org}/{repo}/issues"
        '''rq = requests.get(get_issues_query_url, headers=headers, params=params)'''
        rq = requests.get(get_issues_query_url, params=params)
        out = len(rq.json())
        print('#'+str(len(rq.json())))
        print()
        i+=1
except Exception:
    print('Ошибка подключения к репозиторию')