import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib import dates
import datetime

myFile = open("dataBase.txt","r")
s = myFile.readline()
l = [x.split(',') for x in s.split('\t')]
#print(l)
l.pop(-1)

X = []
Y = []
for i in l:
    #print('it: {}', i)
    X.append(i[0])
    Y.append(int(i[1]))

X2 = list(map(datetime.datetime.strptime, X, len(X)*['%Y-%m-%d %H:%M:%S']))
#X3 = matplotlib.dates.date2num(X2)
formatter = dates.DateFormatter('%Y-%m-%d %H:%M:%S')

#print('this is the X:')
#print(X2)
#print('this is the Y:')
#print(Y)
#plt.plot(X2, Y)
#matplotlib.pyplot.plot_date(X3, Y)

pyplot.plot( X2, Y, '-' )
ax = pyplot.gcf().axes[0] 
ax.xaxis.set_major_formatter(formatter)
pyplot.gcf().autofmt_xdate(rotation=25)
pyplot.show()

