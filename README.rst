Tarkus
======

Tarkus is a plugin manager for IDA Pro, modelled after Python's pip.

Getting Started
---------------

Install Tarkus::

    pip install tarkus

Initialize::

    tarkus init "C:\Program Files (x86)\IDA 6.8"
    
And start installing plugins::

    tarkus install autostruct
    
That's it!

Command Reference
-----------------

.. code:: text

    Tarkus - IDA Plugin Manager

    Usage:
        tarkus.py install <plugin.yml>
        tarkus.py remove <plugin-name>
        tarkus.py freeze
        tarkus.py init <ida-path>
        tarkus.py repo <repo-path>
        tarkus.py update <plugin-name>
        tarkus.py new <plugin-dir> <plugin-name>
