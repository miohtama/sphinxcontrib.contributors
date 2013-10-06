.. contents::

Introduction
============

`Sphinx <http://sphinx-doc.org/>`_ is a software development documentation tool
written in `Python <http://python.org>`_. It is used by
hundreds of proejcts, of some of which you can find on
`readthedocs.org <http://readthedocs.org>`_.

``sphinxcontrib.contributors`` Sphinx extension adds contributors sidebar box in your documentation.
to show the Github authors of who wrote the documentation page.

.. image:: https://raw.github.com/miohtama/sphinxcontrib.contributors/master/docs/screenshot.png
    :width: 200

Often writing open source software documentation is a thankless task.
It is oversighted by many software developers. People who write
documentation do not get to be in limelight like rockstar developers do.
The ``sphinxcontrib.contributors`` Sphinx extension
encourages writing documentation by giving the
face time and link love for the writers
on the documentation page itself by adding a
new box to Sphinx sidebar.

Benefits

* Give the credit where the credit is due

* The process is automatic based on git history
  and there is no need to have separate contributors list

* Show that the documentation is written by humans and it doesn't born automatically

* Encourage people to write more documentation

Examples
=========

See `Plone Developer Documentation <http://developer.plone.org>`_.

Installation
==============

Install the package to your virtualenv:

    pip install sphinxcontrib.contributors

Install templates and static media files needed for  this extension to work.
`You can download the files from here <https://github.com/miohtama/sphinxcontrib.contributors/tree/master/src/sphinxcontrib/contributors>`_.
Use Github raw file view to download the file.

Add to your Sphinx **static** resource folder the following files::

    transparency.min.js
    contributors.js
    contributors.css

Add to your Sphinx **templates** folder the following files::

    contributors.html

Usage
=======

The Sphinx HTML is fitted with information of Github API URL where to get commit for a specific file.
Then a JavaScript AJAX request is used to pull the commit information. The authors are parsed from the commits.

You get a Github username as tooltip, Github profile link and Github avatar of each author.

* If there is Github username available, then the Github gravatar or identifcon is displayed with a
  link to Github profile page

* If the commiter was not a Github author, then the committer's name is displayed on a blank
  image

Limitations
=============

Currently the authors are resolved on the client-side using Github public API.
This is suitable for low traffic documentation hosting.

* Resolving authors during the documentation build time increases the build time considerably

* With large documentation builds you might hit Github API throttling threshold,
  making it difficult to do continuous documentation builds

Other
=========

The extension uses ``git`` command and Python `sh library <https://pypi.python.org/pypi/sh/>`_ to extract the Git repository information.

This project was created in the `Plone <http://plone.org>`_ `Conference 2013 <http://ploneconf.org>`_
with awesome people, many caipirinhas and a lot of fun.

Author
==========

Mikko Ohtamaa (`blog <https://opensourcehacker.com>`_, `Facebook <https://www.facebook.com/?q=#/pages/Open-Source-Hacker/181710458567630>`_, `Twitter <https://twitter.com/moo9000>`_, `Google+ <https://plus.google.com/u/0/103323677227728078543/>`_)
