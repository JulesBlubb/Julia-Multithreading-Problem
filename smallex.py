import threading

#def score(a,b,c,d):
#    print("score called", a,b,c,d)
#    return 1


def compute(score):
    print("Julia is calling")
    score(0.0,0.0,0.0,0.0)


def call_from_julia(score):
    print("Main is called from Julia")
    threads = list()
    for i in range(3):
        print("Main: create and start thread ", i)
        x = threading.Thread(target=compute, args=(score,))
        threads.append(x)
        x.start()

#call_from_julia(score)
