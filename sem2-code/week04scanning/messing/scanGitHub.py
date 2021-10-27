import requests
import json

from requests.api import get

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


def get_filenames_from_repo(reponame):
    url = base + "/repos/"+user+"/"+reponame+'/'+'contents'
    data= getJSONFromUrl(url)
    write_to_file(data)
    print ('done')

#url = "https://api.github.com/users?since=100"
reposurl = base+"/users/"+user+"/repos"

data = getJSONFromUrl(reposurl)
#print (data)
#Get the file name for the new file to write

repositoryNames = []
for repo in data:
    repositoryNames.append(repo['name'])

reponame = 'dataRepresenation2020'
get_filenames_from_repo(reponame)

#print (repr(repositoryNames))
