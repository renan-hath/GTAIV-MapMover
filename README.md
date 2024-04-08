# GTAIV-MapMover

GTA IV Map Mover is a tool for moving map mods across the game map, by modifying the coordinates of each object placement and collision from .OPL and .OBN files. 

Map mods in GTA IV can get pretty large sometimes and it's not unusual for them to overlap, specially given the restricted space of water ingame where they are usually placed on. This mere incompatibility is usually enough for players to give up on one map for the sake of the other. This simple script aims to solve this by providing the means to the player to reposition their installed map mods somewhere differently from where the authors have intended to, enabling them to coexist.

The objects that compose such maps are defined in .IDE files, their meshes positioned through .WPL files, and their collisions, through .WBN files (located inside their .IMG files). By having all the .WPL and .WBN files converted to .OPL and .OBN files (readable formats), respectively, this script will bulk edit the X, Y and Z axes in such files by incrementing whatever floating values the player sets as parameters.

## Requirements

1. [Python](https://www.python.org/)
2. [OpenIV](https://openiv.com/)
3. Grand Theft Auto IV (required only to run OpenIV)

## How to use it

1. Download the **GTAIV-MapMover** folder.

2. Open the map mod in OpenIV.

3. Select all .WPL and .WBN files from the mod, right-click on them and click on *Export to Open Placement (.opl)* / *Export to openFormats (.obn)* to convert them to .OPL and .OBN and save them to ***GTAIV-MapMover\files***.

4. In **GTAIV-MapMover**, run the script by using the following command:

`python GTAIV_Map_Mover.py <X> <Y> <Z>`

( Example in case you wanted to move 300 units in the X axis, not change the Y axis, and pull down 20 units in the Z axis:

`python GTAIV_Map_Mover.py 300 0 -20` )

6. The files with modified coordinates will be placed in ***GTAIV-MapMover\modified_files***. In OpenIV, right-click, click on *Import openFormats*, and select the modified files to convert them back to .WPL and .WBN and replace the old ones in their respective locations.

## Preview

### Before
![Before](https://github.com/renan-hath/GTAIV-MapMover/assets/17623834/18f2e689-0299-45b0-ac04-5049a27df456)
### After
![After](https://github.com/renan-hath/GTAIV-MapMover/assets/17623834/98df86a6-ad56-464f-8841-4d8701c6fd24)
