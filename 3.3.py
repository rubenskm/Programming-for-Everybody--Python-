#Write a program to prompt the user for a score using raw_input. Print out a letter 
#grade based on the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. 
#For the test, enter a score of 0.85.

score = raw_input("Enter you score")
try:
	score = float(score)
except Exception, e:
	print "Enter a valid float Value"
	quit()

if score >= 0.9 :
	letter = 'A';
elif score >= 0.8 :
	letter = 'B';
elif score >= 0.7 :
	letter = 'C';
elif score >= 0.6 :
	letter = 'D';
elif score < 0.6 :
	letter = 'E';

print letter