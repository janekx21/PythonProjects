from thread import start_new_thread
import sys

global erg
thread_num =0
NUM = 12


if not len(sys.argv) > 2:
    DEBUG = False
else:
    DEBUG = bool(sys.argv[1])

def task(inp):
    global erg
    global thread_num
    
    if True:
        tmp = "" + str(inp) + ","
    else:
        tmp = str(inp) + ","
    for i in range(0,1000000):
        2*2
    #finish(tmp)
    erg+=tmp
    thread_num-=1
    return tmp

def main():
    global NUM
    global erg
    global thread_num
    erg = ""
    thread_num = NUM
    for i in range(0,NUM):
        start_new_thread(task,(i,))


    if DEBUG:
        print("proccessing")

    last = 0
    while thread_num >0:
        if DEBUG:
            if last != thread_num:
                last = thread_num
                percent = (-(float(thread_num)/NUM)+1.0)*100.0
                print(str(percent)+"%")
        else:
            pass
    if DEBUG:
        c = raw_input("Enter Key to Contiue.")
        if c == "rev":
            NUM = int(raw_input("Num?"))
            main()
    else:
        print erg
        return


if __name__ == "__main__":
    main()
