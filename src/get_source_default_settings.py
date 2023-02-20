import obspython as obs

source_name = "Video Capture Device"

def get_info(props, prop):
    source = obs.obs_get_source_by_name(source_name)
    settings = obs.obs_source_get_settings(source)
    default_settings = obs.obs_data_get_defaults(settings)
    obs.blog(300, obs.obs_data_get_json(settings))

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

