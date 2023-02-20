# OBS Example Python Scripts

NOTE: This is a draft/scratchpad.
I've got the parts I need. Keeping
it public, but it's not cleaned up.

NOTE: These don't all have the cleanup
reference calls in them. I don't know
how critical that is for one off scripts.
Probably something to address regardless.

---

An example set of python scripts for working
with basic OBS functionality.

I'm not trying to make a full set of example.
This is just what I'm using as a scratchpad
for figuring out the parts I need.

The example use a "Test Source".

NOTE:

I'm using this to release the scene:

```python
obs.obs_scene_release(scene)
```

I'm not yet sure if anything else needs to be
released or not.

---

# Details on transform stuff here:

https://obsproject.com/docs/reference-scenes.html#c.obs_transform_info

https://github.com/upgradeQ/OBS-Studio-Python-Scripting-Cheatsheet-obspython-Examples-of-API/blob/master/src/print_all_source_settings_and_filter_names.py
