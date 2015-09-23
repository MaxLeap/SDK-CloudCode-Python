# coding: utf-8
import leapcloud
import os
import imp

Base_path = '/home/leap'
os.sys.path.append(Base_path)


def load_config():
    config_path = os.path.join(Base_path,'config.py')
    if os.path.exists(config_path):
        imp.load_source('config',config_path)

def load_hook():
    hook_path = os.path.join(Base_path,'hook')
    if os.path.exists(hook_path):
        for source in os.listdir(hook_path):
            if source.endswith('.py'):
                imp.load_source(source[:-3],os.path.join(hook_path,source))

def load_job():
    job_path = os.path.join(Base_path,'job')
    if os.path.exists(job_path):
        for source in os.listdir(job_path):
            if source.endswith('.py'):
                imp.load_source(source[:-3],os.path.join(job_path,source))

def load_function():
    function_path = os.path.join(Base_path,'function')
    if os.path.exists(function_path):
        for source in os.listdir(function_path):
            if source.endswith('.py'):
                imp.load_source(source[:-3],os.path.join(function_path,source))

load_config()
load_hook()
load_job()
load_function()