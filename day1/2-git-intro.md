# Version control and Git

After going through this mini tutorial, you should read [this longer tutorial](http://www.sbf5.com/~cduan/technical/git/) to get a more in depth view of how git actually works.

## Keywords and quick reference

* _Repository_: The thing that keeps track of the history of your files. Think of it like an abstract representation of a "project": it contains the current versions of files, and their entire histories. When a repository exists on your computer, it is like a folder/directory. Often abbreviated as "repo."

* _Tracked files_: The files that a given repository knows to keep track of. If you have a repository on your computer, you can copy files into the directory where your repository lives, but the repository doesn't know about them until you explicitly ask it to track them.

* _Staging area_: When you add files to a repo for the first time, or when you make changes to files and want to tell the repo, you first must add them to the "staging area." It's kind of like purgatory.

* _Commit_: When your files or changes are added to a staging area, you typically then want to commit the changes to the repo. This advances the history of the repo and tracked files.

* _Clone_: An exact copy of a repository, copied from some remote location (e.g., GitHub).

* _Fork_: A copy of a repository that you have permission to edit. Nowadays, this is typically only done on GitHub to make a copy of a project that you don't have write access to.

## Initial Exploration

1. If you don't have one already, create an account on github.com

2. Make a repository on GitHub for your research this summer:
    #. Give it a useful name, related to the science you will be doing (e.g., not "usrp"; it could be something like "galaxy-clustering")
    #. Check the box __Initialize this repository with a README__
    #. Click the __Add a license__ dropdown and select "__MIT License__"

3. Clone the repository onto your computer (suggestion: make a 'repositories' or 'repos' or 'projects' directory under your home directory and clone it there):

   		$ cd
		$ mkdir repositories
		$ cd repositories
		$ git clone https://github.com/username/reponame.git (or git clone git@github.com:username/reponame)

4. Edit the readme file (`README.md`) on your laptop to include a sentence or two describing your project.
    * Use `git status` to see what files you have edited

5. Add the file to the staging area, then commit these changes and push them back to GitHub:

   		$ git add README.md
   		$ git commit -m 'descriptive but concise message'
   		$ git push

6. Use `git status` again to see that all changes have been committed

7. Now, open another terminal window, ssh into your department computer and repeat steps 3-5:
    * Clone the repository onto your department computer
    * Edit the `README.md` file to add your name and github username
    * Add and commit the changes, then push the changes up to GitHub

8. Back on your laptop, pull these new changes

   		$ git pull

   This is how to 'sync' a repository between computers.

9. Now, create a new file called `notes.txt` and add some content (type jibberish if you are feeling uninspired!).  To tell `git` to recognize and track this new file, you first have to add it to the repository; after which you can commit the changes.

   		$ git add notes.txt
   		$ git commit -m 'added notes file'
   		$ git push

To summarize, this is what a typical simple workflow should look like:

		<sit down at computer>
		$ cd /path/to/my/project/dir
		$ git pull
		<edit and/or add some files>
		$ git add <files I edited>
		$ git commit -m 'briefly describe changes'
		<edit some more>
		$ git add <files I edited>
		$ git commit -m 'more changes'
		<when you're ready to stand up from computer>
		$ git push

__One more note__: Whenever you rename or remove files that are being tracked by git, use the `git rm` or `git mv` commands rather than just `rm` or `mv`. so that git won't get confused.
​

---

## Branching

Git repositories let you keep track of entire histories of files that are tracked. You can think of each commit as an entry in the timeline of the project. But, like in quantum physics, or your favorite scifi drama, there can be more than one timeline! Git lets you maintain parallel histories for a given repository, and those histories can diverge and cross-pollinate one another (you can copy commits from history A to/from history B). In git language, these histories are called "branches."

By default, you will typically be working on a branch called 'master', which you can confirm by executing the `git branch` command:

		$ git branch
		* master

To switch between branches, you use the `git checkout <branchname>` command. In your current repo, you probably only have one branch (master). To create a new branch with a name, e.g., "test", use `checkout` with the `-b` flag:

		$ git checkout -b test
		Switched to a new branch 'test'
		$ git branch
		  master
		* test
		$ git checkout master
		$ git branch
		* master
		  test

Using branches will make more sense when you are actually working with code, but for now try the following:

1. Switch to the 'test' branch
2. Create a new file and add/commit it:

  	 $ echo 'this is a test' > test.txt
	 $ git add test.txt
	 $ git commit -am 'added test file'

3. Switch back to 'master' branch and convince yourself that test.txt is no longer there -- it only exists in the 'test' branch!

4. Now imagine you are satisfied with the changes you made on the test branch, and have convinced yourself that those changes haven't broken your project, you can merge those changes into the current branch (master):

    	$ git merge test

5. Now, convince yourself that `test.txt` exists in your master branch.

6. OK, now since this file is actually junk, let's now get rid of it, as well as deleting our test branch (let's not let our repository get too cluttered):

   	$ git rm test.txt
   	$ git branch -d test
   	$ git branch
   	* master

---

## Collaborating: Forking & pull requests

You may find yourself in a position where you want to contribute to a GitHub repository that is not yours. In this case, you can't just clone, make changes, commit, and push, because you will not have push (write) access to the repository (unless you've been explicitly added as a collaborator). Instead of directly pushing changes, you have to go through a process called a "pull request," whereby you ask the repo owner to "pull" your changes into their repo. The process to do this is the following:

1. Fork the repository (press the "Fork" button on GitHub), which creates for you a linked---but totally independent---copy of the entire original repository that you now own (still on GitHub).
2. Clone **your** version of the repository onto your machine.
3. Create a new branch (e.g., 'my-edits')
4. Make any desired changes on this branch.
5. Push this branch back to your fork of the original repo:

   	$ git push origin my-edits

6. On GitHub, create a pull request following [these instructions]( https://help.github.com/articles/creating-a-pull-request/) (or actually, there should be a helpful little "create pull request" button on your repo page after you push, to shortcut this process).
7. The owner of the repo can then review it and decide whether/when to merge it in, and can also make comments.  You can continue to push changes to this branch while the pull request is still open.

**Note:** when you have a forked repository, often the original repo will be updated and you will want to incorporate those changes into your local forked copy. To do that, you have to tell your cloned repository about the original repository, by convention called "upstream." This is how to do that:


	$ git remote add upstream git@github.com:pmelchior/usrp-sciprog
	$ git fetch upstream
	$ git checkout master
	$ git merge upstream/master
