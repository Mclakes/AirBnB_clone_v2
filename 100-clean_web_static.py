#!/usr/bin/python3
<<<<<<< HEAD
# a Fabric script (based on the file `3-deploy_web_static.py`) that
# deletes out-of-date archives, using the function `do_clean`

"""This module contains do_clean() function"""


from fabric.api import *


env.hosts = ['52.91.126.218', '54.89.178.237']


def do_clean(number=0):
    """Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep.
=======
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

>>>>>>> ae1e29a78f5bdf2a8b3afa0c3e25cb538cff3ab0
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
<<<<<<< HEAD

    number = int(number)

    if number == 0:
        number = 1

    local_archives = local("ls -t versions", capture=True).split()
    for archive in local_archives[number:]:
        local("rm -f versions/{}".format(archive))

    remote_archives = run("ls -t /data/web_static/releases/ |\
        grep web_static_*")
    remote_archives = remote_archives.split()
    for archive in remote_archives[number:]:
        run("rm -rf /data/web_static/releases/{}".format(archive))
=======
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
>>>>>>> ae1e29a78f5bdf2a8b3afa0c3e25cb538cff3ab0
