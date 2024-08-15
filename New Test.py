def queue_time(c):
    stop = 0
    time = 0
    def till(z):
        if z == 0:
            del c[0]
        else:
            c[0] -= 1
    while stop == 0:
        if c[0] != 0:
            time += 1
        till(c[0])
        if c == []:
            stop = 1
    return(time)
print(queue_time([3,2]))
