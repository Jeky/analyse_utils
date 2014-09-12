import data

def loadDegData(count = 0):
    print 'Loading Degree File...'
    f = open(data.DEG_FILE)

    idList = []
    for i, l in enumerate(f.xreadlines()):
        if i % 100000 == 0:
            print 'read', i, 'lines'

        if count and i == count:
            f.close()
            return idList

        tid, inDeg, outDeg = l.strip().split('\t')

        idList.append(int(tid))

    f.close()
    return idList