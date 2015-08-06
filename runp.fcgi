#!flask/bin/python
import os

from flipflop import WSGIServer
from app import app

if name == '__main__':
	WSGIServer(app).run()
