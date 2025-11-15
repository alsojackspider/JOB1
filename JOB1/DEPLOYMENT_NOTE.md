Render deployment notes
======================

If Render can't find `requirements.txt`, use the debug script or set the Build Command to reference the `job1` folder.

- Recommended Build Command (in Render UI):

  `bash render-build.sh`

  This script prints the working directory and lists files, then installs dependencies from `job1/requirements.txt`.

- Alternative Build Command (no script):

  `pip install -r job1/requirements.txt`

- Start Command (Render UI):

  `cd job1 && gunicorn job1.wsgi:application`

- Root Directory: leave blank (Render will clone to `/opt/render/project/src/` and the `job1/` folder will be there).

For debugging, deploy with the `bash render-build.sh` build command and check the build logs for the printed directory listing.
