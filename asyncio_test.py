"""

 While the threading module
  implements concurrency 
  through application threads 

  and multiprocessing implements 
  concurrency using system processes, 

  asyncio uses a single-threaded, 
  single-process approach in which parts of
   an application cooperate to switch tasks
    explicitly at optimal times


 Most often this context switching occurs 
 when the program would otherwise block 
 waiting to read or write data, but asyncio 
 also includes support for scheduling code 
 to run at a specific future time, to enable 
 one coroutine to wait for another to complete,
 for handling system signals, and for recognizing
 other events that may be reasons for an 
  application to change what it is working on.

 A future is a data structure representing 
 the result of work that has not been completed yet. 
 The event loop can watch for a Future object to be set to done,
 allowing one part of an application to wait 
 for another part to finish some work. 
 Besides futures, asyncio includes other 
 concurrency primitives such as locks and semaphores.



"""



import asyncio
import json
import time

def get_page(url):
	print('runing get_page...')
	page = "{'a':10,'b':20}"
	time.sleep(5)
	return page

def get_json_data(url):
	data = yield from get_page(url)
	print("hhhhh")
	return json.loads(data)

aa = get_json_data('url')
print(aa)
print('xxxxxx')