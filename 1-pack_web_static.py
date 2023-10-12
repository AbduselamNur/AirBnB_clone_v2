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
        now = datetime.now()
        file = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        path = "versions/{}".format(file)
        res = local("tar -cvzf {} web_static".format(path))
        return path

    except Exception as e:  # Specify the exception type
        print("An error occurred:", str(e))
        return None
