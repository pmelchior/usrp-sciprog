Git Excercises
==============

After going through this mini tutorial, definitely take some time to read [this](http://www.sbf5.com/~cduan/technical/git/).  It's a great and thorough explanation of how git actually works.

Initial Exploration
-------------------

1. If you don't already, create an account on github.com

2. Make a repository on GitHub for your research this summer.  Give it a useful name, related to the science (e.g., not usrp-2015).  

3. Clone this repository onto your computer (suggestion, make a 'respositories' directory under your home directory and clone it there):

   		$ cd
    		$ mkdir repositories
    		$ cd repositories
    		$ git clone  https://github.com/username/reponame.git  (or git clone git@github.com:username/reponame)

4. Edit the readme file on your laptop to include a sentence or two describing your project.

5. Commit these changes and push them back to GitHub:

   	$ git commit -am 'descriptive but concise message'
   	$ git push
	
6. Now, open another terminal, ssh into your department computer and repeat steps 2-4 (making some additional changes to the readme file this time).  

7. Back on your laptop, pull these new changes
 
   	$ git pull 
   	
   And that's how to 'sync' a repository between computers. Note: you can also edit files/commit changes directly on GitHub.  

8. Now, create a new file (maybe called notes.txt or something) and put in some content.  To have git recognize and track this new file, you first have to add it to the repository; after which you can commit the changes.

   	$ git add notes.txt
   	$ git commit -am 'added notes file' 

To summarize, this is what a typical simple workflow should look like:

		<sit down at computer>
		$ cd /path/to/my/project/dir
		$ git pull
		<edit and/or add some files>
		$ git commit -am 'briefly describe changes'
		<edit some more>
		$ git commit -am 'more changes'
		<when you're ready to stand up from computer>
		$ git push

**One more note-- whenever you rename or remove files that are being tracked by git, use the 'git rm' or 'git mv' commands rather than just 'rm' or 'mv'.  That way git won't get confused. 
​	
Branching
------------

One of the biggest advantages of git is that it allows you to experiment without worrying about breaking your code.  Usually by default you will be working on a branch called 'master', which you can confirm with the 'git branch' command:

	$ git branch
	* master

To switch branches, use 'git checkout <newbranch>', with a '-b' flag if the branch does not exist yet and you wish to create it:

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

3. Switch back to 'master' branch and convince yourself that test.txt is no longer there.

4. Now imagine you are satisfied with the changes you made on the test branch, and have convinced yourself that those changes haven't broken your project, you can merge those changes into the master branch:

   $ git merge test

5. Now, convince yourself that test.txt is there.

6. OK, now since this file is actually junk, let's now get rid of it, as well as deleting our test branch (let's not let our repository get too cluttered):

   $ git rm test.txt
   	$ git branch -d test 
   	$ git branch
   	* master

Collaborating: Forking & submitting a pull request
---------------

You may find yourself in a position where you want to contribute to a GitHub repository that is not yours.  In this case, you can't just clone -> make changes -> push, because you will not have push access to the repository (that is, unless you've been explicitly added as a collaborator).  Instead, you have to go through a process called a "pull request," whereby you submit a branch to the repo owner, and she gets to decide whether to merge that branch in.  The process to do this is the following:

1.  Fork the repository (press the "Fork" button on GitHub), which creates for you a linked---but totally independent---copy of the entire original repository that you now own.
2. Clone **your** version of the repository onto your machine.
3. [optional, but recommended] Create a new branch (e.g., 'tdm-edits')
4. Make any desired changes on this branch.
5. Push this branch (or just the master branch with `git push` if you did not create a new branch) back to your repo:

   $ git push origin tdm-edits

6. On GitHub, create a pull request following [these instructions]( https://help.github.com/articles/creating-a-pull-request/) (or actually, there should be a helpful little "create pull request" button on your repo page after you push, to shortcut this process).
7. The owner of the repo can then review it and decide whether/when to merge it in, and can also make comments.  You can continue to push changes to this branch while the pull request is still open.

**Note:** when you have a forked repository, often the "upstream" (original) repo will be updated and you will want to incorporate those changes into your local forked copy.  This is how to do that:


	$ git remote add upstream git@github.com:timothydmorton/usrp-sciprog
	$ git fetch upstream
	$ git checkout master
	$ git merge upstream/master


