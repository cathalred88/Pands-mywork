outer = int(input("Please specify number of outer loops"))
inner = int(input("Please specify number of inner loops"))
for b in range(0,outer):
    print ('here is the outer loop',b)
    for x in range(0, inner):
        #k=p[x]
        print ('processing the inner loop',x)