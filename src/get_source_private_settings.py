import obspython as obs

# NOTE: This didn't have anything in it
# in my test

source_name = "Video Capture Device"

def get_info(props, prop):
    source = obs.obs_get_source_by_name(source_name)
    private_settings = obs.obs_source_get_private_settings(source)
    obs.blog(300, obs.obs_data_get_json(private_settings))

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

