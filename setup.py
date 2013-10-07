from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='sphinxcontrib.contributors',
      version=version,
      description="Show document contributors on the page",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Sphinx',
      author='Mikko Ohtamaa',
      author_email='mikko@opensourcehacker.com',
      url='https://github.com/miohtama/sphinxcontrib.contributors/',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['sphinxcontrib'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'sh'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
