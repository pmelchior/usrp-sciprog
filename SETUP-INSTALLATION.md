# Setup Instructions

Most of us use a python package system called `anaconda`. It has many advantages, so please use it as well even if you already have a python installation on your own machine.

*You will have access to machines in Peyton Hall, these instruction here do not apply to them, only to your own personal machine.*


## If you use Windows on your machine

1. Please follow these instructions for installing the Windows Subsystem for Linux (WSL) - Ubuntu: https://docs.microsoft.com/en-us/windows/wsl/install-win10

2. Install Git. Open your command prompt, type "bash" to start a bash shell. Then run the following commands:
    ```
    sudo apt update
    sudo apt install git
    sudo apt install wget
    ```
    
    (you may need to type your computer login password)
    
3. Install Anaconda for Linux with Python 3.8 (note: *not* Anaconda for Windows!). To do this, in your command prompt, again make sure you are in the bash shell (if you still have the window open from the last step, use that, or type "bash" in a new command prompt). Then run:
    ```
    wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
    ```
    
    To execute the script, type:
    ```
    ./Anaconda3-2021.05-Linux-x86_64.sh
    ```
    
    If it doesn't execute, you need to change the access permissions and make it executable (we will learn what this means during [day1](https://github.com/pmelchior/usrp-sciprog/blob/master/day1/1-terminal-and-cmd-line.md#aparte):
    ```
    chmod 755 Anaconda3-2021.05-Linux-x86_64.sh
    ```
    
4. To access the content of your Linux distribution from your windows interface you should follow the steps described on [this website](https://www.howtogeek.com/261383/how-to-access-your-ubuntu-bash-files-in-windows-and-your-windows-system-drive-in-bash/). The summary is as follows:

    Go to your home directory (e.g. `C:\Users\remyj`) on windows with your usual graphical interface. Among the tabs on the top right click `View` and tick the `Hidden items`  box, then open `AppData\Local\Packages`

    In there you should find a file with a barbaric name like `CanonicalGroupLimited.Ubuntuxxxxxxxxx` or search for something that has the name of your distribution in it. Personally I ordered files by date and found the file corresponding to the date I installed the distro.

    Once in there go to `LocalState\rootsf\home`  and you should see your home directory.

    To do the converse operation and see your windows files from you Ubuntu prompt, you may do so by typing in your Unix prompt:
        ```
        cd /mnt/c/Users/remy
        ```

## If you use Linux on your machine

Install Anaconda for Linux with Python 3.8. Open a terminal prompt, then run:
```
wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
```

## If you use Mac OSX on your machine

1. Please make sure you have the command-line tools installed. Open the Terminal program and run the following command:
    ```
    xcode-select --install
    ```

2. Install Anaconda for Mac with Python 3.8. Download [this](https://repo.anaconda.com/archive/Anaconda3-2021.05-MacOSX-x86_64.pkg) installer, then double-click to open it and follow instructions to install.


--------


Once you have completed the steps above (depending on what kind of operating system you use), if you have time and are interested, you can start taking a look at the following tutorials:

For Git / version control:
https://www.codecademy.com/courses/learn-git/lessons/git-workflow

For Python:
http://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb



## Troubleshooting

For windows users, if anacanda stops working in your Ubuntu environment, you need to load your `.bashrc` again:

  ```bash
source .bashrc
  ```

