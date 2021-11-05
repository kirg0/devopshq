import requests
import os
from pprint import pprint
import json


token = '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'
org = "devopshq"
repo = ''
get_repo_query_url = f"https://api.github.com/orgs/{org}/repos"
params = {
    "state": "all",
}
i=0
headers = {'Authorization': f'token {token}'}
r = requests.get(get_repo_query_url, headers=headers)
output = r.json()
while i < len(output):
    repo = output[i]['name']
    print(repo)
    get_issues_query_url = f"https://api.github.com/repos/{org}/{repo}/issues"
    rq = requests.get(get_issues_query_url, headers=headers, params=params)
    out = len(rq.json())
    print('#'+str(len(rq.json())))
    print()
    i+=1