# Day 1 (Tuesday, June 7)

Everyone should be able to do the following by the end of the day:

1. Choose a department computer for the summer, and log on to it. 

2. Do the following from from a terminal (on both laptop and desktop, if, e.g., you are running Windows):
	a. Create a new directory
	b. Navigate between directories
	c. List the contents of a directory
	d. List all the contents of a directory matching a given pattern (e.g., all files with names ending with '.py')
	e. Create a blank file with a given name.
	f. Open a '.py' file with your favorite text editor supporting syntax highlighting/formatting (e.g., vi, emacs, SublimeText, etc.)
	g. Delete a file
	h. Delete a directory and all its contents (Be careful with this one!)	
	i. Rename a file/directory
	j. Use `ssh` to log on to your department computer from your laptop.  This will require [setting up an "ssh key"](http://www.astro.princeton.edu/docs/SSH#Keys).
	k. Use `scp` to do both of the following:
		* transfer a single file between your laptop and your department computer.
		* transfer an entire directory & its contents between your laptop and your department computer.
	l. Understand the concept of "environment variables" and how to set them, both temporarily and permanently.  Especially understand what the `PATH` variable represents. 
	
3. Be comfortable with the following basic git/Github skills (we will practice these together with the "team bio" exercise):
	a. Understand what the terms 'repository', 'clone', 'fork', 'commit', 'push', 'pull', 'merge' mean
	b. Create a new repository on Github
	c. Fork someone else's repository from Github
	d. Clone an existing repository to your local computer.
	e. Add new files to a repository
	f. Change existing files, commit those changes locally, and push those changes to Github.
	g. Pull changes that other people have made onto your local repository.

4. Install [Anaconda](https://www.continuum.io/downloads) on both your personal computer and your department computer.

5. Print "Hello World!" from all of the following:
	a. `python` command line
	b. `ipython` command line
	c. a `jupyter` python notebook
	d. executing a `hello.py` script from the command line.

6. 	Use a combination of `ssh` and VNC to "remote desktop" into your department computer.  This requires the following steps:
	a. Go to System->Preferences->Remote Desktop on your desktop, make sure "allow other uses to view" and "allow other users to control" are checked, and then "require the user to enter this password" is also checked (use a password different from your astro department login).  Also make sure "You must confirm each access" is *not* checked.
	b. From a terminal on your laptop, run `ssh -L 5901:localhost:5900 user@computer.astro.princeton.edu`.  If you've ssh'd successfully before, this should work.
	c. From your laptop, use a VNC program to connect to `vnc://localhost:5901`.  If you have a Mac, the easiest way to do this is to click on the desktop (so 'Finder' is active), press Apple+k, and then enter `vnc://localhost:5901` as the server address.
	