import rw
import data

def var(data, rank, tid, size, count):
    '''
    This function will return two variance values: 
        v1 using real mean, v2 using real rank
    '''
    rankList = []
    v1 = 0.0
    v2 = 0.0
    mean = 0.0

    for i in range(count):
        rankList.append(data.getRank(tid, [d['id'] for d in data[size * i: size * (i + 1)]]))

    for r in rankList:
        mean += r

    mean /= count

    for r in rankList:
        v1 += (r - mean) ** 2
        v2 += (r - rank) ** 2

    v1 /= count
    v2 /= count

    return v1, v2


if __name__ == '__main__':
    JP_LIST = [0.01 * i for i in range(1, 21)]
    RANK_LIST = range(20)
    SIZE_LIST = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    COUNT = 1000

    varOut = open(data.VAR_FILE, 'w')
    idList = deg.loadDegData(100)

    for jp in JP_LIST:
        data = rw.loadRWData(jp)

        for rank in RANK_LIST:
            tid = idList[rank]

            for size in SIZE_LIST:
                v1, v2 = var(data, rank, tid, size, COUNT)
                varOut.write('%0.2f,%d ,%d  ,%d  ,%lf,%lf\n' %\
                             (jp   ,tid,rank,size,v1 ,v2))

    varOut.close()