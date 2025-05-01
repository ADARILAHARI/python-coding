def count(n):
    i = 1
    while i <= n:
        yeild i
        i += 1

        counter = count(5)

        print(next(counter))
        print(next(counter))
        print(next(counter))
        print(next(counter))
        print(next(counter))
        print(next(counter))
        
