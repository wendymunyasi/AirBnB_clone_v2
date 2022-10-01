#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os.path
from fabric.api import *
from fabric.operations import run, put
import shlex


env.hosts = ['3.227.217.150', '3.95.27.202']
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes an archive to your web servers.

    Args:
        archive_path (string): path to archive

    Returns:
        Boolean: whether the archive is distributed or not
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Uncompress the archive to the folder,
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)

        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create new directory for release
        run("mkdir -p {}".format(releases_path))

        # Untar archive
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))

        # Delete the archive from the web server
        run("rm {}".format(tmp_path))

        # Move extraction to proper directory
        run("mv {}web_static/* {}".format(releases_path, releases_path))

        # Delete first copy of extraction after move
        run("rm -rf {}web_static".format(releases_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create new the symbolic link /data/web_static/current on web server,
        # linked to the new version of your code,
        # (/data/web_static/releases/<archive filename without extension>
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception:
        print("Could not deploy")
        return False
