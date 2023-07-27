#  ``` 0x04. Loops, conditions and parsing ```

==================================================================

#### DevOps | Shell | Bash | Scripting

## Generl Learning Objectives

	* How to create SSH keys
	* What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
	* How to use while, until and for loops
	* How to use if, else, elif and case condition statements
	* How to use the cut command
	* What are files and other comparison operators, and how to use them

## General Requirements


	* Allowed editors: vi, vim, emacs
	* All your files will be interpreted on Ubuntu 20.04 LTS
	* All your files should end with a new line
	* A README.md file, at the root of the folder of the project, is mandatory
	* All your Bash script files must be executable
	* You are not allowed to use awk
	* Your Bash script must pass Shellcheck (version 0.7.0) without any error
	* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	* The second line of all your Bash scripts should be a comment explaining what is the script doing

## ``Tasks | Mandatory``

### 0. Create a SSH RSA key pair

Create a RSA key pair.

Requirements:

* Share your public key in your answer file 0-RSA_public_key.pub
* Fill the SSH public key field of your intranet profile with the public key you just generated
* Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
* If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

### 1. For Best School loop

Write a Bash script that displays Best School 10 times.

Requirement:
* You must use the for loop (while and until are forbidden)

### 2. While Best School loop

Write a Bash script that displays Best School 10 times.

Requirements:
* You must use the while loop (for and until are forbidden)

### 3. Until Best School loop

Write a Bash script that displays Best School 10 times.

Requirements:
* You must use the until loop (for and while are forbidden)

### 4. If 9, say Hi!

Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.

Requirements:
* You must use the while loop (for and until are forbidden)
* You must use the if statement

### 5. 4 bad luck, 8 is your chance

Write a Bash script that loops from 1 to 10 and:
* displays bad luck for the 4th loop iteration
* displays good luck for the 8th loop iteration
* displays Best School for the other iterations

Requirements:
* You must use the while loop (for and until are forbidden)
* You must use the if, elif and else statements
