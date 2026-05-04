GitHub
- First create a Github Repo on line 
- git clone <url>
- ls -- list of directories
- cd -- Change directory

- commit: is a save-point:
Steps to publish your code on GitHub:
- git clone <url>
- git commit -m "message"
- git add <. means all or add the specify file's name >
- git status
- git push
- git commit -am "message"
- git pull -- pull the latest version of your code down from Github.

- git log
- git reset:
- git clone <url>
    - git reset --hard <commit> means the commit i want to go back to.
    - git reset --hard origin/master or origin/main -- reset all the main branch

- Git Branching:
   -git branch: reveals all the branches on github
   - git checkout -b style : create and move to the new branch named style
   - git checkout style : style branch
   - git checkout master or main : go back to the  master or the main branch.
   - git commit -am "message"


echo "# cs50-python-s-notes-" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin url
git push -u origin main