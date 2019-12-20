# WoW-Livesplit
Automatically split your runs when a boss dies. This script may be against [Blizzard EULA Section 1.C.ii.4](https://www.blizzard.com/en-us/legal/fba4d00f-c7e4-4883-b8b9-1b4500a402ea/blizzard-end-user-license-agreement) I am still waiting/praying to get a reply from hacks@blizzard.com

### Requirements
  * Python
    * [Pip](https://pip.pypa.io/en/stable/installing/)
    * Pynput (From Command Prompt: `pip install pynput`)
  * [Memoria](https://www.curseforge.com/wow/addons/memoria) - Takes a screenshot when a raid boss dies. Remember to enable it to take screenshots of bosses you have killed before. 
  * [LiveSplit](http://livesplit.org/) - A tool used by speed runners for Ocarina of Time, Super Mario Bros, and more.
    [LiveSplit layout example](https://imgur.com/dxKTVi9)

### LiveSplit Setup
  1. Open LiveSplit.exe and right click on the interface.
  2. Import the layout by choosing the downloaded file `MC_Layout.lsl`.
  3. Import the splits from the downloaded file `MC_Splits.lss`. If you do not want to use my splits you can still import the `MC_Splits.lss` file and delete the segement timers, or write in the boss names yourself and start blank. 
  5. In Settings assign a hotkey for splits and resets. Enable Global Hotkeys.
  
### Python Script Setup
  1. Change the hot key (I use F1) on line 23 of `splits.py` to match the setting in LiveSplit.
  2. Unbind the key in WoW Keybinds.
  
### Running the Script
  * Open Command Prompt.
  * Type: `python C:\path\to\splits.py`
  * Press the hotkey when the raid initiates the first pull and the script will handle the rest.
