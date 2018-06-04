#/bin/bash

sudo /usr/local/nginx/sbin/nginx
sudo picam/./picam -o /run/shm/hls --alsadev hw:1,0&
./bouton.py&
./projet-flask/app.py


