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

    

    # current_scene = obs.obs_frontend_get_current_scene()
    # scene = obs.obs_scene_from_source(current_scene)
    # scene_item = obs.obs_scene_find_source(scene, "Video Capture Device")
    # if scene_item:
    #     info = obs.obs_transform_info()
    #     obs.obs_sceneitem_get_info(scene_item, info)
    #     print(f"Alignment: {info.alignment}")
    #     print(f"Bounds Alignment: {info.bounds_alignment}")
    #     print(f"Bounds Type: {info.bounds_type}")
    #     print(f"Bounds X: {info.bounds.x}")
    #     print(f"Bounds Y: {info.bounds.y}")
    #     print(f"Position X: {info.pos.x}")
    #     print(f"Position Y: {info.pos.y}")
    #     print(f"Rotation: {info.rot}")
    #     print(f"Scale X: {info.scale.x}")
    #     print(f"Scale Y: {info.scale.y}")
    # obs.obs_scene_release(scene)






    # current_scene = obs.obs_frontend_get_current_scene()
    # scene = obs.obs_scene_from_source(current_scene)
    # scene_item = obs.obs_scene_find_source(scene, "Video Capture Device")
    # if scene_item:
    #     scale = obs.vec2()
    #     scale.x = 0.6
    #     scale.y = 0.6
    #     obs.obs_sceneitem_set_scale(scene_item, scale)
    # obs.obs_scene_release(scene)







        # info = obs.obs_transform_info()
        # crop = obs.obs_sceneitem_crop()
        # obs.obs_sceneitem_get_info(scene_item, info)
        # obs.obs_sceneitem_get_crop(scene_item, crop)

    # source = obs.obs_get_source_by_name("Video Capture Device")
    # print(obs.obs_get_source_properties(source))

    # print("here")
    # NOTE: the obs_source_get_width is the base width
    # when the scale is at 1.0. If the scale changes
    # this value *does not* change. 
    # print(obs.obs_source_get_width(source))
    # print(obs.obs_source_get_height(source))

    #if scene_item:
        # print("here")
        # print(obs.obs_source_get_width(scene_item))
        # obs.obs_source_info.get_properties
        # info = obs.obs_transform_info()
        # obs.obs_sceneitem_get_info(scene_item, info)
        # print(f"Alignment: {info.alignment}")
        # print(f"Bounds Alignment: {info.bounds_alignment}")
        # print(f"Bounds Type: {info.bounds_type}")
        # print(f"Bounds X: {info.bounds.x}")
        # print(f"Bounds Y: {info.bounds.y}")
        # print(f"Position X: {info.pos.x}")
        # print(f"Position Y: {info.pos.y}")
        # print(f"Rotation: {info.rot}")
        # print(f"Scale X: {info.scale.x}")
        # print(f"Scale Y: {info.scale.y}")

    # obs.obs_scene_release(scene)
