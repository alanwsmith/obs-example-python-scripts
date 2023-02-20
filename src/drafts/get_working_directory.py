import obspython as obs
import os

def log_directory(props, prop):
    directory = os.getcwd()
    obs.blog(300, directory)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "get_directory_button", "Log Directory", log_directory
    )
    return props
