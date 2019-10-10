# https://github.com/tiangolo/uwsgi-nginx-flask-docker
# Script that will be run before loading flask

# The default backend stabilizer is buggy
simulaqron set backend projectq
simulaqron start -f
