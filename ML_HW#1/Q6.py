from os import walk
from PIL import Image
from tabulate import tabulate

DATASET_DIR = './Q6_Dataset/Images'

filenames = next(walk(DATASET_DIR), (None, None, []))[2]

TP = 0
FP = 0
TN = 0
FN = 0
for filename in filenames:
    if 'm' in filename:
        expectedClass = 1
    else:
        expectedClass = 0

    im = Image.open(DATASET_DIR + "/" + filename)
    rchannel = 0
    bchannel = 0
    count = 0
    for x in range(im.width):
        for y in range(im.height): 
            count += 1
            rchannel += im.getpixel((x,y))[0]
            bchannel += im.getpixel((x,y))[2]
    rchannel = rchannel / count
    bchannel = bchannel / count
    
    if rchannel > bchannel:
        predictedChannel = 1
    else:
        predictedChannel = 0

    if predictedChannel == 1 and expectedClass == 1:
        TP += 1
    elif predictedChannel == 0 and expectedClass == 0:
        TN += 1
    elif predictedChannel == 0 and expectedClass == 1:
        print(f'FN: {filename}')
        FN += 1
    else:
        print(f'FP: {filename}')
        FP += 1

print(tabulate([[TP, FP], [FN, TN]]))

accuracy = (TP+TN) / (TP+FP+FN+TN) 
precision = (TP) / (TP+FP)
recall = (TP) / (TP+FN)

print(f"Accuracy = {accuracy}")
print(f"Precision = {precision}")
print(f"Recall = {recall}")