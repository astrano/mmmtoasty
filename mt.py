#!/usr/bin/env python
import sys, time
import os
class color:
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'
skull = """      .ed\"\"\"\" \"\"\"\$$$$be.
     -\"           ^\"\"**$$$e.
   .\"                   \'$$$c
  /                      \"4$$b
 d  3                      $$$$
 $  *                   .$$$$$$
.$  ^c           $$$$$e$$$$$$$$.
d$L  4.         4$$$$$$$$$$$$$$b
$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
$$$$P d$$$$F $ $$$$$$$$$- $$$$$$
3$$$F \"$$$$b   $\"$$$$$$$  $$$$*\"
 $$P\"  \"$$b   .$ $$$$$...e$$
  *c    ..    $$ 3$$$$$$$$$$eF
    %ce\"\"    $$$  $$$$$$$$$$*
     *$e.    *** d$$$$$\"L$$
      $$$      4J$$$$$% $$$
     $\"\'$=e....$*$$**$cz$$\"
     $  *=%4.$ L L$ P3$$$F
     $   \"%*ebJLzb$e$$$$$b
      %..      4$$$$$$$$$$
       $$$e   z$$$$$$$$$$ 
        \"*$c  \"$$$$$$$P\"
          \"\"\"*$$$$$$$\""""
skulllaugh = """      .ed\"\"\"\" \"\"\"\$$$$be.
     -\"           ^\"\"**$$$e.
   .\"                   \'$$$c
  /                      \"4$$b
 d  3                      $$$$
 $  *                   .$$$$$$
.$  ^c           $$$$$e$$$$$$$$.
d$L  4.         4$$$$$$$$$$$$$$b
$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
$$$$P d$$$$F $ $$$$$$$$$- $$$$$$
3$$$F \"$$$$b   $\"$$$$$$$  $$$$*\"
 $$P\"  \"$$b   .$ $$$$$...e$$
  *c    ..    $$ 3$$$$$$$$$$eF
    %ce\"\"    $$$  $$$$$$$$$$*
     *$e.    *** d$$$$$\"L$$
      $$$      4J$$$$$% $$$
     $\"\'$=e....$*$$**$cz$$\"
     $$$                 $$
      $$$              $$$
     $  *=%4.$ L L$ P3$$$F
     $   \"%*ebJLzb$e$$$$$b
      %..      4$$$$$$$$$$
       $$$e   z$$$$$$$$$$ 
        \"*$c  \"$$$$$$$P\"
          \"\"\"*$$$$$$$\""""
crack = "\n       PROGRAM IS CRACK BY" + "\n    HACK SQUAD CHECKMATE 1992" + "\n        SERBIA BEST NATION\n"
mt = 69
if len(sys.argv) > 1 and sys.argv[1].isdigit():
  mt = int(sys.argv[1])
for i in range(mt):
  print color.RED + skull  + color.END + "\n          Mmmm... Toasty" + crack
  time.sleep(0.4)
  os.system('clear')
  print color.RED + skulllaugh  + color.END + "\n          Mmmm... Toasty" + crack
  time.sleep(0.4)
  os.system('clear')
