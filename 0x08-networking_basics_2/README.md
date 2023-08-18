#	`0x08. Networking basics #1`

#### DevOps | Network | SysAdmin

=======================================================================

## General Learning Objectives

	* What is localhost/127.0.0.1
	* What is 0.0.0.0
	* What is /etc/hosts
	* How to display your machine’s active network interfaces

## General Requirements

	* Allowed editors: vi, vim, emacs
	* All your files will be interpreted on Ubuntu 20.04 LTS
	* All your files should end with a new line
	* A README.md file, at the root of the folder of the project, is mandatory
	* All your Bash script files must be executable
	* Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any errors
	* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	* The second line of all your Bash scripts should be a comment explaining what is the script doing


## `Tasks | Mandatory`

### 0. Change your home IP

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:
* localhost resolves to 127.0.0.2
* facebook.com resolves to 8.8.8.8.
* The checker is running on Docker
* before running the script, localhost resolves to 127.0.0.1 and facebook.com resolves to 157.240.11.35
* after running the script, localhost resolves to 127.0.0.2 and facebook.com resolves to 8.8.8.8
If you’re running this script on a machine that you’ll continue to use, be sure to revert localhost to 127.0.0.1. Otherwise, a lot of things will stop working!

### 1. Show attached IPs

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
Obviously, the IPs displayed may be different depending on which machine you are running the script on.

Note that we can see our localhost IP :)

## `Tasks | Advanced`

Write a Bash script that listens on port 98 on localhost.

For the sake of the exercise, this connection is made entirely within localhost. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!
