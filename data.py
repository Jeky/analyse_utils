from collections import Counter

DATA_PATH = ''

GRAPH_FILE = DATA_PATH + ''
GRAPH_MAP = DATA_PATH + ''
RW_PATH = DATA_PATH + ''

VAR_FILE = DATA_PATH + ''
BIAS_FILE = DATA_PATH + ''
DEG_FILE = DATA_PATH + ''

def getRank(tid, idList):
    ranker = Counter()

    for i in idList:
        ranker[i] += 1

    if ranker.has_key(tid):
        return [i[0] for i in ranker.most_common()].index(tid)
    else:
        return -1
