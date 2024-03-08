# Git tutorial

* Updated 3/4/24 for Clemson University tutorial

* Files and scripts for git tutorial (UNTHSC)

## What is Git and GitHub?

Git is a version control system that tracks the history of changes made to files (usually plain text files) as people or teams collaborate on projects together. That means that as you are woking on a project you can look into the history to determine: (1) what changes were made, (2) who made the changes, (3) when were the changes made and (4) why were the changes needed?

Most importantly, git gives you access to all versions of files in a project and any earlier version of the project can be recovered at any time (so if you mess up, you can revert to earlier versions!)

Git projects are organized into repositories which encompass the entire collection of files and folders associated with a project, along with each file's revision history. The file history appears as snapshots in time called commits. Repositories are self-contained units and anyone who has a copy of the repository can access the entire codebase and it's history.

GitHub is an online portal that hosts github repositories and provides tools for developers to interact and collaborate with open source software projects. 

There are just a few basic git commands that you will need to know to run git and upload files and projects to github. These basic commands are used to copy, create, change, and combine code and can be executed directly from the command line or using an application like GitHub Desktop. The most commonly used git commands include:

* ```git init``` initializes a brand new git repository and begins tracking an existing directory. It adds a hidden subfolder within the existing directory that houses the internal data structure required for version control.
* ```git clone``` creates a local copy of a project that already exists remotely. The clone includes all the project's files, history, and branches.
* ```git add``` stages a change. Git tracks changes to a developer's codebase, but it's necessary to stage and take a snapshot of the changes to include them in the project's history. This command performs staging, the first part of that two-step process. Any changes that are staged will become a part of the next snapshot and a part of the project's history. Staging and committing separately gives developers complete control over the history of their project without changing how they code and work.
* ```git commit``` saves the snapshot to the project history and completes the change-tracking process. In short, a commit functions like taking a photo. Anything that's been staged with ```git add``` will become a part of the snapshot with ```git commit```
* ```git status``` shows the status of changes as untracked, modified, or staged.
* ```git pull``` updates the local line of development with updates from its remote counterpart. Developers use this command if a teammate has made commits to a branch on a remote, and they would like to reflect those changes in their local environment.
* ```git push``` updates the remote repository with any commits made locally to a branch.

There are many more git commands and other fancier ways to use git/github. See the [full reference guide to git commands](https://git-scm.com/docs).

## Start using git

if you have not used git previously you should set up git to start working with it 

```
# set your user name
git config --global user.name "example_name"

# set your email
git config --global user.email example_email@replace.com

# set default text editor
# this editor will appear by default when you commit to a change if you dont add a short message for the commit
git config --global core.editor "nano -cw" 

#additional configs 
#for windows user if reading newlines from linux/mac
git config --global core.autocrlf true

```


## Let's try some simple git functions

Open a terminal and clone this tutorial on to your laptop

```bash
git clone https://github.com/aemann01/git_tutorial && cd git_tutorial
# what do we have in this repo?
ls # lists files and folders
ls -a # here we can see the hidden git specific folders .git is where your file history is tracked
```

Make a copy of this repo and then add to your github account 

```bash
cd .. 
mkdir testrepo
cd testrepo
cp ../git_tutorial/* .
```

Make an online repository through the github website called "testrepo", then add your files from the command line with git init

```bash
echo "# testrepo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/<your account>/testrepo.git
git push -u origin master
```

Note: now github uses main instead of master you might need to change the name of the initial branch in your local repo.

```
#code to rename the current branch
git branch -m main 

#optinal you can set up your local git to start repositories as main instead of master 
git config --global init.defaultbranch main

```

Now refresh your github repository page for testrepo -- you should see your readme file but no others!

Check the status of the repository 

```bash
git status
```
First let's tell git that we want it to track our python script

```bash
git add count_bases.py && git commit -m "my first commit :)"
# and push our changes to github
git push
```

But say we don't want it to track any files that end with fa (i.e., fasta files)

```bash
touch .gitignore && echo "*fa" >> .gitignore
# see what we added to the file
cat .gitignore
git add .gitignore
git commit -m "adding gitignore file"
git status # you should no longer see the fasta file but it still exists in the repository!
```

Let's add a new file to the repo, check status again

```bash
touch newfile.txt && echo "hello world\!" >> newfile.txt
git status
```

Add your new file to the files to be tracked, then commit your changes

```bash
git add newfile.txt
git status
#commit your changes -- these should be informative but short, remember these are notes to yourself in case something goes funky down the road
git commit -m "adding some new files"
```

Once you are ready satified with the files, you can push it to your github repository

```bash
git push
```

Again, check your online repository -- you should now see your files uploaded and your commit message  

Let's try a more complex example. Say we have a python script called count_bases.py that is written in python3 syntax. The script takes a fasta file and will output the base composition of each read.

Run the script

```bash
python3 count_bases.py iodamoeba_rep.fa
```

Now let's mess up the script 

```bash
sed -i 's/print(/print /g' count_bases.py 
```

If we rerun the command we'll get a syntax error but let's pretend that it's been a long night and you just want to push your changes to gihub and call it a day without testing to see if your changes didn't work (hey, we've all been there)

Check git status, add your messed up python script, commit and push to github

```bash
git status
git add count_bases.py && git commit -m "I'm so tired" && git push
```

You get a good night sleep and your favorite caffinated drink the next morning and you come into work refreshed and ready to start where you picked back up and then...

```bash
#test out our script again
python3 count_bases.py iodamoeba_rep.fa
```

Uh oh :fearful:. You have no idea what changes you made and this is going to set you back weeks!! But then you remember you use git and can revert to before you made the error!

```bash
# whoops now our script doesn't work! revert to your previous commit
# what commit do we want to revert to?
git log
```

Your log keeps a list of all of the commits you have made -- to revert to an older commit (before you messed up the file)

```bash
git reset --hard <hash-or-ref>
git push -f origin
```

Note: this will remove the last commit that you made so be sure you want to completely hard revert!

Say you made many changes during your last commit that only messed up some of your files or you want to play around with your code without damaging the main branch of your git repository. In this case you can create a new branch to run all of your tests without affecting the main branch.

```bash
# create a new branch called whoops
git checkout -b whoops
git push --set-upstream origin whoops
# add a shebang to our python script
sed -i '1 i\#!/usr/bin/python3\n' count_bases.py
# 
git add count_bases.py&& git commit -m "adding shebang to python script"
git push
```

If you want to merge your branches first move back to your master branch

```bash
git checkout master
# and merge
git merge whoops
git push
```

Now the changes you made to the whoops branch are incorporated into your master branch!

