import os
import time 
from time import sleep
import datetime
from datetime import datetime
import serial
from serial import *
import zipfile
from zipfile import ZipFile




def get_all_file_paths(directory): 


    file_paths = [] 


    for root, directories, files in os.walk(directory): 
        for filename in files: 
            
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 

    return file_paths        

def file_store():
    
    directory = 'LOGGER DATA'

    file_paths = get_all_file_paths(directory) 

    
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 

    
    with ZipFile('my_python_files.zip','w') as zip: 
         
        for file in file_paths: 
            zip.write(file)
        

    print('All files zipped successfully!')
    


#if __name__ == "__main__": 
    



def file_rename(): 
    now= datetime.now()
    x=time_limit


      
    for filename in os.listdir("LOGGER DATA"):
        dst ='%d.dat' %x
        src = filename
        dst = dst
          
    if (filename=='new_log.dat'):
        os.rename(src, dst) 
        print("Renamed")
        
        
     
  

      

        
       
        
        

ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 9600)
counter=0


now=datetime.now()
sec=now.hour*3600+now.minute*60+now.second
print(sec)


def file_write ():
    
   
   
    file = open("new_log.dat","a")
    #while True:
    #with open("new_log.dat", "a") as im :


    i=str(ser.readline())
    i=i.replace("\n","")
    i=i.replace("\r","")
    now = datetime.now()
    print("Logging in:")
    print(str(now),i)
    file.write(str(now)+","+i+"\n")
   # j=str(ser.read(1))

    time.sleep(1)
    file.flush()

    file.close() 
 
    current_time=current.hour*3600+current.minute*60+current.second

           # print("Running")
                




    #while(current_time>time_limit):
        
  

    
 

    
        
current= datetime.now()
current_time=current.hour*3600+current.minute*60+current.second
time_limit=current.hour*3600+current.minute*60+current.second+30      
  
    
        

    


            
    
while True:  
    
    current= datetime.now()
    current_time=current.hour*3600+current.minute*60+current.second
    print("Current Time :", current_time)
    print("Time Limit :", time_limit)
    file_write()
    while (current_time>time_limit):

        
        file_rename () 
        file_store()
        for filename in os.listdir("LOGGER DATA"):
            print("Removing "+filename)
           # os.remove(filename)
            time_limit+=30  
        
        

        
        
        
        
        
        
#for filename in os.listdir("LOGGER DATA"):  
 #   print("Removing "+filename)
  #  os.remove(filename)
    
    
