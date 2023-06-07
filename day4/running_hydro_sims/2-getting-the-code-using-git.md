# Software management: version control with `git`

Version control is a technique that allows to keep track of all the changes in a complex software or in a complex document within a large collaboration. 

In order to be able to manage your own software or documentation, you need first to open an account on one of the two popular Open Source servers [GitHub](https://github.com) or [BitBucket](https://bitbucket.org). For today, open your account on BitBucket, because we are going to use it.

Once it is done, visit the BitBucket page of the `RAMSES` code [here](https://bitbucket.org/rteyssie/ramses). 

You can see amnong other things the source code, a Wiki that contains the user's guide and an automatic test page. 

Go to your Terminal window on `adroit` and type:

 ```console
$ git clone https://bitbucket.org/rteyssie/ramses
```

This will clone the entire code repository to your account on adroit. You can look at the history of the repository using:

```console
$ git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
*   ebcb6769 2023-03-04 | Merge branch 'master' of bitbucket.org:rteyssie/ramses (HEAD -> master, origin/master, origin/HEAD) [Romain Teyssier]
|\  
| * 04ca371f 2023-03-03 | Add initial subgrid turbulence in godunov_fine [Romain Teyssier]
| * 4e520013 2023-02-22 | Add halo reader in ramses_io.py [Romain Teyssier]
| *   ed97ec75 2023-02-21 | Merge branch 'master' of bitbucket.org:rteyssie/ramses [Romain Teyssier]
| |\  
| * | 8ff8ae54 2023-02-21 | Fix 2 small bugs that made the debugger complain [Romain Teyssier]
* | | d0acc21b 2023-03-04 | Fix the Makefile and some minor modifications [Romain Teyssier]
| |/  
|/|   
* | 92b0105f 2023-02-06 | Fix issue with quad hilbert for ramses python library [Romain Teyssier]
|/  
```

You can find many resources on `git` in this list:
- https://learngitbranching.js.org/?NODEMO
- https://gitimmersion.com/
- http://think-like-a-git.net/
- http://ndpsoftware.com/git-cheatsheet.html
- https://ohshitgit.com/
- http://gitready.com/
- https://explainshell.com/

What you can do with git:
- track bugs to their authors
- edit users guides and wikis
- revert to older versions
- track the exact version of the code with the Git hash key 
- set up an automatic build and test system
- validation and verification (reproducibility)

