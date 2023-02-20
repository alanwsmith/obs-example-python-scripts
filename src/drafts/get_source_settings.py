import obspython as obs

# Make sure "Video Capture Device" exists 

# There's a bunch of ID stuff in here that I 
# haven't parsed yet

def get_info(props, prop):
    source = obs.obs_get_source_by_name("Video Capture Device")
    settings = obs.obs_source_get_settings(source)
    print(obs.obs_data_get_json(settings))

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

