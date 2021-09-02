import random

dice_face = []
dice_value = random.randint(1,6)

def creating_the_dice():
    for k in range(3):
        dice_face.append([])
    for l in dice_face:
        for k in range(3):
            dice_face[k].append("")

def diceface():
    for k in dice_face:
        for l in k:
            l = "*"
def printing_dice_face():
    for k in dice_face:
        print(k)

def deciding():
    print("dice value is: ", dice_value)
    if dice_value == 1:
        dice_face[1][1] = "X"
    elif dice_value == 2:
        dice_face[0][0] = "X"
        dice_face[2][2] = "X"
    elif dice_value == 3:
        dice_face[0][0] = "X"
        dice_face[1][1] = "X"
        dice_face[2][2] = "X"
    elif dice_value == 4:
        dice_face[0][0] = "X"
        dice_face[0][2] = "X"
        dice_face[2][0] = "X"
        dice_face[2][2] = "X"
    elif dice_value == 5:
        dice_face[0][0] = "X"
        dice_face[0][2] = "X"
        dice_face[1][1] = "X"
        dice_face[2][0] = "X"
        dice_face[2][2] = "X"
    elif dice_value == 6:
        dice_face[0][0] = "X"
        dice_face[0][2] = "X"
        dice_face[1][0] = "X"
        dice_face[1][2] = "X"
        dice_face[2][0] = "X"
        dice_face[2][2] = "X"




def main():
    creating_the_dice()
    diceface()
    deciding()
    printing_dice_face()



main()
