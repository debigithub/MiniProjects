from urllib.request import Request,urlopen
from CSVCounterOut import CSVCounterOut


def scrapper(webpage,OutFile):
    url=Request(webpage,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'})
    f=urlopen(url)
    FileWriter=open(OutFile,'w')
    FileWriter.write(str(f.read()))
    FileWriter.close()

scrapper('http://www.ndtv.com','2017-07-04_ndtv.txt')
CSVCounterOut('2017-07-04_ndtv.txt','2017-07-04_Cleansed_ndtv.txt','[a-zA-Z0-9]+','2017-07-04,TOI')