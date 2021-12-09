import atexit
from time import perf_counter
from functools import reduce

line = "="*40


def seconds_to_str(t):
    return "%d:%02d:%02d.%03d" % \
           reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
                  [(t*1000,),1000,60,60])


def log(s, elapsed=None):
    global last
    print(line)
    print(now(), '-', s)
    end = perf_counter()
    if not elapsed:
        elapsed = seconds_to_str(end-last)
    last = end
    print("Elapsed time:", elapsed)
    print(line)


def end_log():
    end = perf_counter()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


def now():
    return seconds_to_str(perf_counter())


start = perf_counter()
last = start
atexit.register(end_log)
log("Start Program")
