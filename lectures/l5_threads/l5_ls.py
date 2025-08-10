import multiprocessing
print (multiprocessing.cpu_count())
multiprocessing.Pool(processes=multiprocessing.cpu_count())