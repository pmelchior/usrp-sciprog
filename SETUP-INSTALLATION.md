# Setup Instructions

Most of us use a python package system called `anaconda`. It has many advantages, so please use it as well even if yo already have a python installation on your machine.


## If you use Windows on your laptop:

1. Please follow these instructions for installing the Windows Subsystem for Linux (WSL) - Ubuntu: https://docs.microsoft.com/en-us/windows/wsl/install-win10

2. Install Git. Open your command prompt, type "bash" to start a bash shell. Then run the following commands:
    ```
    sudo apt update
    sudo apt install git
    sudo apt install wget
    ```

(you may need to type your computer login password)

3. Install Anaconda for Linux with Python 3.7 (note: *not* Anaconda for Windows!). To do this, in your command prompt, again make sure you are in the bash shell (if you still have the window open from the last step, use that, or type "bash" in a new command prompt). Then run:
    ```
    wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
    bash Anaconda3-2020.02-Linux-x86_64.sh
    ```
PS: To access the content of your Linux distribution from your windows interface you may follw the steps described on [this website](https://www.howtogeek.com/261383/how-to-access-your-ubuntu-bash-files-in-windows-and-your-windows-system-drive-in-bash/)

The summary is as follows:

Go to your home directory (`C:\Users\remyj` for me) on windows with your usual graphical interface. Among the tabs on the top right click `View` and tick the `Hidden items`  box, then open `AppData\Local\Packages`

In there you should find a file with a barbaric name like `CanonicalGroupLimited.Ubuntuxxxxxxxxx` or search for something that has the name of your distribution in it. Personally I ordered files by date and found the file corresponding to the date I installed the distro.

Once in there go to `LocalState\rootsf\home`  and you should see your home directory.

PPS: To do the converse operation and see your windows files from you Ubuntu prompt, you may do so by typing in your Unix prompt:
    ```
    /mnt/c/Users/remy
    ```

## If you use Linux on your laptop:

1. Install Anaconda for Linux with Python 3.7. Open a terminal prompt, then run:
    ```
    wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
    bash Anaconda3-2020.02-Linux-x86_64.sh
    ```


## If you use Mac OSX on your laptop:

1. Please make sure you have the command-line tools installed. Open the Terminal program and run the following command:
    ```
    xcode-select --install
    ```

2. Install Anaconda for Mac with Python 3.7. Download the following installer, then double-click to open it and follow instructions to install:

   https://repo.anaconda.com/archive/Anaconda3-2020.02-MacOSX-x86_64.pkg

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

