One Time Pad Codec
==================

[One-time pad encryption](http://en.wikipedia.org/wiki/One-time_pad) is a theoretically uncrackable encryption method based on a shared random key.

This codec can be used in three ways:

 1. Include the class in your own code (onetime.py).
 2. Use the codec from the command line (onetime.py).
 3. Use the GUI (onetime_gui.py)

Creating windows exe
====================

To create an EXE first make sure python is in your PATH environment variable. 

Then install py2exe.

Finally put this in your command line:

    python onetime_gui.py py2exe
    
The exe and accompanying files will be created in /dist.
