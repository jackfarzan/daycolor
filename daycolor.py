from scipy import misc
import numpy as np
import random
import datetime

random.seed(109283109)

out = np.zeros((1000, 100, 3), dtype=np.uint8)

timeprev = 0
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print "start time: ", time
time = ''.join(e for e in time if e.isalnum())
time = int(time)
starttime = time

for i in range(0, 1000):
	#while you have the same time, try to get new time
	while(time == timeprev):
		time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		time = ''.join(e for e in time if e.isalnum())
		time = int(time)
	#color the row
	print "getting row ", i
	print "currtime: ", time
	print "prevtime: ", timeprev
	for j in range(0, 100):
		out[i][j] = (time & 255, (time >> 8) & 255, (time >> 16) & 255)
	#make sure you don't keep getting the same color
	timeprev = time

time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print "end time: ", time
time = ''.join(e for e in time if e.isalnum())
endtime = int(time)

runtime = endtime - starttime
if(runtime > 60):
	print "runtime:",  runtime / 60, "minutes"
else:
	print "runtime:", endtime - starttime, " seconds"

misc.imsave('output.png', out)

