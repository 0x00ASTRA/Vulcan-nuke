# Vulcan-nuke
An SSD nuke program written in python.

by AJBlondell

=======================================================================================
                 _       _______ _______ _             _               _       _______ 
|\     /|\     /( \     (  ____ (  ___  | (    /|     ( (    /|\     /| \    /(  ____ \
| )   ( | )   ( | (     | (    \/ (   ) |  \  ( |     |  \  ( | )   ( |  \  / / (    \/
| |   | | |   | | |     | |     | (___) |   \ | |_____|   \ | | |   | |  (_/ /| (__    
( (   ) ) |   | | |     | |     |  ___  | (\ \) (_____) (\ \) | |   | |   _ ( |  __)   
 \ \_/ /| |   | | |     | |     | (   ) | | \   |     | | \   | |   | |  ( \ \| (      
  \   / | (___) | (____/\ (____/\ )   ( | )  \  |     | )  \  | (___) |  /  \ \ (____/\
   \_/  (_______|_______(_______//     \|/    )_)     |/    )_|_______)_/    \(_______/

=======================================================================================


Vulcan uses the linux modules, cryptsetup and shred to encrypt and wipe solid-state 
storage volumes. So far it has only been tested on ubuntu based distros, but eventually 
I would like to make it crossplatform(MacOS/Windows/Linux).

To use:
  
  1) clone the repository.
  
  2) edit the drive list in 'main.py' to contain the paths of the drives you would like
     to wipe.
     
  3) open a superuser terminal in the Vulcan-nuke directory.
  
  4) run the 'test.py' file and input how number of passes you would like to wipe the 
     drives with into the terminal.
