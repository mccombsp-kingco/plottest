import matplotlib.pyplot as plt
import numpy as np
import csv

'''
This is ultimately intended to read in csv files, convert them to
np arrays, then let the user pick items to plot on a graph using pyplot.
Right now it's hard coded to plot Star Wars 7 box office receipts and compare
to the next 3 highest selling movies.
Paul McCombs
20160/1/13
'''
            
def csv2numpy(filepath):
    'import csv file and return an Numpy Reccord Array excluding header'
    print "Importing %s to produce a numpy recarray."% filepath
    return np.recfromcsv(filepath, delimiter=',')

def numpy2pyplot(csvdata):
    'takes a numpy record array and returns a tuple of parameters suitable for plt.plot()'
    xcol = 'days'
    ycol = 'total_gross'
    xdata = csvdata[xcol]
    ydata = csvdata[ycol]
    plt.ylabel(ycol)
    plt.xlabel(xcol)
    return [xdata,ydata]
               
filenames = ["sw7.csv","avatar.csv","jworld.csv","titanic.csv"]
for fname in filenames:
    #plotparams = []
    csvdata = csv2numpy(fname)
    plotparams = numpy2pyplot(csvdata)
    plt.plot(label=fname, *plotparams)
    
plt.legend(loc='lower right')
plt.axis([1,300,100000000,1000000000])
plt.show()