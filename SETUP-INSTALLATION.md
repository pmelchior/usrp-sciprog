Welcome to the USRP software and computing tutorial week!

The plan for the week is to give you an overview of good things to know when it comes to scientific computing, give you time to do some hands-on exercises, and provide resources for you to learn more. We aim to cover basic unix commands and remote login (ssh), software version control (git and github), the Python programming language and scientific programming stack, and basic statistics. Given that we only have a week, we will only scratch the surface on each of these topics, but many of us will be around and willing (physically or via email/Slack) to provide support and additional guidance throughout the summer.

With that in mind, there are a few things we would like you all to do *before* arriving next Tuesday. Please try to do this by the end of *this* week, so if you run into any issues we can try to help solve before you arrive.


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
    wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    bash Anaconda3-2019.03-Linux-x86_64.sh
    ```


## If you use Linux on your laptop:

1. Install Anaconda for Linux with Python 3.7. Open a terminal prompt, then run:
    ```
    wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    bash Anaconda3-2019.03-Linux-x86_64.sh
    ```


## If you use Mac OSX on your laptop:

1. Please make sure you have the command-line tools installed. Open the Terminal program and run the following command:
    ```
    xcode-select --install
    ```

2. Install Anaconda for Mac with Python 3.7. Download the following installer, then double-click to open it and follow instructions to install:

   https://repo.anaconda.com/archive/Anaconda3-2019.03-MacOSX-x86_64.pkg

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

