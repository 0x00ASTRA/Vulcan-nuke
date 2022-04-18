# Vulcan-nuke
An SSD nuke program written in python.

by AJBlondell

-----
VULCAN-Nuke
-----

VULCAN uses the linux modules, cryptsetup and shred to encrypt and wipe solid-state 
storage volumes. So far it has only been tested on ubuntu based distros, but eventually 
I would like to make it crossplatform(MacOS/Windows/Linux).

To use:
  
  1) clone the repository.
  
  2) edit the drive list in 'main.py' to contain the paths of the drives you would like
     to wipe.
     
  3) open a superuser terminal in the Vulcan-nuke directory.
  
  4) run the 'test.py' file and input how number of passes you would like to wipe the 
     drives with into the terminal.
