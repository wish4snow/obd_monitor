# obd_moniter
This is an OBD2 monitor made to be used with a WiFi scanner.
## Requirements
So far, this has only been tested with python3.9.
So python3.9 for now
## How to use
1. pip install from https://github.com/dailab/python-OBD-wifi **Do not use the package from pip its self! Or else the program won't work!**
2. Edit the PIDs you want to show up by changing the contents of the `user_wanted_pids` in `obd_monitor.py` if need.
3. Plug in your OBD2 scanner into your car's port.
4. Key on or turn on your car
5. Run `python3.9 obd_monitor.py`
6. You should be all set after that!

Happy OBDing!!!
