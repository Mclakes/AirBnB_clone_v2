#!/usr/bin/python3
# Write a Fabric script (based on the file `2-do_deploy_web_static.py`)
# that creates and distributes an archive to your web servers,
# using the function `deploy`

"""This module contains do_pack() and do_deploy() functions"""

from fabric.api import *
from datetime import datetime
<<<<<<< HEAD
import os


env.hosts = ['52.91.126.218', '54.89.178.237']
=======
from os.path import exists, isdir
env.hosts = ['142.44.167.228', '144.217.246.195']
#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


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
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
>>>>>>> ae1e29a78f5bdf2a8b3afa0c3e25cb538cff3ab0


def do_pack():
    """
    Creates a .tgz archive of the web_static directory

    Returns:
        str: The path to the created archive or None if there's an error.
    """

    # Get current date and time for archive name
    now_datetime = datetime.now()
    archive_name = f"web_static_{now_datetime.strftime('%Y%m%d%H%M%S')}.tgz"

    # Create versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create the archive using tar
    try:
        local(f"tar -cvzf versions/{archive_name} web_static")
        return os.path.join("versions", archive_name)
    except Exception as e:
        print(f"Error creating archive: {e}")
        return None


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
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""

    if not hasattr(deploy, 'archive_path'):
        deploy.archive_path = do_pack()
    if not deploy.archive_path:
        return False

    return do_deploy(deploy.archive_path)


# def deploy():
#     """Creates/Archives and deploys/distributes the
#     archive (static files) to the host/web servers."""
#     archive_path = do_pack()
#     if archive_path:
#         return do_deploy(archive_path)
#     else:
#         return False
