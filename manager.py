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

    def perform(self):
        """
        Старт выполнения задачи
        """
        print(self.func(*self.args, **self.kwargs))


class TaskProcessor:
    """
    Воркер-процесс. Достает из очереди тасок таску и делает ее
    """
    def __init__(self, tasks_queue):
        """
        :param tasks_queue: Manager.Queue с объектами класса Task
        """
        self.tasks_queue = tasks_queue

    def run(self, start_new_task_time, instance_num):
        """
        Старт работы воркера
        """
        while True:
            if not self.tasks_queue.empty():
                task = self.tasks_queue.get()
                try:
                    start_new_task_time[instance_num] = time.time()
                    task.perform()
                except:
                    pass
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
        start_new_task_time = Manager().dict()
        worker_and_his_process = {}
        instance_num = 0
        while not self.tasks_queue.empty():
            if len(worker_and_his_process) < self.n_workers:
                new_worker = TaskProcessor(self.tasks_queue)
                instance_num += 1
                new_proc = Process(target=new_worker.run, args=(start_new_task_time, instance_num))
                worker_and_his_process[instance_num] = [new_proc, new_worker]
                new_proc.start()
            for key, value in start_new_task_time.items():
                if time.time() - value < self.timeout:
                    break
                else:
                    worker_and_his_process[key][0].kill()
                    p = Process(target=worker_and_his_process[key][1].run, args=(start_new_task_time, key))
                    worker_and_his_process[key][0] = p
                    p.start()
        for key, value in worker_and_his_process.items():
            value[0].join()


def f(x):
    time.sleep(2)
    return x**2
    
def f2(x):
    #time.sleep(2)
    return x**3

queue = Manager().Queue()
tasks = [Task(f, i) for i in range(7)]
tasks.append(Task(f2, 3))
for i in tasks:
    queue.put(i)
t = TaskManager(queue, 5, 1)
t.run()
