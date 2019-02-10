import sqlite3
from github import Github
import schedule
import time

conn = sqlite3.connect('../web.db')
print("Opened database")

git = Github("fb3025d2855730d6b8d29ff75d0dbefa35f0d99c")
Repos = []

def job():
    cursor = conn.cursor()

    ##Gets repos for the user and replaces empty description with "TODO"
    for repo in git.get_user().get_repos():
        if repo.description == None:
            Repo_Info = [repo.name, "TODO", repo.html_url, str(repo.forks_count), str(repo.stargazers_count)]
        else:
            Repo_Info = [repo.name, repo.description, repo.html_url, str(repo.forks_count), str(repo.stargazers_count)]
        Repos.append(Repo_Info)

    ##TODO look for deleted and new repos to delete/add to the database 
    ##Updates repos data
    for repo in Repos:
        params = (repo[1], repo[2], repo[3], repo[4], repo[0])
        cursor.execute("UPDATE GITHUB set DESCRIPTION = ?, LINK = ?, FORKS = ?, STARS = ? where NAME = ?", params)
        
    print("Updated !")
    conn.commit()

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
