# workshop_server

This project is designed to run on a Ubuntu 18.04 machine with port 80 open.

1. clone this repo to your VPS.
2. Install base dependencies: python-3, python3-venv, supervisor, nginx
3. create a virtual environment with: python3 -m venv venv
4. Activate the venv and install the requirements in requirements.txt
5. install gunicorn with: pip install gunicorn
6. Change the **user** directory in configuration/server.conf to the current user directory on your machine.
7. Copy the file configuration/server.conf into /etc/supervisor/conf.d/
8. reload supervisor with: sudo supervisorctl reload
9. copy the file configuration/server into /etc/nginx/sites-enabled/ (remove any default file created by nginx)
10. reload nginx with: sudo service nginx reload