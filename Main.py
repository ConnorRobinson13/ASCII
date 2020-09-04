import sys

import numpy as np
from PIL import Image

np.set_printoptions(threshold=sys.maxsize)

pic = Image.open("Nole.jpg")

pic = np.asarray(pic)

brightnessArray = np.empty((480, 640, 1), dtype=int)

for i in range(len(pic)):
    for j in range(len(pic[1])):
        avg = round((int(pic[i][j][0]) + int(pic[i][j][1]) + int(pic[i][j][2])) / 3)
        brightnessArray[i][j][0] = avg

ASCIIcharacters = "``` ^^^ \"\"\" ,,, ::: ;;; III lll !!! iii ~~~ +++ --- ??? ]]] [[[ }}} {{{ 111 ))) ((( ||| \\\\\\ " \
                  "/// ttt fff jjj rrr xxx nnn uuu vvv ccc zzz XXX YYY UUU JJJ CCC LLL QQQ " \
                  "000 OOO ZZZ mmm www qqq " \
                  "ppp ddd bbb kkk hhh aaa ooo *** ### MMM WWW &&& 888 %%% BBB @@@ $$$"

ASCIIarray = list(ASCIIcharacters.split(" "))

finalArray = np.empty((480, 640), dtype=str)

for i in range(len(brightnessArray)):
    for j in range(len(brightnessArray[1])):
        first = int(brightnessArray[i][j][0])
        second = (round(first / 3.984375))
        finalArray[i][j] = ASCIIarray[second - 1]

np.savetxt("data.csv", finalArray, delimiter="", fmt="%s")
