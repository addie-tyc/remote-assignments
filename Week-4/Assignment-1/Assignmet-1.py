import threading
from time import sleep
import timeit


def do_job(number): 
    sleep(3)
    print(f"Job {number} finished")

def main():
    for i in range(5):
        do_job_3s = threading.Thread(target=do_job, args=(i,))
        do_job_3s.start()

main()

