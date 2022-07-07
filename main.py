import requests, threading
url = "hurlhere"

data = {"datahere":True}

def do():
    while True:
        res = requests.post(url, data=data).text
        print(res)

        
threads = []
for i in range(50):
    t = threading.Thread(target=do)
    t.daemon = True
    threads.append(t)
    
for i in range(50):
    threads[i].start()
for i in range(50):
    threads[i].join()