def dollar_to_euro(dollar_value):
	return dollar_value * 0.89 # $137 * 0.89 = 121.93 euros

def euro_to_yen(euro_value):
	return euro_value * 124.15 # e121.93 * y124.15 = 15137.6095 yenes 

####### ↓ YOUR CODE BELOW ↓ #######

euros = dollar_to_euro(137)
yenes = euro_to_yen(euros)

print(yenes)

