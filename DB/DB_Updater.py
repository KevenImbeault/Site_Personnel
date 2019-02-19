import sqlite3
from github import Github
import schedule
import time

conn = sqlite3.connect('web.db')
print("Script started !")

f = open('Github_Key.txt', 'r')

#TODO Encrypt this key
git = Github(f.readline())


def job():
    #Initialisation of various variables.
    Repos = []
    Repos_Names = []
    names = []

    cursor = conn.cursor()

    #Gets public repos of the user and replaces empty descriptions with "TODO".
    for repo in git.get_user().get_repos():
        print(repo.language)
        if repo.description == None:
            Repo_Info = [repo.name, "TODO", repo.html_url, str(repo.forks_count), str(repo.stargazers_count), repo.updated_at.strftime('%Y-%m-%d'), repo.language]
        else:
            Repo_Info = [repo.name, repo.description, repo.html_url, str(repo.forks_count), str(repo.stargazers_count), repo.updated_at.strftime('%Y-%m-%d'), repo.language]
        Repos.append(Repo_Info)

    for repo in Repos:
        
        Repos_Names.append(repo[0])
        cursor.execute("SELECT count(*) FROM GITHUB WHERE NAME = ?", (repo[0],))
        data=cursor.fetchone()[0]
        #If the repo isn't in the GITHUB table, insert it.
        if data==0:
            params = (repo[0], repo[1], repo[2], repo[3], repo[4], repo[5], repo[6])
            cursor.execute("INSERT INTO GITHUB (NAME, DESCRIPTION, LINK, FORKS, STARS, UPDATED_AT, LANGUAGE) VALUES (?, ?, ?, ?, ?, ?, ?)", params)
            print("Created an entry for the repo : " + repo[0])
        #If the repo is already in the GITHUB table, update it.
        else:
            params = (repo[1], repo[2], repo[3], repo[4], repo[5], repo[6], repo[0])
            cursor.execute("UPDATE GITHUB set DESCRIPTION = ?, LINK = ?, FORKS = ?, STARS = ?, UPDATED_AT = ?, LANGUAGE = ? WHERE NAME = ?", params)
            print("Updated the entry for the repo : " + repo[0])

    #Get the names of the repos inside the GITHUB table and puts them in a list .   
    query = cursor.execute('SELECT NAME FROM GITHUB')
    rows = query.fetchall()
    for row in rows:
        names.append(row[0])

    #Check if any of the repos in the databse are deleted/privated...
    for name in names:
        #...if there is, remove it from the database.
        if name not in Repos_Names:
            cursor.execute("DELETE FROM GITHUB WHERE NAME=?", (name,))
            print('Repo ' + name + ' deleted')

    conn.commit()   
    print("Done !")    
    
    
#Do the function job every hour.
schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
