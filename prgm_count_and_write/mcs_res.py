import os
import time
import datetime
def iter_count(file_name):
    from itertools import (takewhile, repeat)
    buffer = 1024 * 1024
    with open(file_name) as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)

def nowTime():
    return int(round(time.time() * 1000))
print(os.getcwd())
des_dir = os.getcwd()+"\\MCS_Matrix\\"
print(des_dir)
matrixfiles = os.listdir(des_dir)

with open(des_dir+"mhs_clock_rows_res.txt", 'w') as fcr:#python write fcr == file_clock_rows
    for fname in matrixfiles:
        if "_res" in fname:
            continue
        abs_fname = des_dir+fname
        print(abs_fname)
        
        # begin_time = nowTime()
        '''
        the first os invoke is only to write |M_matrix.txt|2.3700|    | to "mhs_clock_res.txt"
        '''
        os.system("mhs2_clock.exe -i "+des_dir+fname) #write to "mhs_clock_res.txt"

        '''
        the second os invoke is only to get "_Matrix_res.txt" rows and make injunction with "|file|clock| |
        '''
        des_file = abs_fname[0:-4]+"_res.txt"

        os.system("mhs2_origin.exe -i "+des_dir+fname+" -o "+des_file)
        # read from "mhs_clock_res.txt"
        with open(des_dir+"mhs_clock_res.txt", 'r') as fc:
            file_clock = fc.readline()
            #str injunction
            fcr.write(file_clock+str(iter_count(des_file)-1)+'\n')

        # print(step_time)
        # write total format: MSC_2_7.txt 0.2300 408
        # fcr.write(fname[0:-4]+" ")
        # fcr.write(str(step_time)+" ")
        # fcr.write(str(iter_count(des_file)-1)+"\n")
