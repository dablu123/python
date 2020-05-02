

nums=[8,4,9,6,1]



it= iter(nums)

print(it.__next__())


############### Genrator @@@@@@@@@@@@

def topten():
    n=1

    while n <= 10:
        sq=n*n
        yield sq
        n+=1

values=topten()


for i in values:
    try:
        print(i)
    except Exception:
        print("Error occured")
    finally:
        print("Bye")