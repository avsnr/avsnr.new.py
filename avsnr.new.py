import random,time

us = "avsnrqwertyuiopasdfghjklzxcvbnm1234567890"

while True:
 
 time.sleep(0.099)
 oo = "56789"
 ne = int(''.join(random.choice(oo)for o in range(1)))
 
 email = str(''.join(random.choice(us)for o in range(ne)))
 email=email + '@gmail.com'
 print(email)
