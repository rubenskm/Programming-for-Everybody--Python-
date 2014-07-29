def computepay(h,r) :
	if (h > 40) :
		value = (((h - 40) * 1.5) + 40) * r
	else :
		value = h * r
	return value

hours = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")

try:
	hours = float(hours)
	rate = float(rate)
except Exception, e:
	print "Enter a valid float Value"
	quit()
   
p = computepay(hours,rate)
print p