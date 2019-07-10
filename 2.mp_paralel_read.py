import pandas as pd
import time as tm
from multiprocessing import Process

start = tm.time()

df = pd.read_csv('sample_kesehatan.csv')

def calc_PSN_25(number):
    for x in range (0,number):
        Iya = 0
        Tidak = 0
        print ('pasien -', x+1)
        for y in range (3,15):
            sample = df.iloc[number,y]
            if sample == 'Y':
                Iya += 1
            else:
                Tidak += 1
        print ('Jumlah Ya :', Iya)
        print ('Jumlah Tidak :', Tidak)
        print ('Done in :', tm.time()-start, 'Seconds')
        print ()

def calc_PSN_50(number):
    for x in range (250,number):
        Iya = 0
        Tidak = 0
        print ('pasien -', x+1)
        for y in range (3,15):
            sample = df.iloc[number,y]
            if sample == 'Y':
                Iya += 1
            else:
                Tidak += 1
        print ('Jumlah Ya :', Iya)
        print ('Jumlah Tidak :', Tidak)
        print ('Done in :', tm.time()-start, 'Seconds')
        print ()

def calc_PSN_75(number):
    for x in range (500,number):
        Iya = 0
        Tidak = 0
        print ('pasien -', x+1)
        for y in range (3,15):
            sample = df.iloc[number,y]
            if sample == 'Y':
                Iya += 1
            else:
                Tidak += 1
        print ('Jumlah Ya :', Iya)
        print ('Jumlah Tidak :', Tidak)
        print ('Done in :', tm.time()-start, 'Seconds')
        print ()

def calc_PSN_100(number):
    for x in range (750,number):
        Iya = 0
        Tidak = 0
        print ('pasien -', x+1)
        for y in range (3,15):
            sample = df.iloc[number,y]
            if sample == 'Y':
                Iya += 1
            else:
                Tidak += 1
        print ('Jumlah Ya :', Iya)
        print ('Jumlah Tidak :', Tidak)
        print ('Done in :', tm.time()-start, 'Seconds')
        print ()

def calc_YT(number):
    Total_Y = 0
    Total_T = 0
    for x in range (0,number):
        for y in range (3,15):
            sample = df.iloc[x,y]
            if sample == 'Y':
                Total_Y += 1
            else:
                Total_T += 1
    print ('Kloter-1 (500)')
    print ('Total Ya :', Total_Y)
    print ('Total Tidak :', Total_T)
    print ('Done in :', tm.time()-start, 'Seconds')
    print ()

if __name__ == '__main__':
    #Menentukan banyak pasien yang dihitung
    kl1 = 250
    kl2 = 500
    kl3 = 750
    kl4 = 1000
    cr_YT = kl4

    mp1 = Process(target=calc_PSN_25, args=(kl1,))
    mp2 = Process(target=calc_PSN_50, args=(kl2,))
    mp3 = Process(target=calc_PSN_75, args=(kl3,))
    mp4 = Process(target=calc_PSN_100, args=(kl4,))
    mp5 = Process(target=calc_YT, args=(cr_YT,))
    
    mp1.start()
    mp2.start()
    mp3.start()
    mp4.start()
    mp5.start()

    mp1.join()
    mp2.join()
    mp3.join()
    mp4.join()
    mp5.join()
    
    print ('MultiProcessing Done in :', tm.time()-start, ' Seconds')

end = tm.time()
dur = end-start

if dur<60:
    print('MultiProcessing Done in :',dur,'Seconds')
elif dur>60 and dur<3600:
    dur /= 60
    print('MultiProcessing Done in :',dur,'Minutes')
else:
    dur /= (60*60)
    print('MultiProcessing Done in :',dur, 'Hours')
