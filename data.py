from collections import Counter

DATA_PATH = '/Volumes/Time Machine/jeky/twitter/'

GRAPH_FILE = DATA_PATH + 'twitter-encode.graph'
GRAPH_MAP = DATA_PATH + 'twitter.map'
RW_PATH = DATA_PATH + 'rw/'

OUTPUT_FILE = DATA_PATH + 'twitter.output'
DEG_FILE = DATA_PATH + 'twitter-deg.list'


def getRank(tid, idList):
    ranker = Counter()

    for i in idList:
        ranker[i] += 1

    if ranker.has_key(tid):
        return [i[0] for i in ranker.most_common()].index(tid)
    else:
        return -1
