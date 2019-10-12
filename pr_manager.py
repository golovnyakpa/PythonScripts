#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import time
import os


class Task:
    """
    Задача, которую надо выполнить.
    В идеале, должно быть реализовано на достаточном уровне абстракции,
    чтобы можно было выполнять "неоднотипные" задачи
    """
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.func_res = None

    def perform(self):
        """
        Старт выполнения задачи
        """
        self.func_res = self.func(*self.args, **self.kwargs)
        print(self.func_res)
        #print(self.func_res)


class TaskProcessor:
    """
    Воркер-процесс. Достает из очереди тасок таску и делает ее
    """
    def __init__(self, tasks_queue, num):
        """
        :param tasks_queue: Manager.Queue с объектами класса Task
        """
        self.tasks_queue = tasks_queue
        self.num = num

    def run(self, start_new_task_time, result_queue):
        """
        Старт работы воркера
        """
        while True:
            if self.tasks_queue.full():
                task = self.tasks_queue.get()
                try:
                    start_new_task_time[self.num] = time.time()
                    task.perform()
                    result_queue.put(task.func_res)
                    print(os.getpid())
                except:
                    result_queue.put('Exception happens :(')
            else:
                break


class TaskManager:
    """
    Мастер-процесс, который управляет воркерами
    """
    def __init__(self, tasks_queue, n_workers, timeout):
        """
        :param tasks_queue: Manager.Queue с объектами класса Task
        :param n_workers: кол-во воркеров
        :param timeout: таймаут в секундах, воркер не может работать дольше, чем timeout секунд
        """
        self.tasks_queue = tasks_queue
        self.n_workers = n_workers
        self.timeout = timeout

    def run(self):
        """
        Запускайте бычка! (с)
        """
        '''
        start_new_task_time = Manager().dict()
        worker_and_his_process = {}
        instance_num = 0
        result_queue = Manager().Queue()
        while self.tasks_queue.full():
            print('h')
            if len(worker_and_his_process) < self.n_workers:
                new_worker = TaskProcessor(self.tasks_queue, result_queue)
                instance_num += 1
                new_proc = Process(target=new_worker.run, 
                args=(start_new_task_time, instance_num, result_queue))
                worker_and_his_process[instance_num] = [new_proc, new_worker]
                new_proc.start()
            for key, value in start_new_task_time.items():
                if time.time() - value < self.timeout:
                    break
                else:
                    worker_and_his_process[key][0].kill()
                    worker_and_his_process[key][0].join()
                    p = Process(target=worker_and_his_process[key][1].run,
                    args=(start_new_task_time, key, result_queue))
                    worker_and_his_process[key][0] = p
                    p.start()
        for key, value in worker_and_his_process.items():
            value[0].join()
        answ = []
        while not result_queue.empty:
            answ.append(result_queue.get())
        return answ'''
        '''
        result_queue = Manager().Queue()
        worker_and_his_process = {}
        start_new_task_time = Manager().dict()
        for i in range(self.n_workers):
            self.tasks_queue.put('stop')
            worker = TaskProcessor(self.tasks_queue, i)
            worker_and_his_process[i] = [worker]
            new_proc = Process(target=worker.run, args=(start_new_task_time,result_queue))
            worker_and_his_process[i].append(new_proc)
            new_proc.start()
        #time.sleep(self.timeout)
        while True:
            print('here')
            for i, val in start_new_task_time.items():
                if time.time() - val < self.timeout:
                    break
                else:
                    worker_and_his_process[i][1].kill()
                    worker_and_his_process[i][1].join()
                    result_queue.put('Timeout happens')
                    worker_and_his_process[i][1] = Process(target=worker_and_his_process[i][0].run,
                                                 args=(start_new_task_time, result_queue))
                    worker_and_his_process[i][1].start()
            if all([val[1].is_alive() for val in worker_and_his_process.values()]):
                break
            
        for val in worker_and_his_process.values():
            val[1].join()
        '''
        result_queue = Manager().Queue()
        worker_and_his_process = {}
        start_work = Process(target=self.start_work, args=(worker_and_his_process, result_queue))
        start_work.start()
        start_work.join()
        answ = []
        while result_queue.full:
            answ.append(result_queue.get())
        return answ

        '''
        for i in range(self.n_workers):
            self.tasks_queue.put('stop')
            worker = TaskProcessor(self.tasks_queue, i)
            worker_and_his_process[i] = [worker]
            new_proc = Process(target=worker.run, args=(start_new_task_time,result_queue))
            worker_and_his_process[i].append(new_proc)
            new_proc.start()
        time.sleep(self.timeout)
        while True:
            for i, val in start_new_task_time.items():
                if time.time() - val < self.timeout:
                    break
                else:
                    worker_and_his_process[i][1].kill()
                    worker_and_his_process[i][1].join()
                    result_queue.put('Timeout happens')
                    worker_and_his_process[i][1] = Process(target=worker_and_his_process[i][0].run,
                                                 args=(start_new_task_time, result_queue))
                    worker_and_his_process[i][1].start()
            if all([val[1].is_alive() for val in worker_and_his_process.values()]):
                break
            
        for val in worker_and_his_process.values():
            val[1].join()
        answ = []
        while not result_queue.empty:
            el = result_queue.get()
            print(el)
            answ.append(result_queue.get())
        return answ
    '''
    def start_work(self, worker_and_his_process, result_queue):
        start_new_task_time = Manager().dict()
        for i in range(self.n_workers):
            worker = TaskProcessor(self.tasks_queue, i)
            worker_and_his_process[i] = [worker]
            new_proc = Process(target=worker.run, args=(start_new_task_time,result_queue))
            worker_and_his_process[i].append(new_proc)
            new_proc.start()
        while True:
            print('here')
            for i, val in start_new_task_time.items():
                if time.time() - val > self.timeout:
                    worker_and_his_process[i][1].kill()
                    worker_and_his_process[i][1].join()
                    result_queue.put('Timeout happens')
                    worker_and_his_process[i][1] = Process(target=worker_and_his_process[i][0].run,
                                                 args=(start_new_task_time, result_queue))
                    worker_and_his_process[i][1].start()
            if all([val[1].is_alive() for val in worker_and_his_process.values()]):
                break
        for val in worker_and_his_process.values():
            val[1].join()

def f(x):
    time.sleep(1)
    return x**2
    
def f2(x):
    #time.sleep(2)
    return x**3

queue = Manager().Queue()
tasks = [Task(f, i) for i in range(7)]
tasks.append(Task(f2, 3))
for i in tasks:
    queue.put(i)
t = TaskManager(queue, 5, 3)
print(t.run())
