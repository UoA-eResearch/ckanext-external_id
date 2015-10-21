.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/neon-ninja/ckanext-external_id.svg?branch=master
    :target: https://travis-ci.org/neon-ninja/ckanext-external_id

.. image:: https://coveralls.io/repos/neon-ninja/ckanext-external_id/badge.svg
  :target: https://coveralls.io/r/neon-ninja/ckanext-external_id

.. image:: https://pypip.in/download/ckanext-external_id/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-external_id/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-external_id/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-external_id/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-external_id/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-external_id/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-external_id/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-external_id/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-external_id/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-external_id/
    :alt: License

=============
ckanext-external_id
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

This extension provides support for generic external IDs for datasets.
It does not provide a means to generate IDs from any specific providers,
instead if provides an interface for other plugins to implement.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-external_id:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-external_id Python package into your virtual environment::

     cd src
     git clone https://github.com/neon-ninja/ckanext-external_id.git
     cd ckanext-external_id
     python setup.py develop

3. Add ``external_id`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

