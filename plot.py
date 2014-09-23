from data import *

# OUTPUT DATA FORMAT:
# JP,TWITTER_ID(AFTER_COMPRESSED),RANK(STARTS FROM 0),SAMPLE_SIZE,VAR1,VAR2,BIAS1,BIAS2

def loadOutput():
    f = open(OUTPUT_FILE)
    output = []

    for l in f.xreadlines():
        output.append([float(i) for i in l.strip().split(',')])

    f.close()

    return output

def select(output, conditionList, indexList):
    r = []
    for d in output:
        selected = True

        for c in conditionList:
            if not c(d):
                selected = False

        
