#!/usr/bin/env python
#-*- coding:utf-8 -*-
#from ez_setup import use_setuptools
#use_setuptools()
from setuptools import setup,find_packages
import os
import os.path
import sys
import requests

def md_to_rst(from_file, to_file):
    """
    将markdown格式转换为rst格式
    @param from_file: {str} markdown文件的路径
    @param to_file: {str} rst文件的路径
    """
    response = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'rst', 'from': 'markdown'},
        files={'input_files[]': open(from_file, 'rb')}
    )

    if response.ok:
        with open(to_file, "wb") as f:
            f.write(response.content)

def get_data_files():
    data_files=[]
    for path,subdirs,files in os.walk("GouYong/share"):
        if files:
            data_files.append((os.path.join(sys.prefix,path[path.find('/')+1:]),[os.path.join(path,file) for file in files]))
    return data_files

def get_file(*paths):
    path = os.path.join(*paths)
    try:
        with open(path, 'rb') as f:
            return f.read().decode('utf8')
    except IOError:
        pass

def get_readme():
    md_to_rst("README.md", "README.rst")
    return get_file(os.path.dirname(__file__), 'README.rst')

if __name__=="__main__":
    setup(
        name = "GouYong",
        version = '0.4.6',
        packages = find_packages(),
        #include_package_data=True,
        install_requires = [
            'requests>=2.9.1',
            'PyStarDict>=0.8',
            'googletrans>=2.3.0',
            'setuptools>=40.1.0',
            'Xlib>=0.21'
        ],
        entry_points = {
            'gui_scripts':[
                    'GouYong = GouYong.src.window:main'
                ]
            },

        package_data = {
            '':['*.temp'],
            #'GouYong':['cache/*','dict/*/*'],
            },
        data_files = get_data_files(),
        #exclude_package_data = {'': ['.gitignore']},
        author = "Liyj",
        author_email = "liyujiangwork@gmail.com",
        description = "A translation software on  linux",
        long_description = get_readme(),
        license = "GPL",
        url = "https://github.com/zaixi/GouYong",
        classifiers=[
            'Natural Language :: Chinese (Simplified)',
            'Environment :: X11 Applications :: GTK',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3',
        ],
    )
