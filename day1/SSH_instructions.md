## SSH and remote login

We will now learn how to connect between your laptop and remote machine. That's what ssh does. With this you will be able to exchange files between your machine and the remote machine. This is particularly useful if you need to do computation on datasets that are too large for your laptop to handle for instance. This way, your laptop can be used to develop code or use programs that are already installed on your machine. 

The detailed informations about ssh and remote login are described in the following:

See the information here:
https://researchcomputing.princeton.edu/ssh

Make an SSH key:
https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-linux

We strongly recommend that you read these instructions to get a better understanding of ssh and ssh keys. In the following, we will see how to setup an ssh key and use it to. Connect remotely.

This year we will use **MyAdroit Web Portal** to run Jupyter Notebook.

### SSH key

SSH keys are a mean of identification between two machines. One machine, the one we would like to ssh from, has to generate a key. The key is then passed on to the machines that we want to access. This way, it ensures that only the machines to which we sent a key can connect.

To setup an ssh key, simply type on your computer:

    ssh-keygen -t ecdsa -b 521

You should the following lines appear:

	Generating public/private ecdsa key pair.
	Enter file in which to save the key (/Users/remy/.ssh/id_ecdsa):

This is asking you to chose a file to save the key. The default choice is perfectly fine, so just type `enter`. 

CAREFUL NOW!! The next line is more important. You should now see this appear:

	Enter passphrase (empty for no passphrase):

At this point, you NEED to type a passphrase that you will be able to remember.

This has created a private key (/Users/remy/.ssh/id_ecdsa) that you should keep like it is your browser history. The public key (/Users/remy/.ssh/id_ecdsa.pub) is made to be shared with computers that would like to connect to. 

To make sure that no one else but you can see these, enter the following lines:

	chmod 700 ~/.ssh
	chmod 600 ~/.ssh/id_ecdsa

For this purpose, send your public key to Leigh Koven via secure send so that you can have it on your department machine.

On your department machine, go to the folder where your `id_ecdsa.pub` is. We will now append our authorized_keys file to allow the key to be used on your laptop:

	cat id_ecdsa.pub >> ~/.ssh/authorized_keys

Again, let's make sure that our files remain visible only by us:

	chmod 700 ~/.ssh
	chmod 600 ~/.ssh/authorized_keys


Now you should be able to ssh your department machine from your computer.
Type:

	ssh login@domain

### SCP

A particularly useful command using the ssh protocol is the scp command. Command scp serves the same purpose as cp, but between remote machines (your laptop and your department machine for instance). The scp command is used as follows:

	scp origin user@host:path

Create a file on your machine with text,not on the department machine, so this should not follow the ssh command. Either terminate ssh or open a new terminal.

	cat > your_filename.txt
	your text
	ctrl-c

Now copy the file to your department machine:

	scp ./your_filename.txt user@host:

Try the other way around: copying a file from your department machine to your laptop.
