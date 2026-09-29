#import pylab
import pylab
listofints = []  #specify the range
for counter in range(10):
    listofints.append(counter*2)
    
print (listofints)
print (len(listofints))
#now plot the list
pylab.plot(listofints)
pylab.show()
