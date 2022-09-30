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
        wExtension = archive_path.replace('/', ' ')
        wExtension = shlex.split(wExtension)
        wExtension = wExtension[-1]

        # Get name without extension
        noExtention = wExtension.replace('.', ' ')
        noExtention = shlex.split(noExtention)
        noExtention = noExtention[0]

        releases_path = "/data/web_static/releases/{}/".format(noExtention)
        if releases_path.failed:
            print("failed to create archive directory for release...")
            return False

        tmp_path = "/tmp/{}".format(wExtension)

        # upload the archive to the /tmp/ directory of the web server
        uploaded = put(archive_path, "/tmp/")
        if uploaded.failed:
            return False

        # Create new directory for release
        new_dir = run("mkdir -p {}".format(releases_path))
        if new_dir.failed:
            print("failed to create archive directory for relase...")
            return False

        # Untar archive
        untar = run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        if untar.failed:
            print("failed to untar archive...")
            return False

        # Delete the archive from the web server
        deleted = run("rm {}".format(tmp_path))
        if deleted.failed:
            print("failed to remove archive...")
            return False

        # Move extraction to proper directory
        mov = run("mv {}web_static/* {}".format(releases_path, releases_path))
        if mov.failed:
            print("failed to move extraction to proper directory...")
            return False

        # Delete first copy of extraction after move
        rem_fir = run("rm -rf {}web_static".format(releases_path))
        if rem_fir.failed:
            print("failed to remove first copy of extraction after move...")
            return False

        # Delete the symbolic link /data/web_static/current from the web server
        sym_old = run("rm -rf /data/web_static/current")
        if sym_old.failed:
            print("failed to clean up old release...")
            return False

        # Create new the symbolic link /data/web_static/current on web server,
        # linked to the new version of your code,
        # (/data/web_static/releases/<archive filename without extension>
        symNew = run("ln -s {} /data/web_static/current".format(releases_path))
        if symNew.failed:
            print("failed to create link to new release...")
            return False

        print("New version deployed!")
        return True

    except Exception:
        print("Could not deploy")
        return False
