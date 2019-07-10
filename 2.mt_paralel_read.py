from threading import Thread
import pandas as pd
import time as tm

start = tm.time()

df = pd.read_csv('sample_kesehatan.csv')

def Calc_PSN(number):
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

if __name__ == '__main__':
    #Menentukan banyak pasien yang dihitung
    psn = 1000
    
    t1 = Thread(target=Calc_PSN, args=(psn,))
    t2 = Thread(target=Calc_YT, args=(psn,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print ('MultiThread Done in :', tm.time()-start, ' Seconds')

end = tm.time()
dur = end-start

if dur<60:
    print('Multithread Done in :',dur,'Seconds')
elif dur>60 and dur<3600:
    dur /= 60
    print('Multithread Done in :',dur,'Minutes')
else:
    dur /= (60*60)
    print('Multithread Done in :',dur, 'Hours')
