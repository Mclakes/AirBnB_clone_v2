#!/usr/bin/python3
<<<<<<< HEAD
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
=======
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


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
>>>>>>> ae1e29a78f5bdf2a8b3afa0c3e25cb538cff3ab0
