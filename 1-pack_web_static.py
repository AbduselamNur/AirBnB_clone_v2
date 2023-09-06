#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of
AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    FORMAT = datetime.now().strftime("%Y%M%D%H%M%S")
    file = "web_static_{}.tgz".format(FORMAT)
    path = "versions/{}".format(file)
    res = "tar -cvzf {} web_static".format(path)

    if res.succeeded:
        return file
    else:
        None
