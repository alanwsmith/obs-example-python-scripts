import obspython as obs

class SceneItem():
    def __init__(self, name):
        self.name = name 
        self.prep()
    
    def cleanup(self):
        obs.obs_scene_release(self.scene_obj)
        obs.obs_source_release(self.source)

    def prep(self):
        # TODO: Throw an error if the thing doesn't exist
        self.source = obs.obs_get_source_by_name(self.name)
        self.scene_ref = obs.obs_frontend_get_current_scene()
        self.scene_obj = obs.obs_scene_from_source(self.scene_ref)
        self.item = obs.obs_scene_find_source(self.scene_obj, self.name)
        self.crop = obs.obs_sceneitem_crop()
        self.info = obs.obs_transform_info()
        obs.obs_sceneitem_get_crop(self.item, self.crop)
        obs.obs_sceneitem_get_info(self.item, self.info)

    def width(self):
        return obs.obs_source_get_width(self.source)

    def height(self):
        return obs.obs_source_get_height(self.source)

    def set_width(self, value):
        scale_value = value / self.width() 
        scale = obs.vec2()
        scale.x = scale_value
        scale.y = scale_value
        obs.obs_sceneitem_set_scale(self.item, scale)


    def apply_crop(self):
        obs.obs_sceneitem_set_crop(self.item, self.crop)

    def crop_left(self, value):
        self.crop.left = value
        self.apply_crop()

    def crop_right(self, value):
        self.crop.right = value
        self.apply_crop()

    def crop_top(self, value):
        self.crop.top = value
        self.apply_crop()

    def crop_bottom(self, value):
        self.crop.bottom = value
        self.apply_crop()



def trigger_set_width_including_crop(props, prop):
    si = SceneItem(name="Video Capture Device")
    # si.set_width(1920)
    # si.crop_left(400)
    si.cleanup()

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Set Width", trigger_set_width_including_crop
    )
    return props


# class SceneItem():
#     def __init__(self, name):
#         self.name = name 
#         self.prep()
#     def prep(self):
#         self.scene_ref = obs.obs_frontend_get_current_scene()
#         self.scene_obj = obs.obs_scene_from_source(self.scene_ref)
#         self.item = obs.obs_scene_find_source(self.scene_obj, self.name)
#         self.crop = obs.obs_sceneitem_crop()
#         obs.obs_sceneitem_get_crop(self.item, self.crop)













    # current_scene = obs.obs_frontend_get_current_scene()
    # scene = obs.obs_scene_from_source(current_scene)
    # scene_item = obs.obs_scene_find_source(scene, "Video Capture Device")
    # if scene_item:
    #     crop = obs.obs_sceneitem_crop()
    #     obs.obs_sceneitem_get_crop(scene_item, crop)
    #     print(f"Left: {crop.left}")
    #     print(f"Right: {crop.right}")
    #     print(f"Top: {crop.top}")
    #     print(f"Bottom: {crop.bottom}")
    #     crop.left = 100
    #     print(f"Left: {crop.left}")
    #     obs.obs_sceneitem_set_crop(scene_item, crop)
    # obs.obs_scene_release(scene)




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
