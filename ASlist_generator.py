import os,sys
import csv
import pandas as pd
import numpy as np
import re
import random

import cv2 
import xlwt




############################################
how_many_trials = 120 # Unit * len(vector) =how_many_trials
############################################
Unit = 3 # 40 ge trial how_many_trials/(10*Unit) 
vector =       [1,2,1,2] # #s1 s0 sn ss
vector_catch = [3,4,4,4]
############################################



def exp(x,a,b,trials): # x:dist # sig:std # u:mean

    y= []
    distf = lambda z:np.exp(-z/a)/b

    y2  = distf(x)/ sum(distf(x))*trials
    for i in y2:
        y.append(int(round(i)))
        
    print(x,y)
    # figs
    #plt.subplot(2,1,1)
    #plt.scatter(x,y)

    #plt.subplot(2,1,2)
    #plt.scatter(x,distf(x))
    #plt.savefig("C:/Users/kwok/Desktop/for_me/figs_1.png")
    print('total level: %s total trial:%s' %(len(x),sum(y)))
    
    return y;
    
    

def dist_list(x2,y):
    x_a = []
    dist_onepeak = []
    switch_ornot = [] 
    catch_ornot = []
    x =[x for x in x2]
    
    for i in x:
        x_a.append(round(i,2))

    k = 0
    for i in x_a:
        for j in range(1,y[k]+1):
            dist_onepeak.append(i)
            #TBD.append(0)
            #catch_ornot.append(0)
        k = k + 1
                                
#    l = 0
#    for i in range(1,31):
#        catch_ornot[l] = 1
#        l = l + 1
                   
    list_for_csv ={'dist_onepeak':[],'catch_ornot':[],'switch_ornot':[]}
    random.shuffle(dist_onepeak)
    #random.shuffle(catch_ornot)
    #random.shuffle(TBD)
    
    #sequence1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# gagaga

    sequence1_10 =      [1,1,1,1,1,1,1,1,1,1]
    sequence0_10 =      [0,0,0,0,0,0,0,0,0,0]

    sequence_noswitch = [0,0,0,0,0,0,0,0,0,0]
    sequence_switch =   [1,2,3,4,5,0,0,0,0,0] 


    #switch_ornot = 120 /10 20 40 60 12

    switch_ornot = []
    for i in vector:
        if i ==1:
            switch_ornot = switch_ornot + sequence1_10 * Unit
        if i ==2:
            switch_ornot = switch_ornot + sequence0_10 * Unit
            


    catch_ornot = []
    for ii in vector_catch:
        if ii ==3:
            catch_ornot = catch_ornot + sequence_noswitch * Unit
        if ii ==4:
            catch_ornot = catch_ornot + sequence_switch + sequence_noswitch* (Unit-1)


#    sequence1_20 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#    sequence0_20 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    

    #sequence2 = [1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#    sequence2 = [1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    
    #sequence_start = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#    sequence_start = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    #switch_ornot = sequence1 * 4
#    switch_ornot = sequence1_20 * 2 + sequence0_20 * 2 + sequence1_20 * 2
#    catch_ornot = sequence_start + sequence2 * 2
    
    
    for i in dist_onepeak:
        list_for_csv['dist_onepeak'].append(i)
     
    for ii in catch_ornot:
        list_for_csv['catch_ornot'] = (catch_ornot)
    for i in switch_ornot:
        list_for_csv['switch_ornot'].append(switch_ornot)
    
    print 'one_peak', len(list_for_csv['dist_onepeak']),'switch_ornot',len(list_for_csv['switch_ornot']),'catch_ornot',len(list_for_csv['catch_ornot'])
    df = pd.DataFrame(list_for_csv)
    #print(df)
    return df,dist_onepeak,switch_ornot,catch_ornot;
    
    
    
    
    
    
for i in range(120,125): #days #gaga


    saved_path = 'meta_day%s_AS_120_40.xls'%(i)
    print saved_path

    #how_many_trials = 120


    #y = gasuan(np.arange(6,12,0.3), 1.5, 1.5)
    y = exp(np.arange(5.25,11.25,0.25), 2.9, 1.5,how_many_trials)

    df = dist_list(np.arange(5.25, 11.25,0.25),y) #
    #df[0].to_csv('dist_testing.csv')
    dist_onepeak = df[1]
    switch_ornot =df[2]
    catch_ornot = df[3]

    print dist_onepeak,df[2],df[3]


    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)

    _thisDir=_thisDir.replace('\\','/')

    path =  'Ppic_pool'

    print path
    file_name = os.listdir(path)


    with open("pic_list.csv","w") as csvfile: 
        
        writer = csv.writer(csvfile)
        writer.writerow(["pic_location"])
        
        for file in file_name:
            
            if file[-4:]=='jpeg':
                writer.writerow([path +'/' + file])


    data = pd.read_csv('pic_list.csv')

    train_data = np.array(data)#np.ndarray()

    tansform = train_data.tolist()#list
    print tansform

    pic_list = random.sample(tansform, how_many_trials)


    #print (type(pic_list))
    #print (pic_list)



    wb = xlwt.Workbook()
    ws = wb.add_sheet('AS_Sheet')
    ws.write(0,0,'movie_location')
    ws.write(0,1,'picture_1')
    ws.write(0,2,'picture_2')
    ws.write(0,3,'dist_onepeak')
    ws.write(0,4,'switch_ornot')
    ws.write(0,5,'catch_ornot')



    random.shuffle(pic_list)


    #print (pic_list)
    trialnumber = len(pic_list)

    print(trialnumber)


    for i in range(1,trialnumber+1):
        
        
        ws.write(i, 0, 'video_pool/' + (pic_list[10][0].split('/')[-1]).split('-')[0]+(pic_list[15][0].split('/')[-1]).split('-')[0])
        
        if switch_ornot[i-1] == 1:
            
            ws.write(i, 1, pic_list[10][0])
            ws.write(i, 2, pic_list[15][0])
        else:
            
            ws.write(i, 1, pic_list[15][0])
            ws.write(i, 2, pic_list[10][0])
        
        if i <= len(dist_onepeak):
            
            ws.write(i, 3, dist_onepeak[i-1])
            ws.write(i, 4, switch_ornot[i-1])
            ws.write(i, 5, catch_ornot[i-1])
        


    wb.save(saved_path) 




