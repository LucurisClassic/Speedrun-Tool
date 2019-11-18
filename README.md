# WoW-Livesplit
Automatically split your runs when a boss dies.

### Requirements
  * Python
    * [Pip](https://pip.pypa.io/en/stable/installing/)
    * Pynput (From Command Prompt: `pip install pynput`)
  * [Memoria](https://www.curseforge.com/wow/addons/memoria) - Takes a screenshot when a raid boss dies. Remember to enable it to take screenshots of bosses you have killed before. 
  * [LiveSplit](http://livesplit.org/) - A tool used by speed runners for Ocarina of Time, Super Mario Bros, and more.
    [LiveSplit layout example](https://imgur.com/dxKTVi9)

### Live Split Setup
  1. Open Live Split and right click on the interface.
  2. Import the layout and choose from file `Molten_Core.lsl`.
  3. Import the splits (for example from the included file `MC.lss`). If you do not want to use my splits you can: still import the `MC.lss` file and delete the segement timers, or write in the boss names yourself and start blank. 
  5. In Settings assign a hotkey for splits and resets.
  6. Make sure Global Hotkeys are enabled.
  
### Python Script Setup
  1. Change the hot key (I use F1) on line 23 of `splits.py` to match the setting in Live Split.
  2. Unbind the key in WoW Keybinds.
  
  
### Running the Script
  * Open Command Prompt from the Start Menu.
  * Type: python C:\path\to\splits.py
  * Press the hotkey when you initiate the first pull and the script will handle the rest.
