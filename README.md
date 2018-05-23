# Tokyo Dark macOS Port
[![Join the chat at https://gitter.im/td_install/Lobby](https://badges.gitter.im/FrederickGeek8/td_install.svg)](https://gitter.im/td_install/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Automated [Tokyo Dark](http://www.tokyodark.com/) macOS port creation tool.
Built to run on macOS. Will not run on other platforms.

**Disclaimer:** This is a third-party modification to
[Tokyo Dark](http://www.tokyodark.com/) and is not affiliated in any way with
Cherrymochi. This does not contain any assets from
[Tokyo Dark](http://www.tokyodark.com/) and requires a Steam login which has
purchased [Tokyo Dark](http://www.tokyodark.com/) to build.

## Installation
To install, run `pip install td_install` in Terminal. This application was
developed in Python 3.6.4, but will likely work in any modern version of Python
(either of version 2 or 3).

## Usage
There are two modes that you can run `td_install` in: *Installation Mode* and
*Debugging Mode*. *Installation Mode* is the intended, default installation
method for the macOS version of [Tokyo Dark](http://www.tokyodark.com/).
However, there are some bugs in SteamCMD that makes it that if you suspect
something is wrong, perhaps *Debugging Mode* will be better.

**To install Tokyo Dark via *Installation Mode***
In Terminal, run `td_install`. The installer will will ask for your Steam
credentials as well as a installation directory at the end, so it is a
semi-interactive procedure.

**To install Tokyo Dark via *Debugging Mode***
Debugging mode will show the output of all internal commands run by `td_install`.
In order to install Tokyo Dark in this manner, run `td_debug` in Terminal.

## Notes
1. Steam typically will open a Finder window. This is completely normal,
and the window can be closed immediately if wanted. Not quite sure why this
happens.
2. Steam will sometimes crash or hang when logging in and updating. If 
Steam **crashes**, you will get notified through the Terminal immediately as
`td_install` will crash. If Steam **hangs**, then it is harder to detect 
outside of debugging mode since it will appear to just be downloading Tokyo
Dark. If you suspect that Steam is hanging (i.e. the download is taking longer
then you would expect given your internet conditions), you can check by going 
into the network tab in Activity Monitor and seeing if there is significant network
activity from `steamcmd`, which would indicate that Steam is working as expected.
