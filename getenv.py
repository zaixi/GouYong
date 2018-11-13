#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import subprocess
from distutils.version import LooseVersion
from setup import VERSION
from shlex import quote
import json

def main():
    full_cmd = "pip list --format=json | grep GouYong"
    pypi = subprocess.run(full_cmd, shell=True, stdout=subprocess.PIPE)
    # print( pypi.stdout.decode("UTF-8"))
    datas = json.loads(pypi.stdout.decode("UTF-8"))
    for data in datas:
        if data["name"] == "GouYong":
            remote_version = data["version"]
            break
    deploy = LooseVersion(remote_version) < LooseVersion(VERSION)
    print('export DEPLOY={}'.format(quote(str(deploy))))

if __name__=="__main__":
    main()