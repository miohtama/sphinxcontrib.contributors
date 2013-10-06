.. contents::

Introduction
============

This Sphinx extension adds contributors sidebar box in your documentation.
This box shows the Github authors of the file.

Benefits

* Give the credit where the credit is due

* Show that the documentation is written by humans and it doesn't born automatically

* Encourage people to write more documentation

Examples
=========

See Plone Developer Documentation.

Installation
==============

Install the package to your virtualenv:

Limitations
=============

Currently the authors are resolved on the client-side using Github public API.
This is suitable for low traffic documentation hosting.

* Resolving authors during the documentation build time increases the build time considerably

* With large documentation builds you might hit Github API throttling threshold,
  making it difficult to do continuous documentation builds

Author
==========

Mikko Ohtamaa (`blog <https://opensourcehacker.com>`_, `Facebook <https://www.facebook.com/?q=#/pages/Open-Source-Hacker/181710458567630>`_, `Twitter <https://twitter.com/moo9000>`_, `Google+ <https://plus.google.com/u/0/103323677227728078543/>`_)
