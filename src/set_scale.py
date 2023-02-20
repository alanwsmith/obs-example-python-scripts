import obspython as obs

source_name = "Video Capture Device"

def get_info(props, prop):
    current_scene = obs.obs_frontend_get_current_scene()
    scene = obs.obs_scene_from_source(current_scene)
    scene_item = obs.obs_scene_find_source(scene, source_name)
    if scene_item:
        scale = obs.vec2()
        scale.x = 0.4
        scale.y = 0.4
        obs.obs_sceneitem_set_scale(scene_item, scale)
    obs.obs_scene_release(scene)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

