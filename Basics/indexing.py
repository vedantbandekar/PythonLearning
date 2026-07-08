# indexing = accessing elements of a sequence using [] (indexing operator,) [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4]) #for start to required number
print(credit_number[5:9])
print(credit_number[5:]) #for gievn number to end
print(credit_number[-5]) #from the end of string
print(credit_number[::2]) #prints every 2nd character

last_degits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_degits}")

credit_number = credit_number[::-1]
print(credit_number)