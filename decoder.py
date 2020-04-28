from PIL import Image
import numpy as np
import sys
import string


def main():
    picName = sys.argv[1]
    img = Image.open(picName)
    ary = np.array(img)
    messageLength = 0
    chars = string.printable
    message = ""

    intToChar = {}

    index = 0
    for c in chars:
        intToChar[index] = c
        index += 1


    ind = -1
    for x in ary:
        for y in x:
            if ind == -1:
                lengthStr = ""
                for n in y:
                    lengthStr += str(n)[len(str(n)) - 1]
                messageLength = int(lengthStr)
            elif ind < messageLength:
                intToDecode = ""
                for n in y:
                    intToDecode += str(n)[len(str(n)) - 1]
                message += intToChar[int(intToDecode)]
            ind += 1

    print(message)


main()
