=============
ckanext-external_id
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

This extension provides support for generic external IDs for datasets.
It does not provide a means to generate IDs from any specific providers,
instead if provides an interface for other plugins to implement.

For an example of an external ID provider plugin, see `ckanext-googl
<https://github.com/UoA-eResearch/ckanext-googl>`_.


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
     git clone https://github.com/UoA-eResearch/ckanext-external_id.git
     cd ckanext-external_id
     python setup.py develop

3. Add ``external_id`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

