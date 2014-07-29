text = "X-DSPAM-Confidence:    0.8475";

index = text.rfind(" ")
value = text[index :]

try :
	value = float(value)
except Exception, e:
	print "not valid"

print value