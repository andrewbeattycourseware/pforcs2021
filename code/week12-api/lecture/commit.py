from github import Github
import requests
from conf import auth

token = auth['token']

# remove the minus sign from the key
# you can add this to your code just don't commit it
# or use an API key to your own repo
g = Github(token)

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
repo = g.get_repo("datarepresentationstudent/aPrivateOne")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)
newContents = contentOfFile + " more stuff \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
