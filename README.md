# OBS Example Python Scripts

This is a collection of prototype scripts
I put together to figure out how to
use Python scripts to control OBS.

The name of each file in the `src` directory
identifies what the script will do.

There's a bunch of draft notes in the
`README_DRAFT.md` file but they are kinda
all over the place and have not been fully
vetted and reviewed.

To use a script, go under the OBS menu:

```
Tools -> Scripts
```

Point OBS to your Python Install Path under
the "Python Settings" tab. For example, on
my windows machine it's:

```
C:/Users/alan/AppData/Local/Programs/Python/Python310
```

At press time, Python 3.11 isn't supported in OBS.
Some earler versions are, but since these are prototype
scripts I haven't check them.

Switch back to the "Scripts" tab after the Python
Install path has been set and click the plus
button to add a script. Some of them run immediately
and some add buttons into the window that let you
control them.

Click the trashcan icon with a script selected to
remove it. (This is how you stop scripts that
run automatically and don't have buttons to
control them.)

If you make changes to a script, click the reload
button beside the trash can to pick them up.
