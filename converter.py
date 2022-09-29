from PIL import Image, ImageEnhance
import numpy

#The amount of characters the widest axis of the image will have
#Increasing this number will make the output more defined, but the program will take longer to process the image
#I personally recommend leaving this number at around 170-200
widest_px = 185

#Adjusts the contrast of the image in % (1.25 = 125%, .75 = 75% etc.)
#I wouldn't recommend increasing this past 2.5
contrast = 1.25

ascii= {range(0, 3): '@', range(3, 7): 'Q', range(7, 11): 'B', range(11, 15): '#', 
        range(15, 18): 'N', range(18, 22): 'g', range(22, 26): 'W', range(26, 30): 'M', 
        range(30, 33): '8', range(33, 37): 'R', range(37, 41): 'D', range(41, 45): 'H', 
        range(45, 48): 'd', range(48, 52): 'O', range(52, 56): 'K', range(56, 60): 'q', 
        range(60, 63): '9', range(63, 67): '$', range(67, 71): '6', range(71, 75): 'k', 
        range(75, 78): 'h', range(78, 82): 'E', range(82, 86): 'P', range(86, 90): 'X', 
        range(90, 93): 'w', range(93, 97): 'm', range(97, 101): 'e', range(101, 105): 'Z', 
        range(105, 108): 'a', range(108, 112): 'o', range(112, 116): 'S', range(116, 120): '2', 
        range(120, 123): 'y', range(123, 127): 'j', range(127, 131): 'u', range(131, 135): 'f', 
        range(135, 138): 'F', range(138, 142): ']', range(142, 146): '}', range(146, 150): '{', 
        range(150, 153): 't', range(153, 157): 'x', range(157, 161): '1', range(161, 165): 'z', 
        range(165, 168): 'v', range(168, 172): '7', range(172, 176): 'l', range(176, 180): 'c', 
        range(180, 183): 'i', range(183, 187): 'L', range(187, 191): '/', range(191, 195): '\\',
        range(195, 198): '|', range(198, 202): '?', range(202, 205): '*', range(205, 207): '>', 
        range(207, 209): 'r', range(209, 211): '^', range(211, 213): ';', range(213, 215): ':', 
        range(215, 217): '_', range(217, 219): '"', range(219, 221): '~', range(221, 223): ',', 
        range(223, 225): "'", range(225, 227): '.', range(227, 229): '-', range(229, 233): '`', range(233, 256): ' '}

def adjust(image, contrast):
    img = ImageEnhance.Contrast(image).enhance(contrast)

    iw, ih = img.size

    if iw >= ih:
        coef = iw/widest_px
    else:
        coef = ih/widest_px

    return img.resize((int(iw/(coef*(10/7))), int(ih/(coef*(10/4)))))

def build_ascii(array):
    new = [[]*i for i in range(len(array))]
    for i1, li1 in enumerate(array):
        for i2, li2 in enumerate(array[i1]):
            for rng in ascii.keys():
                if array[i1][i2] in rng:
                    new[i1].append(ascii[rng])
    return new

fn = input('Filename: ')

img = adjust(Image.open(fn), contrast).convert('L')

ary = numpy.array(img)

with open('output.txt', 'w') as f:
    ret = build_ascii(ary)
    output = ''.join([''.join([x for x in line])+'\n' for line in ret])
    f.write(output)
