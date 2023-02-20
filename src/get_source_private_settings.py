import obspython as obs

# Make sure "Test Source" exists
# This is empty in my test run

def get_info(props, prop):
    source = obs.obs_get_source_by_name("Video Capture Device")
    private_settings = obs.obs_source_get_private_settings(source)
    print(obs.obs_data_get_json(private_settings))

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

