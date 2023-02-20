import obspython as obs

source_name = "Video Capture Device"

def get_info(props, prop):
    current_scene = obs.obs_frontend_get_current_scene()
    scene = obs.obs_scene_from_source(current_scene)
    scene_item = obs.obs_scene_find_source(scene, source_name)
    if scene_item:
        crop = obs.obs_sceneitem_crop()
        obs.obs_sceneitem_get_crop(scene_item, crop)
        obs.blog(300, f"Crop Left: {crop.left}")
        obs.blog(300, f"Crop Right: {crop.right}")
        obs.blog(300, f"Crop Top: {crop.top}")
        obs.blog(300, f"Crop Bottom: {crop.bottom}")
    obs.obs_scene_release(scene)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props
