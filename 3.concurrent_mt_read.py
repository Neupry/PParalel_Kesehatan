import pandas as pd
import time as tm
from concurrent.futures import ThreadPoolExecutor

df = pd.read_csv('sample_kesehatan.csv')

start = tm.time()

def Calc_PSN_50(number):
    for x in range (0,number):
        Iya = 0
        Tidak = 0
        print ('pasien -', x+1)
        for y in range (3,15):
                sample = df.iloc[x,y]
                if sample == 'Y':
                    Iya += 1
                else:
                    Tidak += 1
        print ('Jumlah Ya :', Iya)
        print ('Jumlah Tidak :', Tidak)
        print ('Done in :', tm.time()-start, 'Seconds')
        print ()


def Calc_PSN_100(number):
    for x in range (500,number):
        Iya = 0
        Tidak = 0
        print ('pasien -', x+1)
        for y in range (3,15):
                sample = df.iloc[x,y]
                if sample == 'Y':
                    Iya += 1
                else:
                    Tidak += 1
        print ('Jumlah Ya :', Iya)
        print ('Jumlah Tidak :', Tidak)
        print ('Done in :', tm.time()-start, 'Seconds')
        print ()

def Calc_YT(number):
    Total_Y = 0
    Total_T = 0
    for x in range (0,number):
        for y in range (3,15):
            sample = df.iloc[x,y]
            if sample == 'Y':
                Total_Y += 1
            else:
                Total_T += 1
    print ('Seluruh Pasien')
    print ('Total Ya :', Total_Y)
    print ('Total Tidak :', Total_T)
    print ('Done in :', tm.time()-start, 'Seconds')
    print ()

def run():
    psn1 = 500
    psn2 = 1000
    with ThreadPoolExecutor(max_workers=3) as exc:
        task1 = exc.submit(Calc_PSN_50, psn1)
        task2 = exc.submit(Calc_PSN_100, psn2)
        task3 = exc.submit(Calc_YT, psn2)
    print ('Concurrent Done in : ',tm.time()-start,' Seconds')

if __name__ == '__main__' :
    run()

end = tm.time()
dur = end-start
if dur<60:
    print("Concurrent Done in :",dur,"seconds")
elif dur>60 and dur<3600:
    dur=dur/60
    print("Concurrent Done in :",dur,"minutes")
else:
    dur=dur/(60*60)
    print("Concurrent Done in :",dur,"hours")
