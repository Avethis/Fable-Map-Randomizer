First time:

1. Make a copy of your TLC install to use for the randomizer.

2. Unpack the FinalAlbion.wad file per usual. Here's how if you're unsure:
	a.  Get Freeroam. 
	b. In the top left, select "File>Open". Go into YourRandoInstall\data\Levels\FinalAlbion.wad.
	c.  Select the TNG and LEV (Unpatched) options. 
	d. Save the rip to the data folder (YourRandoInstall\data\).
	e. Make sure the FinalAlbion folder is in your Levels folder. 
	f. Rename FinalAlbion.wad to something else like BackupFinalAlbion.wad.
	g. Go to YourRandoInstall\usersst.ini, and change "UseLevelWAD" to "FALSE;"
	h. Make sure to close Freeroam.

3. Run FableRandomizerOneWay.exe in the mod's folder (it doesn't need to be in your game folder). There will be a success popup if the randomizer executed properly.

4. Go to \OneWayRandomizer\TNGS\ and copy the FinalAlbion folder within. Go to your randomizer install and paste it in Levels. It should replace 397 files.

5. You need to edit Fable.exe in your randomizer install to allow you to exit quest areas. Open it in a hex editor like HxD, go to (ctrl+G) F75741, and change 01 to 00.

You did it! Note that some exits and entrances are not randomized on preexisting saves. You will need to make a new save. 


~~~~~


If you want to randomize again:

1. Run the .exe again.

2. Copy FinalAlbion folder from inside \OneWayRandomizer\TNGS\ to your rando install's Levels folder.

3. You did it. Make a new save, just to be safe. 


~~~~~


Some more info:

Heroes' Guild<->Guild Woods, Arena Entrance<->Hall of Heroes, Hall of Heroes<->Arena Anteroom, Arena Anteroom<->Arena, and Lookout Point<->Prophet's Chamber are all static. Trust me, it's better this way. For now.

If you want to put those back in to be randomized, take the contents of RemovedUIDList.txt and add them to UIDList.txt in the map folder.

A cool feature: for dead end maps, the only entrance to the map will never be within the map itself. This makes dead end maps more accessible. To remove this, make a backup of UIDList.txt in the map folder, then go through the list and remove all "NeverBe [UID]".

It also includes a cheat sheet, granted it's really hard to understand!

If you have any questions, ask the Fable Speedrun mods or message me on Discord (Avethis)