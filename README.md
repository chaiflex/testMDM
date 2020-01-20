Project: Motion Processing
======================

The main purpose of this project is to count Occurence of each strings into queries entry

Requirements and settings
-----------------------------------

__1. Configuration:__
- Ubuntu 16.04
- Python 3.X
- Set environment variable [STRINGS_TEST]

__2. Python Libraries:__
Under Ubuntu 18.04 (should work with 16.O4) 
```shell
> sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 
> python --version 
Python 3.6.5
```

__4. To be installed__	
* numpy==1.18.1

__5. Command to use to install additionnal package__
```shell
> sudo apt install python3-pip
> pip3 install resource [PACKAGENAME]
>
>OR
> pythonX -m pip [PACKAGENAME]
```

How to run 
--------------
The library countOccurence

```shell
> python3 countOccurence.py [QUERIES]
```

Data description
----------------
__1. Input Data__ 

The library take as input the queries data

__2. Parameters inputs__

QUERIES

__3. Output Data__

To generate the dictionnary of occurence.

Usage
-------------------------

__1. Usage__


The main purpose of the script is to be use with gcp as part of Kuberetes deployment.
User can use the library by cloning the git repository:

__https://git.connecthings.com/data/__
