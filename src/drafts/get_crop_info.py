import obspython as obs

# Make sure "Video Capture Device" exists 

def get_info(props, prop):
    print("Getting Info")
    current_scene = obs.obs_frontend_get_current_scene()
    scene = obs.obs_scene_from_source(current_scene)
    scene_item = obs.obs_scene_find_source(scene, "Video Capture Device")
    if scene_item:
        crop = obs.obs_sceneitem_crop()
        obs.obs_sceneitem_get_crop(scene_item, crop)
        print(f"Left: {crop.left}")
        print(f"Right: {crop.right}")
        print(f"Top: {crop.top}")
        print(f"Bottom: {crop.bottom}")
    obs.obs_scene_release(scene)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props
