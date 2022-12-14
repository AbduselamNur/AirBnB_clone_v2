#!/usr/bin/python3
"""
Deploy archive!"""
from os.path import exists
from fabric.api import env, put, run


env.hosts = ["34.239.207.57", "100.26.216.20"]


def do_deploy(archive_path):
    """a Fabric script (based on the file 1-pack_web_static.py)
       that distributes an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        archive_file = archive_path.split("/")[-1]
        archive_no_ext = archive_file.replace(".tgz", "")
        remote_path = "/tmp/{}".format(archive_file)
        remote_folder = "/data/web_static/releases/{}".format(archive_no_ext)
        put(archive_path, remote_path)
        run("mkdir -p {}".format(remote_folder))
        run("tar -xzf {} -C {}".format(remote_path, remote_folder))

        run("rm -f {}".format(remote_path))
        run("rm -f {}".format("/data/web_static/current"))

        run("ln -s {} {}".format(remote_folder, "/data/web_static/current"))
        print("New version deployed!")

        return True
    except Exception:
        return False
