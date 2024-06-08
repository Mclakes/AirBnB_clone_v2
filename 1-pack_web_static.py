#!/usr/bin/python3
# a Fabric script that generates a `.tgz` archive
# from the contents of the `web_static` folder
# of your AirBnB Clone repo, using the function `do_pack`

from fabric.api import local, run

import os
from datetime import datetime


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


# Run the do_pack function when called from the command line
if __name__ == "__main__":
    archive_path = do_pack()
    if archive_path:
        print(f"Packing web_static to {archive_path}")
