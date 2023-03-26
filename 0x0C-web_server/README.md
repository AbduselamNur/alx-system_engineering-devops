#	`0x0C. Web server`

#### DevOps | SysAdmin

========================

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

## General Learning Objectives

	* What is the main role of a web server
	* What is a child process
	* Why web servers usually have a parent process and child processes
	* What are the main HTTP requests

## DNS
	* What DNS stands for
	* What is DNS main role

## General Requirements
	
	* Allowed editors: vi, vim, emacs
	* All your files will be interpreted on Ubuntu 16.04 LTS
	* All your files should end with a new line
	* A README.md file, at the root of the folder of the project, is mandatory
	* All your Bash script files must be executable
	* Your Bash script must pass Shellcheck (version 0.3.7) without any error
	* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	* The second line of all your Bash scripts should be a comment explaining what is the script doing
	* You can’t use systemctl for restarting a process

## `Tasks | Mandatory`

### 0. Transfer a file to your server

Write a Bash script that transfers a file from our client to a server:

Requirements:

* Accepts 4 parameters
	1. The path to the file to be transferred
	2. The IP of the server we want to transfer the file to
	3. The username scp connects with
	4. The path to the SSH private key that scp uses
* Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
* scp must transfer the file to the user home directory ~/
* Strict host key checking must be disabled when using scp
