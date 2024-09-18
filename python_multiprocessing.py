import os, time
import multiprocessing as mp


cores = os.cpu_count()
# 8 core CPU


def cal_cube(val):
    return val*val*val

def cal_square(val):
    return val*val

if __name__ == "__main__":
    print('inside main')
    start_time = time.process_time()

    p1 = mp.Process(target=cal_cube, args=(10,))
    p2 = mp.Process(target=cal_square, args=(10,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    end_time = time.process_time()
    print('started at ',start_time, " End time ", end_time, " Elapsed time -- ",end_time-start_time)