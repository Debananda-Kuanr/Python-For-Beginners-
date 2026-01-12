name = "Debananda"
print(name[-4:-1])#output will be 'nad' because -4 corresponds to 'n' and -1 corresponds to 'a', but is not included in the slice

print(name[:4])# Output will 'Deba'
# This is same as print(name[0:4]) because default starting index is 0
print(name[1:])# Output will be 'eabananda'
# This Output will same as print(name[1:9]) because default last index is the length of string

# Slicing With Skip Value 
word = "amazing"
print(word[1: 6: 2])# Output will be 'mzn' because it starts from index 1 to index 6 but skips every 2nd character
NumberString = "0123456789"
print(NumberString[1: 7 : 3])# output will 14 because it starts from index 1 to index 7 but skips every 3rd character