import obspython as obs

# Make sure "Video Capture Device" exists in the current scene

def get_info(props, prop):
    print("Getting Info")
    current_scene = obs.obs_frontend_get_current_scene()
    scene = obs.obs_scene_from_source(current_scene)
    scene_item = obs.obs_scene_find_source(scene, "Video Capture Device")
    if scene_item:
        info = obs.obs_transform_info()
        obs.obs_sceneitem_get_info(scene_item, info)
        print(f"Alignment: {info.alignment}")
        print(f"Bounds Alignment: {info.bounds_alignment}")
        print(f"Bounds Type: {info.bounds_type}")
        print(f"Bounds X: {info.bounds.x}")
        print(f"Bounds Y: {info.bounds.y}")
        print(f"Position X: {info.pos.x}")
        print(f"Position Y: {info.pos.y}")
        print(f"Rotation: {info.rot}")
        print(f"Scale X: {info.scale.x}")
        print(f"Scale Y: {info.scale.y}")
    obs.obs_scene_release(scene)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Get Info", get_info 
    )
    return props

