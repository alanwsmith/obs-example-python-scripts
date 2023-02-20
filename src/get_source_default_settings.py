import obspython as obs

# Make sure "Video Capture Device" exists 
# This one doesn't look different from
# the basic settings in my example

def get_info(props, prop):
    source = obs.obs_get_source_by_name("Video Capture Device")
    settings = obs.obs_source_get_settings(source)
    default_settings = obs.obs_data_get_defaults(settings)
    print(obs.obs_data_get_json(settings))

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

