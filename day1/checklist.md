# Day 1 checklist

Everyone should be able to do the following by the end of today:

1. Choose a department computer for the summer, and log on to it.

2. Do the following from from a terminal (on both laptop and desktop, if, e.g., you are running Windows):
 * Create a new directory
 * Navigate between directories
 * List the contents of a directory
 * List all the contents of a directory matching a given pattern (e.g., all files with names ending with '.py')
 * Create a blank file with a given name.
 * Open a '.py' file with your favorite text editor supporting syntax highlighting/formatting (e.g., vim, emacs, SublimeText, etc.)
 * Delete a file
 * Delete a directory and all its contents (Be careful with this one!)
 * Rename a file/directory
 * Use `ssh` to log on to your department computer from your laptop.  This will require [setting up an "ssh key"](http://www.astro.princeton.edu/docs/SSH#Keys).
 * Use `scp` to do both of the following:
  * transfer a single file between your laptop and your department computer.
  * transfer an entire directory & its contents between your laptop and your department computer.
 * Understand the concept of "environment variables" and how to set them, both temporarily and permanently.  Especially understand what the `PATH` variable represents.

3. Be comfortable with the following basic git/Github skills (we will practice these together with the "team bio" exercise):
 * Understand what the terms 'repository', 'clone', 'fork', 'commit', 'push', 'pull', 'merge' mean
 * Create a new repository on Github
 * Fork someone else's repository from Github
 * Clone an existing repository to your local computer.
 * Add new files to a repository
 * Change existing files, commit those changes locally, and push those changes to Github.
 * Pull changes that other people have made onto your local repository.

4. Install [miniconda](https://conda.io/miniconda.html) (or [anaconda](https://www.continuum.io/downloads)) on both your personal computer and your department computer.

5. Print "Hello World!" from all of the following:
 * `python` command line
 * `ipython` command line
 * a `jupyter` python notebook
 * executing a `hello.py` script from the command line.

6. Use a combination of `ssh` and VNC to "remote desktop" into your department computer.  This requires the following steps:
   * Go to System->Preferences->Remote Desktop on your desktop, make sure "allow other uses to view" and "allow other users to control" are checked, and then "require the user to enter this password" is also checked (use a password different from your astro department login).  Also make sure "You must confirm each access" is *not* checked.
   * From a terminal on your laptop, run `ssh -L 5901:localhost:5900 user@computer.astro.princeton.edu`.  If you've ssh'd successfully before, this should work.
   * From your laptop, use a VNC program to connect to `vnc://localhost:5901`.  If you have a Mac, the easiest way to do this is to click on the desktop (so 'Finder' is active), press Apple+k, and then enter `vnc://localhost:5901` as the server address.
