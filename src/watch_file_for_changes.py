import obspython as obs
from os.path import getmtime, join, isfile

# This watches a file for changes. It 
# also makes sure the file exists before
# trying to get it's time stamp. The
# process starts as soon as the script
# is loaded and continues to run until
# the script is unloaded.

file_path = join(
        "D:", 
        "obs-example-python-scripts",
        "README.md"
        )

global update_time
mod_time = 0

def check_file():
    global mod_time
    obs.blog(300, "Checking file")
    if isfile(file_path) == False:
        obs.blog(300, f"- File does not exist: {file_path}")
    else:
        compare_time = getmtime(file_path)
        if mod_time != compare_time:
            mod_time = compare_time
            obs.blog(300, f"- File Changed: {mod_time}")

obs.timer_add(check_file, 1000)

def script_description():
    return """A basic file watcher. It runs as 
soon as it's loaded and continues to run
until it's unloaded"""
