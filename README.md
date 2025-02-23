## Modifications from the original repository
This fork fixes the incomplete codebase to allow the repository to run on Ubuntu. Additionally, it greatly modifies the original installation bash script to allow easy installation on Ubuntu 

## Flurry
A fully automated framework to simulate host behavior and capture data provenance and system behavior for graph generation and representation learning.

## Description
Flurry is a simulation framework for different types of systems that researchers may want to gather provenance data from. Flurry comes equipped with tools for provenance capture and provenance graph generation. Using Flurry, researchers may run either prewritten attack or benign behavior scripts, capture these system processes and accesses, and generate graphs from them, or run custom scripts. The framework is highly customizable so that nearly any contrivable scenario can be experimented with and tested.


## Installation for Ubuntu
Download only the flurry-ubuntu.sh script and place it in your Ubuntu VM's /home/<user> directory. The script will download all the other dependencies and the repository automatically.

Open a terminal in the /home directory and give the script permission to execute with the command:

`sudo chmod +x flurry-ubuntu.sh`

Then, run it with:

`./flurry-ubuntu.sh`

This script should NOT be run with sudo.

This script will auto-reboot at the end.

## Provenance Capture Tools

CamFlow

CamFlow is a Linux security module designed for fine-grained, whole-system provenance capture. The module works by using hooks to monitor security access in the kernel space as well as NetFilter hooks to capture network provenance. These are passed via the CamFlow daemon to user-space, where it may be conveyed to a log file, piped to a storage back-end, or conveyed via message bus to some other interface. There are a number of configuration options both for the application and daemon in order to fine-tune the provenance capture to your liking. The system may also be configured for whole-system capture or target capture for specific files and/or processes.

sysdig (upcoming feature)


## Usage
To start the program, run

`source start.sh` in the flurry directory.

This will start the program and all required dependencies.

From there, select any number of attacks, behaviors, and scripts, then set the iteration count, provenance capture scope, and the convention to use for what constitutes a node and an edge. Once all the inputs have been made, Flurry should proceed automatically.

Note: In the browser-based attacks, the DVWA web page may fail to show up, even if the webserver is running. To fix it, access the page http://127.0.0.1/setup.php in a web browser and click the button at the bottom of the page to set up the DVWA’s SQL database. Then, run Flurry again.

## Advanced Usage
Advanced Execution
Custom Scripts
In addition to the 18 total attack and benign routines, Flurry supports custom scripts. The files in the scripts folder, which handle all the default routines, follow the same format as custom scripts and may be used as templates

Input Configuration
Flurry can be run using input configuration files. To save the input given for a run as a file, answer the prompt after Flurry has finished executing. To rerun the same inputs, simply start Flurry again and enter the local path to the config file. If a valid config file is provided, no further input will be required.

A typical input configuration file looks like this:
xssdom,xssreflected,commandinjection,message,ping
2
1
c
f


Functionally, this is just the set of inputs to use when responding to the prompts. The first line is a comma-separated list of attacks to run, the second is the number of iterations, the third is the provenance capture scope (1 is “whole system”), and lines four and five are the edge and node types, respectively. If the input involves custom scripts, they are added after the list of attacks, one line at a time:

sqlinjection,customattack,customattack,custombehavior
scripts/custom1.py
scripts/custom2.py
scripts/anothercustom.py
1
1
c
f


