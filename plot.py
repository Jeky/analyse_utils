from data import *

# OUTPUT DATA FORMAT:
# 0 JP
# 1 TWITTER_ID(AFTER_COMPRESSED)
# 2 RANK(STARTS FROM 0)
# 3 SAMPLE_SIZE
# 4 VAR1
# 5 VAR2
# 6 BIAS1
# 7 BIAS2

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

        if selected:
            r.append([d[i] for i in indexList])

    return r


def printPlotScript(result, outputFile, xlabel, ylabel, isLogX = False, isLogY = False):
    fout = open(outputFile, 'w')
    fout.write('data=[')
    for r in result:
        fout.write('%s;\n' % ','.join([str(i) for i in r]))
    fout.write('];')
    if isLogX and isLogY:
        fout.write('plot(log(data(:,1)), log(data(:,2)), \'x-\');\n')
    elif isLogX:
        fout.write('plot(log(data(:,1)), data(:,2), \'x-\');\n')
    elif isLogY:
        fout.write('plot(data(:,1), log(data(:,2)), \'x-\');\n')
    else:
        fout.write('plot(data(:,1), data(:,2), \'x-\');\n')

    fout.write('xlabel(\'%s\');\n' % xlabel)
    fout.write('ylabel(\'%s\');\n' % ylabel)

    fout.close()


if __name__ == '__main__':
    output = loadOutput()
    print 'Load Output Data:', len(output), 'rows...'
    for size in [10 ** 3, 10 ** 4, 10 ** 5]:
        for rank in range(20):
            result = select(output, [lambda c : c[3] == size, lambda c : c[2] == rank], [0, 4])
            printPlotScript(result, DATA_PATH + 'rw_result/jp_var_s%d_r%d.m' % (size, rank), 'JP', 'VAR', isLogY = True)
            result = select(output, [lambda c : c[3] == size, lambda c : c[2] == rank], [0, 6])
            printPlotScript(result, DATA_PATH + 'rw_result/jp_bias_s%d_r%d.m' % (size, rank), 'JP', 'BIAS', isLogY = True)

    for rank in range(20):
        for jp in [0.01 * i for i in range(1, 21)]:
            result = select(output, [lambda c : c[2] == rank, lambda c : c[0] == jp], [3, 4])
            printPlotScript(result, DATA_PATH + 'rw_result/size_var_j%d_r%d.m' % (jp * 100, rank), 'LOG(SIZE)', 'LOG(VAR)', isLogX = True, isLogY = True)
            result = select(output, [lambda c : c[2] == rank, lambda c : c[0] == jp], [3, 6])
            printPlotScript(result, DATA_PATH + 'rw_result/size_bias_j%d_r%d.m' % (jp * 100, rank), 'LOG(SIZE)', 'LOG(BIAS)', isLogX = True, isLogY = True)

    



