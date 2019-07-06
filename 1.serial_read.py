import pandas as pd
import time as tm

start = tm.time()

df = pd.read_csv('sample_kesehatan.csv')

#Tentukan jumlah pasien yang diperiksa
Pasien = 100
Total_Y = 0
Total_T = 0

for x in range (0,Pasien):
    Iya = 0
    Tidak = 0
    print ('pasien -', x+1)
    for y in range (3,15):
        sample = df.iloc[x,y]
        if sample == 'Y':
            Iya += 1
            Total_Y += 1
            #print ('indikator -',y-2,': Ya')
        else:
            Tidak += 1
            Total_T += 1
            #print ('indikator -',y-2,': Tidak')
    print ('Jumlah Ya :', Iya)
    print ('Jumlah Tidak :', Tidak)
    print ('Done in :', tm.time()-start, 'Seconds')
    print ()

end = tm.time()
dur = end-start

print ('Total Ya :', Total_Y)
print ('Total Tidak :', Total_T)

if dur<60:
    print('Serial Done in :',dur,'Seconds')
elif dur>60 and dur<3600:
    dur /= 60
    print('Serial Done in :',dur,'Minutes')
else:
    dur /= (60*60)
    print('Serial Done in :',dur, 'Hours')
