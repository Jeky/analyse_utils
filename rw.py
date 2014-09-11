import data

COUNT = 1000
RW_DATA_FILE = data.RW_PATH + '%d/rw-%d.list'

def loadRWData(jp, index = None):
    if not index: # load all data by jp
        rw = []

        for i in range(COUNT):
            rw += loadSingleRWData(jp, index)

        return rw
    else:
        return loadSingleRWData(jp, index)

def loadSingleRWData(jp, index):
    rw = []

    f = open(RW_DATA_FILE % (int(jp * 100), index))
    print 'Loading', f
    for i, l in enumerate(f.xreadlines()):
        tid, tag = l.strip().split('\t')
        rw.append({
                'id' : tid,
                'tag': tag
            })

    f.close()