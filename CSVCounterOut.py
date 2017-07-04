import re
from collections import Counter


def CSVCounterOut(InFileName,OutFileName,CleanseParameters,LineHeader):
    InputReader=open(InFileName,'r')
    OutputWriter=open(OutFileName,'w')
    for chunk in InputReader.readlines():
        for Word,Repeat in Counter(re.findall(CleanseParameters,chunk)).items():
            if len(Word)>1:
                OutputWriter.write('%s,%s,%s' % (LineHeader,Word,Repeat))
                OutputWriter.write('\n')
    OutputWriter.close()

