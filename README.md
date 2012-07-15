OMNMETA
=======

Omni Metadata. Metadata All The Things!

Experimental project to learn PySide and SQLAlchemy to create an app that can
store metadata on arbitrary files.

Many programs exist for media managment. Unfortunately, they don't support
many file formats (PNG, MPG, AVI).

Dev Installation
----------------
Install PySide:

Ubuntu:
	$ sudo add-apt-repository ppa:pyside
	$ sudo apt-get update
	$ sudo apt-get install python-pyside

Windows:
Install the appropriate binary from [qt-project.org](http://qt-project.org/wiki/PySide_Binaries_Windows).

OSX:
Untested. I know there are recipes for homebrew and macports.

If you're using virtualenv, you'll have to symlink PySide in. There may be a way to use `add2virtualenv` but I haven't tried.

Run omnmeta/scripts/resetdb.py to start and between migrations.

Sample Applications
-------------------
* Organize your animated gifs! find the perfect reaction + caption
* Play a random tv episode

Planned Features
----------------
* Get app working
* Thumbnails
* Read from embedded metadata
* Hierarchical tags
* Write to embedded metadata
* Bundle a Flask app
* Binaries
