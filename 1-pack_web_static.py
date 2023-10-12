#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of
AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        filename = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        local("tar -cvzf versions/{} web_static".format(filename))
        return "versions/{}".format(filename)
    except:
        return None
