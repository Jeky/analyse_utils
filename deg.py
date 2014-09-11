import data

def loadDegData(count = 0):
    print 'Loading Degree File...'
    f = open(data.DEG_FILE)

    idList = []
    for i, l in enumerate(f.xreadlines()):
        if i % 1000000 == 0:
            print 'read', i, 'lines'

        if count and i == count:
            f.close()
            return idList

        idList.append(int(l.strip()))

    f.close()
    return idList