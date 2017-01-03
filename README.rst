timers
======

This is a simple Python module that provides a command-line stopwatch and
countdown clock.

*Disclaimer:* I wrote these tools to time some basic household tasks, and
because I don't want to use my phone's stopwatch.  As a result, both tools only
provide a rough measurement of time, and **should not be used in situations**
**that require a high degree of accuracy**.

To use the stopwatch:

.. code-block:: console

   $ stopwatch
   00:00:00
   00:00:01
   00:00:02
   ...

or the countdown clock:

.. code-block:: console

   $ countdown 5m 7s
   00:05:07
   00:05:06
   00:05:05
   ...

The countdown accepts timestamps in the form `1h 2m 3s`, where spacing and
case are both optional.  At the end of the countdown, it uses the ASCII bell
to get your attention.

Installation
------------

You can install these two functions using pip:

.. code-block:: console

   $ pip install -e git+ssh://git@github.com/alexwlchan/timers.git

or with `pipsi <https://github.com/mitsuhiko/pipsi>`_:

.. code-block:: console

   $ pipsi install -e git+ssh://git@github.com/alexwlchan/timers.git#egg=timers

This module runs in Python 2.7 or Python 3.3+.

License
-------

This project is licensed under the MIT license.
