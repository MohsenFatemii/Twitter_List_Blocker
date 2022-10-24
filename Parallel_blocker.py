from threading import Thread
from queue import Queue

# TwitterAPI library should be installed before running this program.
from TwitterAPI import TwitterAPI

'''
In order to use this script, you need to have access to twitter API.
If you don't have access to twitter API, you need to sign up from the
Following link :
https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api

After signing up in you need to create an app in twitter using this link :
https://apps.twitter.com/

Then you can use it to get API keys and use this script.
'''

api = TwitterAPI(
    # the consumer key
    consumer_key='Enter Your Consumer Key here',

    # the consumer secret key
    consumer_secret='Enter Your Consumer Secret Key here',

    # the access token key
    access_token_key='Enter Your Access Token Key here',

    # the access token secret key
    access_token_secret='Enter Your Access Token Secret Key here'
)


# In order to parallelize this code i was inspired by berkerpeksag's threadpool code.
# Source :
# https://github.com/berkerpeksag/python-playground/blob/master/threadpool.py

class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()


# This is the function that is going to be parallelized.
def block_username(username):
    '''
    This function takes a username as input, then blocks it
    in twitter.

    :param username: an string that contains the username of an account

    :return: None
    '''
    blocked = api.request('blocks/create', {'screen_name': username})
    if blocked:
        print(f"Blocked user: [ @{username} ].")


'''
The following list is the list of usernames of
accounts that you want to block.
'''
block_list = []  # list of usernames to block

pool = ThreadPool(40)
pool.map(block_username, block_list)
pool.wait_completion()
