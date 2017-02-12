# brightness
Simple command-line tool to change screen brightness, can be used in conjunction with keyboard shortcut.

HOWTO
=====

    $ git clone https://github.com/herrfz/brightness
    $ cd brightness
    $ pip install .
    
Then simply `brightness inc` and `brightness dec`.

To use as a keyboard shortcut, e.g. via `obkey`, it may be required to include in `$PATH`, or add a symlink:

    $ sudo ln -s $(which brightness) /usr/bin/brightness
    
