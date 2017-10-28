Title: Yorg's translations
Status: hidden
Save_as: pages/yorg_translations.html

Here's a short guide about creating or modifying translations for Yorg.

This guide assumes several prerequisites. This would be the optimal path for creating the translations since you would be credited as a contributor on GitHub. Anyway, if you don't want to follow it, feel free to:

* edit the file [yorg.po](https://github.com/cflavio/yorg/tree/master/assets/locale) for your language and [send it to me]({filename}/pages/about.md) (if your language already exists);
* edit the [template file](https://github.com/cflavio/yorg/blob/master/assets/locale/it_IT/LC_MESSAGES/yorg.pot) and [send it to me]({filename}/pages/about.md) if your language doesn't exist.

Please note that the following guide doesn't pollute your system: you can safely remove everything with `rm -rf yorg` when you want.

* if your language hasn't been added already, please [contact me]({filename}/pages/about.md) so i can implement the needed modifications (and wait for them)
* clone the repository: `git clone --recursive https://github.com/cflavio/yorg.git`
* go into the directory: `cd yorg`
* checkout the branch you want to work on (one of *master*, *testing*, *stable*): `git checkout <branchname>; git submodule foreach git checkout <branchname>`
* create a python2 virtualenv: `virtualenv --python=/usr/bin/python2 venv`
* activate the virtualenv: `. ./venv/bin/activate`
* install the prerequisites: `pip install panda3d SCons`
* build the required assets: `scons lang=1 images=1 tracks=1`
* edit the file `assets/locale/<your_language>/LC_MESSAGES/yorg.po`
* rebuild the language files `scons lang=1`
* launch the game so you can test your translation: `python main.py`
* create a pull request for [Yorg](https://github.com/cflavio/yorg) which contains your `assets/locale/<your_language>/LC_MESSAGES/yorg*` files, so I can pull your modifications (and you will be added as a contributor of the project on GitHub automatically)
