import tracemalloc as tm
def sumofN(n):
    return (n*(n+1)/2)
tm.start()
x = sumofN(100)
print(x)
print(tm.get_tracemalloc_memory())
tm.stop()




