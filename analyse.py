import rw
import data
import deg

def analyse(rwData, rank, tid, size, count):
    '''
    This function will return two variance values and two bias value:
        v1 using real mean, v2 using real rank
        b1 using real mean, b2 using real rank
    '''
    rankList = []
    rank += 1
    v1 = 0.0
    v2 = 0.0
    mean = 0.0
    b1 = 0.0
    b2 = 0.0

    for i in range(count):
        rankList.append(1 + data.getRank(tid, rwData[size * i: size * (i + 1)]))#[d['id'] for d in rwData[size * i: size * (i + 1)]]))

    for r in rankList:
        mean += r

    mean /= count

    for r in rankList:
        v1 += (r - mean) ** 2
        v2 += (r - rank) ** 2

    v1 /= count
    v2 /= count

    b1 = (mean - rank) / rank

    return v1, v2, b1, b2


if __name__ == '__main__':
    JP_LIST = [0.01 * i for i in range(1, 21)]
    RANK_LIST = range(20)
    SIZE_LIST = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    COUNT = 1000

    varOut = open(data.OUTPUT_FILE, 'w')
    idList = deg.loadDegData(100)

    for jp in JP_LIST:
        rwData = rw.loadRWData(jp)

        for rank in RANK_LIST:
            tid = idList[rank]

            for size in SIZE_LIST:
                print 'Analysing...JP =', jp, ', Rank =', rank, ', Size =', size
                v1, v2, b1, b2 = analyse(rwData, rank, tid, size, COUNT)
                varOut.write('%0.2f,%d,%d,%d,%lf,%lf,%lf,%lf\n' %\
                             (jp   , tid, rank, size, v1 , v2 , b1 , b2))

    varOut.close()
