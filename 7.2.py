# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

avg = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    try:
    	avg += float(line[20:])
    	count += 1
    except Exception, e:
    	print "Provide number"
    	exit()

print "Average spam confidence:", avg / count    