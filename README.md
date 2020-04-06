# workshop_server

This project is designed to run on a Ubuntu 18.04 machine with port 80 open using nginx, supervisor, gunicorn and python 3.7(works with 3.X as far as i know). This project is intended for training and demonstraion purposes and was developed by me for use in a workshop teaching masters students at Linköpings university about server deployment.

1. clone this repo to your VPS.
2. Install base dependencies: python-3, python3-venv, supervisor, nginx
3. create a virtual environment with: python3 -m venv venv
4. Activate the venv and install the requirements in requirements.txt
5. install gunicorn with: pip install gunicorn
6. Create the database by running the init_db.py script
7. Change the **xxxx** text in configuration/server.conf to the current user on your machine (if you dont know who you are, type whoami in the terminal).
8. Copy the file configuration/server.conf into /etc/supervisor/conf.d/
9. reload supervisor with: sudo supervisorctl reload
10. copy the file configuration/server into /etc/nginx/sites-enabled/ (remove any default file created by nginx)
11. reload nginx with: sudo service nginx reload
