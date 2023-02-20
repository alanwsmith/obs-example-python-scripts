import obspython as obs

def make_logs(props, prop):
    obs.blog(100, "Level 100 == LOG_ERROR")
    obs.blog(200, "Level 200 == LOG_WARNING")
    obs.blog(300, "Level 300 == LOG_INFO")
    obs.blog(400, "Level 400 == LOG_DEBUG")

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "log_button", "Make Logs", make_logs
    )
    return props
