from PIL import Image
import numpy as np
import sys
import string

def main():
    picName = sys.argv[1]
    hiddenText = sys.argv[2]

    img = Image.open(picName)
    ary = np.array(img)
    chars = string.printable
    messageLength = len(hiddenText)

    if messageLength > 999:
        print("message is too long, needs to be less than 1000 characters")
        return

    charToInt = {}

    index = 0
    for c in chars:
        charToInt[c] = index
        index += 1

    textToInt = []
    for l in hiddenText:
        textToInt.append(charToInt[l])

    ind = -1
    for x in ary:
        for y in x:
            if ind == -1:
                messageLengthStr = str(messageLength)
                messageLengthArr = list(messageLengthStr)
                for i in range(0, 3 - len(messageLengthArr)):
                    messageLengthArr.insert(0, "0")
                for n in range(0, 3):
                    rem = np.mod(y[n], 10)
                    y[n] = y[n] - rem + int(messageLengthArr[n])
            elif ind < messageLength:
                intToHide = textToInt[ind]
                intToHideStr = str(intToHide)
                intToHideArr = list(intToHideStr)
                for i in range(0, 3 - len(intToHideArr)):
                    intToHideArr.insert(0, "0")
                for n in range(0, 3):
                    rem = np.mod(y[n], 10)
                    y[n] = y[n] - rem + int(intToHideArr[n])
            ind += 1

    postImage = Image.fromarray(ary, 'RGB')
    postImage.save("images/post.png")

main()