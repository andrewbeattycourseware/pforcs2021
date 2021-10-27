import requests
import json

from requests.api import get
# this program falls into rate limit issues 
# because I am not identifiying myself though authentication


base = "https://api.github.com"
user = 'andrewbeattycourseware'

def getJSONFromUrl(url):
    response = requests.get(url)
    data = response.json()
    return data

# this is mainly used for dubugging
def write_to_file(data):
    filename = 'githubusers.json'
    if filename:
        # Writing JSON data
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

def scan_dir (dir_base, dirname):
    url = dir_base + '/' + dirname
    data = getJSONFromUrl(url)
    for content in data:
        print (type(content))
        if content['type'] == 'dir':
            scan_dir(url, content['name'])
        elif content['type'] == 'file':
            filename = content['name']
            sha = content['sha']
            print(filename)


def scan_repo(reponame):
    url = base + "/repos/"+user+"/"+reponame+'/'+'contents'
    scan_dir(url,'')

#url = "https://api.github.com/users?since=100"
reposurl = base+"/users/"+user+"/repos"

data = getJSONFromUrl(reposurl)
print (data)
#Get the file name for the new file to write

repositoryNames = []
for repo in data:
    repositoryNames.append(repo['name'])

reponame = 'dataRepresenation2020'
scan_repo(reponame)

#print (repr(repositoryNames))
