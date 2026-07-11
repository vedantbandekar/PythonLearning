num_pad=((1 ,2 ,3),
         (4 ,5, 6),
         ("*",0 ,"#"))

for pad in num_pad:
    for num in pad:
        print(num, end=" ")
    print()