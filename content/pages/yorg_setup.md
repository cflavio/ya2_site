Title: Yorg's set up
Status: hidden
Save_as: pages/yorg_setup.html

Here's a short guide about installing and preparing your environment for Yorg.

* clone the repository: `git clone --recursive https://github.com/cflavio/yorg.git`
* go into the directory: `cd yorg`
* create a python2 virtualenv: `virtualenv --python=/usr/bin/python2 venv`
* activate the virtualenv: `. ./venv/bin/activate`
* install the prerequisites: `pip install panda3d SCons`
* build the required assets: `scons lang=1 images=1 tracks=1`
* launch the game: `python main.py`
