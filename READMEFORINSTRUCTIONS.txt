First time:

1. Install the latest version of Python 3. If you're using W10, install it through the Microsoft Store.

2. Make a copy of your TLC install to use for the randomizer.

3. Unpack the FinalAlbion.wad file per usual. Here's how if you're unsure:
	a.  Get Freeroam. 
	b. In the top left, select "File>Open". Go into YourRandoInstall\data\Levels\FinalAlbion.wad.
	c.  Select the TNG and LEV (Unpatched) options. 
	d. Save the rip to the data folder (YourRandoInstall\data\).
	e. Make sure the FinalAlbion folder is in your Levels folder. 
	f. Rename FinalAlbion.wad to something else like BackupFinalAlbion.wad.
	g. Copy the new FinalAlbion folder to bring it to the OneWayRandomizer folder.
	h. Go to YourRandoInstall\usersst.ini, and change "UseLevelWAD" to "FALSE;"
	i. Make sure to close Freeroam.

4. Unzip your OneWayRandomizer folder. Paste the FinalAlbion folder inside the OneWayRandomizer folder, and also in Backup, just in case. 

5. RENAME THE FinalAlbion FOLDER TO "TNGS"

6. Open the TNGS folder, and create an empty folder inside called FinalAlbion. This is your output folder and will host your randomized .tngs.

7. Open a command prompt in the OneWayRandomizer folder. (For W10, in the OneWayRandomizer folder, press Alt+D, type cmd, and press enter)

8. Type "FableRandomizerOneWay.py" (no quotes) into the command prompt and press enter. 

*If you receive an error, make sure your tngs are in the correct folder \OneWayRandomizer\TNGS\. Make sure there is a folder inside \OneWayRandomizer\TNGS\ called FinalAlbion. If nothing else, just close and reopen cmd and try again.

If done correctly, it should finish with Witchwood_Leadout_08.tng

9. Go to \OneWayRandomizer\TNGS\ and copy the FinalAlbion folder within. Go to your randomizer install and paste it in Levels. It should replace 397 files.

10. You need to edit Fable.exe in your randomizer install to allow you to exit quest areas. Open it in a hex editor like HxD, go to (ctrl+G) F75741, and change 01 to 00.

You did it! Note that some exits and entrances are not randomized on preexisting saves. You will need to make a new save. 


~~~~~


If you want to randomize again:

1. Run FableRandomizerOneWay.py in cmd again.

2. Copy FinalAlbion folder from inside \OneWayRandomizer\TNGS\ to your rando install's Levels folder.

3. You did it. Make a new save, just to be safe. 


~~~~~


Some more info:

Heroes' Guild<->Guild Woods, Arena Entrance<->Hall of Heroes, Hall of Heroes<->Arena Anteroom, Arena Anteroom<->Arena, and Lookout Point<->Prophet's Chamber are all static. Trust me, it's better this way. For now.

If you want to put those back in to be randomized, take the contents of RemovedUIDList.txt and add them to UIDList.txt in the map folder.

A cool feature: for dead end maps, the only entrance to the map will never be within the map itself. This makes dead end maps more accessible. To remove this, make a backup of UIDList.txt in the map folder, then go through the list and remove all "NeverBe [UID]".

It also includes a cheat sheet, granted it's really hard to understand!

If you have any questions, ask the Fable Speedrun mods or message me on Discord at  Avethis#0002