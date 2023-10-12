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
    try:
        local("mkdir -p versions")
        FORMAT = datetime.now()
        file = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        res = local("tar -cvzf {} web_static".format(path))
        path = "versions/{}".format(file)
        return path
    except:
        None
