PyCon Introduction to Web and Data Scraping Tutorial
===========================================

A tutorial-based introduction to web scraping with Python. 

Virtual Env
------------

If you'd like to use virtual environments, please follow the following instructions. It is not required for the tutorial but may be helpful.

For more details on [virtual environments](http://www.doughellmann.com/projects/virtualenvwrapper/)

If you don't have virtual env wrapper and/or pip: 
    
    $ easy_install pip
    $ pip install virtualenvwrapper
    
and read the additional instructions [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)


    $ mkvirtualenv scraper_tutorial
    $ pip install -r requirements.txt


LXML and Selenium
-------------------------
You will need both [LXML](http://lxml.de/) and [Selenium](http://selenium-python.readthedocs.org/en/latest/index.html) to follow this tutorial in it's entirety.

If you are using a Mac, I would highly recommend using [Homebrew](http://brew.sh/). It will help make pip install *very easy* for you to use.
  * [Homebrew and LXML Installation](http://geekforbrains.com/how-to-install-lxml-for-python-using-homebrew-and-pip-in-3-steps)
  * [More help on Installing LXML on Mac](http://lxml.de/installation.html#installation)
  * [And additional suggestions for LXML on Mac](http://stackoverflow.com/questions/1277124/how-do-you-install-lxml-on-os-x-leopard-without-using-macports-or-fink)

If you are using Windows, it might be worth it to run this within a Linux Virtual Machine. If you are a Windows + Python guru, please follow these installation instructions. I can help as needed but I have not programmed on Windows in more than 5 years.
  * [Installing Selenium on Windows](http://selenium-python.readthedocs.org/en/latest/installation.html#detailed-instructions-for-windows-users)
  * [Installing LXML on Windows](http://lxml.de/installation.html#ms-windows)

Please reach out to me if you have any questions on getting the initial requirements set up. Thanks!


Firefox Web Browser
---------------------

Firefox comes as the default web driver for Selenium. To use Selenium easily, please [download and install Firefox](http://www.mozilla.org/en-US/firefox/new/).

Using PIP
------------

If you have never used PIP before you will need to sudo easy_install pip or brew install pip. PIP is a python package manager and it's really super so I highly advise using it!


Questions?
----------
/msg kjam on freenode or @kjam on twitter

