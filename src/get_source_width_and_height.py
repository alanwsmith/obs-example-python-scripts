import obspython as obs

# Make sure "Test Source" exists

# NOTE: the obs_source_get_width is the base width
# when the scale is at 1.0. If the scale changes
# this value *does not* change. 

def get_info(props, prop):
    source = obs.obs_get_source_by_name("Video Capture Device")
    print(obs.obs_source_get_width(source))
    print(obs.obs_source_get_height(source))
    obs.obs_source_release(source)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

