# One Time Pad Codec

[One-time pad encryption](http://en.wikipedia.org/wiki/One-time_pad) is a theoretically uncrackable encryption method based on a shared random key.

This codec can be used in three ways:

 1. Include the class in your own code (onetime.py).
 2. Use the codec from the command line (onetime.py).
 3. Use the GUI (onetime_gui.py)

# Running from the command line

```sh
# Encode a string
$ python onetime.py enc 'Hello, World!' 'my secret key'
> TC#Ds!}0H}vh

# Decode a string
$ python onetime.py dec 'TC#Ds!}0H}vh' 'my secret key'
> Hello, World!

# Provide a custom alphabet
$ python onetime.py enc 'Hello, World!' 'my secret key' 'abcdefghijklmnopqrstuvwxyz1234567890'
> m3l4scre8rvhy
```

# Running the GUI

```sh
$ python onetime_gui.py
```

# Creating windows exe

To create an EXE first make sure python is in your PATH environment variable.

Then install py2exe.

Finally put this in your command line:

    python onetime_gui.py py2exe

The exe and accompanying files will be created in /dist.
