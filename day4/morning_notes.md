Some Thoughts
============


* The way we've been using git/GitHub (the pull request model) is for a particular collaboration model: one where one person/group is the owner of a project and you wish to contribute a small bit.  A more common collaboration situation might be peer collaboration---where you and a few other people all have write access to the same repository.  In this case, you probably wouldn't bother with pull requests, but rather just branch/merge/push/pull all to the same repository.
* Dealing with data on multiple computers, where you can't put the data into the repository.  **Watch out for hard-coding file paths into your code!**  There's a better way to deal with this, and that's using the concept of **environment variables**.
	
	In the shell, you can define an environment variable like this:
	
		$ export myvar=/some/value
		$ echo $myvar
		/some/value
		
	From within python, you can access the values of all the environment variables that the system had at the point where python was launched:
	
		>>> import os
		>>> os.environ
		< dictionary of all env. variables > 
		>>> os.environ['myvar']
		/some/value
		
	This allows you to define file paths in your code that will work on multiple different computers.	
		
	You can "permanently" define environment variables by adding the `export` command defining the variable to your `~/.bash_profile` file.  
	
	You can also use a command that will return some default value if a desired environment variable is not defined on the system you're on.
	
		>>> import os
		>>> os.getenv('myvar', 'the default value')
		/some/value
		>>> os.getenv('myvar2', 'a second default')
		a second default

