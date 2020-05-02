


nums= [3,2,5,7,4,5,90]

evens= list(filter(lambda n: n%2==0,nums))

print(evens)

doubles= list(map(lambda n: n*2, evens))

print(doubles)