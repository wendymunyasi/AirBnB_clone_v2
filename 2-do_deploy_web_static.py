#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os.path
from fabric.api import *
from fabric.operations import run, put
from datetime import datetime
import os
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
        try:
            new_comp = archive_path.split("/")[-1]
            new_fold = ("/data/web_static/releases/" + new_comp.split(".")[0])
        except Exception:
            print("failed to get archive name from split...")
            return False

        if new_fold.failed:
            print("failed to create archive directory for release...")
            return False

        # upload the archive to the /tmp/ directory of the web server
        uploaded = put(archive_path, "/tmp/")
        if uploaded.failed:
            return False

        # Create new directory for release
        new_dir = run("sudo mkdir -p {}".format(new_fold))
        if new_dir.failed:
            print("failed to create archive directory for relase...")
            return False

        # Untar archive
        untar = run("sudo tar -xzf /tmp/{} -C {}".format(new_comp, new_fold))
        if untar.failed:
            print("failed to untar archive...")
            return False

        # Delete the archive from the web server
        result = run("sudo rm /tmp/{}".format(new_comp))
        if result.failed:
            print("failed to remove archive...")
            return False

        mov = run("sudo mv {}/web_static/* {}/".format(new_fold, new_fold))
        if mov.failed:
            print("failed to move extraction to proper directory...")
            return False

        run("sudo rm -rf {}/web_static".format(new_fold))

        # Delete the symbolic link /data/web_static/current from the web server
        del_old = run('sudo rm -rf /data/web_static/current')
        if del_old.failed:
            print("failed to clean up old release...")
            return False

        # Create new the symbolic link /data/web_static/current on web server,
        # linked to the new version of your code,
        # (/data/web_static/releases/<archive filename without extension>
        link = run("sudo ln -s {} /data/web_static/current".format(new_fold))
        if link.failed:
            print("failed to create link to new release...")
            return False
        return True

    except Exception:
        return False
