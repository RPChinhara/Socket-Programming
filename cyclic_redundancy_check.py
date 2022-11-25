# Returns XOR of 'a' and 'b'
# (both of same length)
def xor(a, b):
	result = []
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')
	return ''.join(result)


# Performs Modulo-2 division
def modulo2div(dividend, divisor):
	pick = len(divisor)
	tmp = dividend[0 : pick]
	while pick < len(dividend):
		if tmp[0] == '1':
			tmp = xor(divisor, tmp) + dividend[pick]
		else:
			tmp = xor('0'*pick, tmp) + dividend[pick]
		pick += 1
	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)
	checkword = tmp
	return checkword

# Function used at the sender side to encode data by appending 
# remainder of modular division at the end of data.
def encodeData(data, key):
	l_key = len(key)
	appended_data = data + '0'*(l_key-1)
	remainder = modulo2div(appended_data, key)
	codeword = data + remainder
	print("Remainder : ", remainder)
	print("Encoded Data (Data + Remainder) : ", codeword)

# main code
data = "1010001101"
key = "110101"
encodeData(data, key)