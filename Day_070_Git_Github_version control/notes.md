# Notes of Git and GitHub Version Control cmd


**1- repos**: My alias for the repositories folder.

**2- mkdir python**: Create a new directory named "python".

**3- cd python**: Change the current working directory to the "python" directory

**4- ls**: List the contents of the current directory.

**5- touch notes.txt**: Create a new file named "notes.txt".

**6- nano notes.txt**: Open the "notes.txt" file in a text editor I'm using (nano) you can use different editor depending on your OS.

**7- exit**: Write something then exit the text editor.

**8- git init**: Initialize a new Git repository in the current directory.

**9- ls -a**: List the contents of the current directory with hidden files.

**10- git status**: Show the status of the Git repository.

**11- git add notes.txt**: Add the "notes.txt" file to the Git staging area.

**12- git commit -m "Initial commit of notes.txt"**: Commit the changes to the Git repository with a commit message. (ps: It's good practice to write the commit in present tense and use a descriptive message.)

**13- git log**: Show the commit history of the Git repository.

**14- touch notes2.txt**: Create a new file named "notes2.txt".

**15- nano notes2.txt**: Open the "notes2.txt" file in a text editor.

**16- exit**: Write something then exit the text editor.

**17- touch notes3.txt**: Create a new file named "notes2.txt".

**18- nano notes3.txt**: Open the "notes3.txt" file in a text editor.

**19- exit**: Write something then exit the text editor.

**20- git add .**: Add all the files in the current directory to the Git staging area.

**21- git status**: Show the status of the Git repository.

**22- git commit -m "Initial commit of notes2.txt and notes3.txt"**: Commit the changes to the Git repository with a commit message.

**23- git log**: Show the commit history of the Git repository.

**24- nano notes3.txt**: Open the "notes3.txt" file in a text editor change its content and save it.

**25- git diff notes3.txt**: Show the changes made to the "notes3.txt" file since the last commit.

**26- git checkout notes3.txt**: Switch back to the "notes3.txt" file from the staging area.

---

## Now let's connect this with remote reposotry.

**27- git remote add origin https://github.com/yourusername/your-repo.git**: Add the remote repository URL to the local Git repository.

**28- git push -u origin main**: Push the changes to the remote repository.

---

## Important commands to manage files in Git.

**29- git rm --cached -r .**: Remove all files from the staging area.

**30- touch .gitignore**: Create a new file named ".gitignore".

**31- nano .gitignore**: Open the ".gitignore" file in a text editor and add the name of the files you want to avoid uploading to the remote repository.
