import data

COUNT = 1000
RW_DATA_FILE = data.RW_PATH + '%d/rw-%d.list'

def loadRWData(jp, index = None):
    if not index: # load all data by jp
        rw = []

        for i in range(COUNT):
            loadSingleRWData(rw, jp, i)

        return rw
    else:
        return loadSingleRWData(jp, index)


def loadSingleRWData(rw, jp, index):
    f = open(RW_DATA_FILE % (int(jp * 100), index))
    print 'Loading', RW_DATA_FILE % (int(jp * 100), index)

    for l in f.xreadlines():
        tid, tag = l.strip().split('\t')
        rw.append(int(tid))

    f.close()