# Vulcan-nuke
An SSD nuke program written in python.

by AJBlondell

-----
VULCAN-Nuke
-----

VULCAN uses the linux modules, cryptsetup and shred to encrypt and wipe solid-state 
storage volumes. So far it has only been tested on ubuntu based distros, but eventually 
I would like to make it crossplatform(MacOS/Windows/Linux)
MUST HAVE lshw and cryptsetup installed.

To use:
  
  1) clone the repository.
  
  3) open a superuser terminal in the Vulcan-nuke directory.
  
  4) run the 'main.py' file and input how number of passes you would like to wipe the 
     drives with into the terminal.
