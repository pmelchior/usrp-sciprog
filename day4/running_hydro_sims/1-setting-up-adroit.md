# Computing infrastructure: setting up your adroit environment

Most of this page has been presented to you already on Day 1. We repeat here what is specifically required for running hydro simulations on the `adroit` cluster.

We will first explain how to connext to `adroit` using `ssh` on the Terminal window of your laptop or using a Web interface.We will then explain how to set up the software environment on `adroit` using the `module load` command.

## Using the Terminal window on your laptop

You first need to install an X sever and a Terminal window manager.

For MacOS, use:

- iTerm for the Terminal window [click here to download](https://iterm2.com)
- XQuartz for the X server [click here to download](https://www.xquartz.org)

For Windows, use:

- PuTTY or KiTTY to connect remotely using the ssh protocol [click here to download](https://www.putty.org)
- Xming for the X server [click here to download](http://www.straightrunning.com/XmingNotes/)


## Connection to adroit

You have many different options to connect to the `adroit` supercomputing cluster. 

- using the ssh protocol from a Terminal window on your laptop or using a ssh client such as PuTTY. Type in the Terminal window the following command line:

		$ ssh -X yourlogin@adroit.princeton.edu

- using `myadroit` and a Web interface. You need to be on campus or use a VPN connection. In your browser, connect to [myadroit.princeton.edu](https://myadroit.princeton.edu/pun/sys/dashboard). Go to the menu **Clusters** and choose the option **_Adroit Cluster Shell Access** [you can also click here](https://myadroit.princeton.edu/pun/sys/shell/ssh/adroit). 

In both case, you shoud be now in a Terminal window on `adroit`. You need to get familiar with the Linux operating system and the corresponding languqge called `bash`. A few basic commands are listed here:

| Command | Examples | Description |
| :----------- | :----------- | :----------- |
| ``ls`` | ``ls``<br> ``ls -als`` | List files in current directory <br> List in long format including hidden files and file sizes|
| ``cd`` | ``cd ..`` <br> ``cd week9`` <br> ``cd ~bob/se-for-sci/content``| Change to parent directory <br> Change to directory ``week9`` <br> Change to target directory inside Bob's SE course directory|
| ``mkdir`` | ``mkdir test``| Creating a new directory called ``test`` |
| ``rmdir`` | ``rmdir test`` | Removing the directory called ``test`` |
| ``cp`` | ``cp file1.txt file2.txt`` <br> ``cp ~bob/file1.txt .`` <br> ``cp ~bob/* .`` <br> ``cp -r ~bob/se-for-sci .`` | Copy ``file1.txt`` into a new file called ``file2.txt`` <br> Copy the file called ``file1.txt`` in Bob's home directory into a new file locally keeping the same name <br> Copy all the files in Bob's home directory locally giving them the same name <br> Copy recursively the entire content of Bob's SE course directory locally keeping the same names | 
| ``rm`` | ``rm file1.txt`` <br> ``rm -rf *`` | Remove only the file called ``file1.txt`` <br> Remove recursively all files and directories without asking permission (very dangerous) |
| ``mv`` | ``mv ~bob/file1.txt file2.txt`` | Move one file into another location and with a new name |
| ``more`` | ``more file1.txt`` | Look at the file content one page at a time |
| ``man`` | ``man more`` | Look at the manual for a given Linux command |
| ``grep`` | ``grep Hello file1.txt`` | Search for string ``Hello`` inside the file ``file1.txt`` |


## Setting up your adroit environment

The software environment can be configured using the **Environment Module Package** on `adroit`. 

In order to see what software packages are available on `adroit`, type:

		$ module avail
		
You will see a long list of software like:

```
---------------------------------- /usr/share/Modules/modulefiles -----------------------------------
dot  module-git  module-info  modules  null  use.own
-------------------------------------- /usr/share/modulefiles ---------------------------------------
mpi/mpich-x86_64
------------------------------- /usr/local/share/Modules/modulefiles --------------------------------
boost/1.73.0                  fftw/gcc/openmpi-4.1.0/3.3.9                openblas/0.3.x
cmake/3.18.2                  gsl/2.6                                     openmpi/gcc/4.1.0
cudatoolkit/10.2              hdf5/gcc/1.10.6                             R/3.6.3
cudatoolkit/11.1              hdf5/gcc/intel-mpi/1.10.6                   R/4.0.5
cudatoolkit/11.3              hdf5/gcc/openmpi-4.0.4/1.10.6               R/4.1.3
cudatoolkit/11.4              hdf5/gcc/openmpi-4.1.0/1.10.6               R/4.2.3
cudatoolkit/11.7              netcdf/gcc/hdf5-1.10.6/4.7.3                ucx/1.9.0
```
In order to see the list of packages already installed in your environment, type:

		$ module list
		No Modulefiles Currently Loaded.

We want now to install the Message Passing Interface (MPI) library. For this, type:

		$ module load openmpi/gcc/4.1.0

You can check that it has been properly loaded by typing:

		$ module list
		Currently Loaded Modulefiles:
 		1) openmpi/gcc/4.1.0  

You can unload it by typing:

		$ module unload openmpi/gcc/4.1.0

You can check it is gone by typing:

		$ module list
		No Modulefiles Currently Loaded.

You can load these 2 important packages that we will need later for running hydro simulations:

		$ module load openmpi/gcc/4.1.0 
		$ module load anaconda3/2021.5

