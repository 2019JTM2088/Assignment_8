#! /usr/bin/python3
# Python3 program to convert 
# binary to decimal 

# Function to convert 
# binary to decimal 
def binaryToDecimal(n): 
	num = n; 
	dec_value = 0; 
	
	# Initializing base 
	# value to 1, i.e 2 ^ 0 
	base = 1; 
	
	temp = num; 
	while(temp): 
		last_digit = temp % 10; 
		temp = int(temp / 10); 
		
		dec_value += last_digit * base; 
		base = base * 2; 
	return dec_value; 

# Driver Code 
print("Enter binary bit data that has to be transmitted.")

num =int(input(),2) 
binaryToDecimal(num) 




def getParity( num ): 
	parity = 0
	while num: 
		parity = ~parity 
		num = num & (num - 1) 
	return parity 

# Driver program to test getParity() 
#num = 7
print ( 
	( "odd parity" if getParity(num) else "even parity")) 




# Function to convert Decimal number 
# to Binary number 

def decimalToBinary(num): 
	return bin(num).replace("0b","") 

# Driver code 
if __name__ == '__main__': 
	print(decimalToBinary(num)) 




