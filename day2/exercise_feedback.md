General feedback on exercises
---------------

* Please follow the suggested directory structure for your work, so we can keep the repo organized.  Your exercises should all be in a folder called `day1/exercises/yourname/`.

* Also, please only submit one exercise per pull request.  In other words, for each exercise you work on, create a new branch and use that branch for the pull request (e.g., `day1-ex1`, `day1-ex2`, etc.).  This will (a) give you more practice with branching/pushing/pull-requesting, and (b) allow your code review (my comments) to be more atomistic rather than all-at-once.

* Make your branch names (like your Python variable names) meaningful.  i.e., don't just call a branch (`tdm`).

* Everyone should be sure that they've added the `upstream` remote to their fork of the repository.  In other words, from within your version of the `usrp-sciprog` repo, execute the following:

		$ git remote add upstream https://github.com/timothydmorton/usrp-sciprog.git
		
	View your remotes with
	
		$ git remote -v
		
	Then, whenever you want to update your fork of the repo with changes that I have made to my version, run the following.
	
		$ git fetch upstream
		$ git checkout master
		$ git merge upstream/master
		
	And then, as you wish, to push your master back to github, do the following:
	
		$ git push

* All the requested "programs" should be exectuble from the command line (both on Windows and Mac/Linux), which requires `#!/usr/bin/env python` to be the first line.

* Please follow the following style conventions in your coding:
	* All variable/function names should be meaningful, such that if someone glances quickly through your code, it's clear what each name represents.  Err on the side of using more characters (if you're getting too pedantic I'll let you know).
	* Long variable/function names should have words separated by an underscore (e.g., `max_value` rather than `maxvalue` or even `maxValue`).  General rule of thumb is that if your variable name is three syllables or longer it should have an underscore somewhere.
	* Every function should have a documentation string.  That looks like this:
			
			def square(x):
				"""
				Returns the square of a number
				"""
				return x**2
		
		At the minumum it should succinctly describe what the function does.  Ideally it should also describe exactly what is expected as input and what it returns as output or what the side effects of calling the function are. 
