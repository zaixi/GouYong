import subprocess
from distutils.version import LooseVersion
from setup import VERSION
from shlex import quote

def main():
    full_cmd = "pip list | grep GouYong | awk '{ print $2}'"
    pypi = subprocess.run(full_cmd, shell=True, stdout=subprocess.PIPE)
    remote_version = pypi.stdout.decode("UTF-8").replace("(", "").replace(")", "").replace("\n", "")
    deploy = LooseVersion(remote_version) < LooseVersion(VERSION)
    print('export DEPLOY={}'.format(quote(str(deploy))))


if __name__=="__main__":
    main()
