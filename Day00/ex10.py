from time import sleep, time
def ft_progress(lst):
    lst = list(lst)[1:]
    taille = len(lst)
    start = time()
    for i in lst:
        now = time()
        time_elapsed = now - start
        time_estimated = 0
        time_estimated = time_elapsed * taille / i
        print("ETA : ", end="")
        print("{:.2f}".format(time_estimated) + "s", end="")
        print("[{:>3.0f}%]".format(i * 100 / taille), end="")
        print("[{:=>{}}>{:<{}}]".format("", int((i/taille)*24), "", 24 - int((i/taille)*24)), end="")
        print("{:{}}/{}".format(i, len(str(taille)), taille ) end="")
        print("| elapsed time {:.2f}".format(time_elapsed) + "s", end="")  
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
