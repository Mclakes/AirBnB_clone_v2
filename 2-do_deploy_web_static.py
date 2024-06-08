#!/usr/bin/python3
<<<<<<< HEAD
# a Fabric script (based on the file `1-pack_web_static.py`) that
# distributes an archive to your web servers, using the function `do_deploy`

from fabric.api import env, put, run
# Import os for path manipulation (optional, depending on your implementation)
import os


# Define web server IPs
env.hosts = ['52.91.126.218', '54.89.178.237']


def do_deploy(archive_path):
    """
    Deploys the provided archive to web servers.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """

    if not os.path.exists(archive_path):
        print(f"Error: Archive file {archive_path} does not exist.")
        return False

    # Extract the file name and folder name from the archive path
    # Extracts the file name from the path
    file_name = os.path.basename(archive_path)
    # Removes the file extension to get the folder name
    folder_name = file_name.replace(".tgz", "")

    # Construct the folder path based on the folder name
    folder_path = "/data/web_static/releases/{}/".format(folder_name)

    try:
        # Upload archive to temporary directory
        put(archive_path, "/tmp/")

        # Create release directory
        run(f"mkdir -p {folder_path}")

        # Extract archive to the release directory
        run(f"tar -xzf /tmp/{file_name} -C {folder_path}")

        # Clean up temporary archive
        run(f"rm -rf /tmp/{file_name}")

        # Update symbolic link and directories
        # Move content to release directory
        run(f"mv {folder_path}web_static/* {folder_path}")

        # Remove empty web_static directory
        run(f"rm -rf {folder_path}web_static")

        # Delete old current link
        run("rm -rf /data/web_static/current")

        # Create new current link
        run(f"ln -sf {folder_path} /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Error deploying archive: {e}")
=======
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
>>>>>>> ae1e29a78f5bdf2a8b3afa0c3e25cb538cff3ab0
        return False
    return True