# pySokoban
Sokoban is a japanese transport puzzle game originally developped by Hiroyuki Imabayashi in 1982. The name comes from Japan and means "warehouse keeper". The player pushes boxes or crates around in a warehouse, trying to get them to storage locations. This implementation is based on Python & pyGame Library.

## System Requirements
Python 3 & pyGame 2

## How to play
Use arrows keys to move player
U   => Undo move
R   => Reset level
ESC => Exit game

## Themes
To change theme change the following line of code into sokoban.py file
```theme = "soft"```

At this moment three themes are supported. [soft | default | ksokoban]

## Level Sets
Original game (published 1982 by Thinking Rabbit) included 20 levels. Sokoban 2 (1984) included 50 levels. Spectrum HoloByte was the first game company to bring Sokoban to gamers outside Japan with it's 1988 release called Soko-Ban. This release included 50 levels and are those levels called "original" nowdays.
In pySokoban each level is a plain text file. A collection of levels is called a "Level Set". The most commonly used format for representing a level is the following:

| Level element         |  Character |
| --------------------- |:----------:|
| Wall                  | #          |
| Player                | @          |
| Player on goal square | +          |
| Box                   | $          |
| Box on goal square    | *          |
| Goal square	        | .          |
| Floor                 | (Space)    |

A typical level looks like this:

```
   #########
  ##   ##  ######
###     #  #    ###
#  $ #$ #  #  ... #
# # $#@$## # #.#. #
#  # #$  #    . . #
# $    $ # # #.#. #
#   ##  ##$ $ . . #
# $ #   #  #$#.#. #
## $  $   $  $... #
 #$ ######    ##  #
 #  #    ##########
 ####
```

In pySokoban each "Level Set" is stored in a subdirectory inside "levels" directory. For example the original Level Set (50 levels) from Spectrum HoloByte is stored under levels/original directory. Different Level Sets reside in different directories. To play a different Level Set change the following line of code into sokoban.py file
```level_set = "original"```

## Screenshots
Default theme
!["Screenshot of the game"](themes/default/images/screenshot.png?raw=true "Screenshot of the game")
Soft theme
!["Screenshot of the game"](themes/soft/images/screenshot.png?raw=true "Screenshot of the game")
Ksokoban theme
!["Screenshot of the game"](themes/ksokoban/images/screenshot.png?raw=true "Screenshot of the game")

## To Do
* Refactor movePlayer() function
* Count moves & pushes
* Show moves & pushes in interface

## Known bugs
* When player is on goal square and the u (Undo) button is pressed and then an arrow key is pressed an unnecessary goal square is created.
