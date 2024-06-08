#!/usr/bin/python3
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
        return False
