import urllib2
import os

# Settings
years = [2013, 2014, 2015]
periods = ['d', 'w', 'm'] # daily, weekly, monthly
stocksFilename = 'stocklist.txt'
baseUri = 'http://real-chart.finance.yahoo.com/table.csv?s='
directory = 'stockcorpus'

def downloadFile(csvUrl):
    try:
        response = urllib2.urlopen(csvUrl)
        return response.read()
    except:
        print 'Problems with URL: ' + csvUrl
        return ''

def makeDir(name):
  try:
      os.makedirs(name)
  except OSError:
      pass

def writeToFile(filename, content):
    f = open(filename, 'a')
    f.write(content)
    f.close()

# Empty lines and lines with comments will be skipped
def readStockAbbrFile(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    cleanedLines = []
    for line in lines:
        if line.strip()[0] != '#' and line.strip() != '':
            cleanedLines.append(line)
    return cleanedLines

# Main:
stocks = readStockAbbrFile(stocksFilename)
makeDir(directory);
os.chdir(directory);
for year in years:
    makeDir(str(year));
    for period in periods:
        makeDir(str(year) + '/' + period)
    for stock in stocks:
        for period in periods:
            csv = downloadFile(baseUri + stock + '&a=00&b=1&c=' + str(year) + '&d=11&e=31&f=' + str(year) + '&g=' + period + '&ignore=.csv');
            if csv != '':
                writeToFile(str(year) + '/' + period + '/' + stock + '.txt', csv);
