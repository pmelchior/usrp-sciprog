# Getting comfortable with your UNIX terminal: the Bash shell

A shell is a program that interprets and executes commands. `Bash` is a popular shell program and scripting language, and is the default for most linux and Mac operating systems. Below, we'll cover some basic commands that you'll use on a day-to-day basis, and touch on how to customize your shell to add, e.g., color, custom commands (aliases), and to remotely connect to other machines (via ssh).

Most shell programs can be run interactively, or via scripts that contain sequential commands. Below, we'll mostly work interactively. Note that this is really just a cursory introduction to working with the `Bash` shell! I highly recommend reading through a tutorial, [like this one](http://cs.lmu.edu/~ray/notes/bash/) to see all of the cool things you can do with a shell.

Let's now all start up a terminal. On a Mac, you can use the pre-installed Terminal application or download and install a third-party terminal software like [iterm2](https://www.iterm2.com/). On Linux, open the default Terminal application. On Windows, we'll be working with the Ubuntu subsystem, so open up the terminal / Ubuntu program you installed.

You should now have a terminal open and see the blinking cursor eagerly awaiting input.


## Basic commands

When you first open a shell, you will be in some default path. Usually this is your home folder / directory. To check what path you are in, also known as the current or present working directory, use the `pwd` command. In your shell, type this command and hit enter - you should see something like the below (it may start with /home/... instead):

    $ pwd
    /Users/adrian

To find out what files and folders are in your current directory, use the `ls` command - you should see a bunch of names print out:

    $ ls
    Applications  
    Desktop      
    Documents    
    Downloads    
    Dropbox      
    ...etc...

We can also list the contents of any other directory on your machine by specifying a path after the command. For example, to see what is in your Documents folder (you might not have one), you can do:

    $ ls Documents
    master.tar.gz  photo.jpg      sample_cmd.png
    ...etc...

Let's say I have many image files in there, and I want to know what PNG images are in my documents path. I can list sub-selections of files using a "wildcard" operator, the * symbol. This symbol basically means "match anything in replace of the *". For example, I could find all .png files by doing:

    $ ls Documents/*.png
    Documents/sample_cmd.png

Notice I had to type the name of the Documents folder each time because that is a subdirectory within the path that I am currently in (/Users/adrian). In any shell, you can also move your current working directory using the `cd` (change directory) command. For example, I can move into the Documents folder:

    $ cd Documents
    $ pwd
    /Users/adrian/Documents
    $ ls *.png
    Documents/sample_cmd.png

You don't always have to type the full name of a directory to go to it. Now that we're in the Documents folder, if I want to go back up to my home directory, I can type either:

    $ cd ..
    $ pwd
    /Users/adrian

The `..` is shorthand for "the directory above my current one". You can string these together to go up several directories. For example, we'll go back down in to my Documents folder, then go all the way up to the /Users/ folder:

    $ cd Documents
    $ cd ../../
    $ pwd
    /Users

Another good shorthand to know is the short name for "home directory": `~/`

    $ cd ~/
    $ pwd
    /Users/adrian

The most common commands I use in a shell are:

* `ls` - to list the contents of a directory
* `cd` - to change the current working directory
* `cp` - to copy a file or directory
* `mv` - to move a file or directory (_be careful with this one_)
* `rm` - to delete a file or directory (_be careful with this one_)
* `man` - to display the manual (help) for a command or program
* `wc` - word count or line count (with the `-l` flag)
* `less` - show part of a text file
* `cat` - dump the contents of a file
* `touch` - create an empty file with the specified name

Most of the above commands are not actually part of `bash`, but are programs that can be run from within a `bash` shell. So how does `bash` know about these scripts?


## Environment variables

All shells allow setting variables that store values. There are also a number of special variable names that control aspects of the shell. To set an environment variable, you just have to set some value to a name with the = operator:

    $ myvariable=14

We can dump the contents of this variable with the `echo` command:

    $ echo $myvariable
    14

Note that when I want to work with an env variable (after setting), the name is prefaced with a dollar sign!

So how does your `bash` shell know about all of those scripts (like `cat`) that aren't part of the `bash` shell? Well, there is a special environment variable called `$PATH`, and this tells your shell where to look for program names when you type something in the terminal prompt. Dump the contents of this variable:

    $ echo $PATH
    .../usr/local/bin:/usr/bin:/bin...

It should contain a bunch of things that contain `/bin` paths. List the contents of one of those, like `/bin`:

    $ ls /bin
    [          chmod      date       domainname expr       ksh        ln         mv         pwd        sh         sync       unlink
bash       cp         dd         echo       hostname   launchctl  ls         pax        rm         sleep      tcsh       wait4path
cat        csh        df         ed         kill       link       mkdir      ps         rmdir      stty       test       zsh

Aha! So all of those commands we were playing with above are just executable programs that like in a path that `Bash` knows about. You can add other paths to your `$PATH` variable to make `Bash` aware of other program locations. __But beware__: if you accidentally delete the contents of the variable, it can be a huge pain to fix!


## Startup and configuration files

...


## Text editors (for making quick changes)

I use a graphical text editor ([Atom](https://atom.io/)) that has a bunch of nifty, customizable features. Many people instead swear by using shell-based text editors, like `emacs` or `vim`. I don't care what you use, but it's important that you learn the basics in at least one of the shell-based text editors, at least for making quick edits or edits on remote machines. Your options are (to name a few):

* `emacs`
* `vim`
* `nano`

If you go with `emacs` (that's what I use occasionally), the most important things to know are how to save, and how to quit. To open `emacs`, type the command name with a filename. For example, to edit a file "test.txt" in the current directory:

    $ cd ~/
    $ emacs test.txt

Type some words in there. Then, to save, do:

    ctrl + x, s

In the above, hold ctrl and hit x, then hit s.

To quit `emacs`, the command sequence is:

    ctrl + x, c


## SSH and remote login

Make an SSH key:
https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-linux
