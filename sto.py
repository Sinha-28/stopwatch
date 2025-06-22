import time 
print("press enter to start the stopwatch")
print("and press CTRL + C to stop the stopwatch")


while True:
    try:
        input()
        start_time = time.time()
        print("stop watch started...")


    except:
        print("stop watch stopped...")
        end_time = time.time()
        print("total time: ", round(end_time-start_time,2),"seconds")
        
