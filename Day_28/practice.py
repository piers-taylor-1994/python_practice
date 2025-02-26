import time

count = 65

def minutes_seconds():
    global count
    return f"{count // 60} {count - (60 * (count // 60))}"

def count_time():
    global count
    count -= 1
    return count
    
while count >= 0:
    count_time()
    print(f"{minutes_seconds()}")
    time.sleep(1)

    # if count == 60:
    #     count = 90