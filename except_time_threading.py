import traceback
import threading
import multiprocessing

import datetime
import time
def save_err(method):
    def wrapper(*args, **kwargs):
        try:
            result = method(*args, **kwargs)
            return result
        except :
            now = datetime.datetime.now()
            a = traceback.format_exc()
            f = open('errorlog.txt', 'a')
            f.write('\n'+str(now)+'\n')
            f.write(str(a))
            f.close()
    return wrapper

def helper_wrap(b,c,a = 'a'):
    helper(b,c,a= 'a')

@save_err
def helper(b, c, a = 'a'):
    make_err_process = multiprocessing.Process(target = err_printer)
    make_err_process.start()
    help_wow(1)
    print(a,b,c)

def help_wow(x):
    print('wow'+x)

def printer():
    i = 3
    while i > 0 :
        print('zzzzz')
        time.sleep(2)
        i -= 1
        
@save_err
def err_printer():
    raise ValueError

#@save_err
if __name__ == '__main__':
        
    def starter():
        h = threading.Thread(target = helper, args = (1,2))
        p = threading.Thread(target = printer)
        m1 = multiprocessing.Process(target = helper_wrap, args = (1,2))
        m2 = multiprocessing.Process(target = printer)
        m1.start()
        m2.start()
        h.start()
        p.start()

    starter()


    '''
    흐아.. 멀티프로레싱의 대상함수는 반드시 그냥 함수여야함. ~.~ 식의 함수를 넣을 경우 오류가 발생한다!
      => decorator 를쓰면 안됨!
    '''