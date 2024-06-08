#!/usr/bin/python3
# a Fabric script (based on the file `3-deploy_web_static.py`) that
# deletes out-of-date archives, using the function `do_clean`

"""This module contains do_clean() function"""


from fabric.api import *


env.hosts = ['52.91.126.218', '54.89.178.237']


def do_clean(number=0):
    """Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """

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
