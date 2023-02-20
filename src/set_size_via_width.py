import obspython as obs

# NOTE: This only works with width
# right now. 

# NOTE: This is the base width, if you
# apply a scale the final dimension
# will take this bast width and multiple
# it by the scale value

#
# NOTE: This version does not take
# crops into account. See the main 
# obs-position-sources-script project
# for that


class SceneItem():
    def __init__(self, name):
        self.name = name 
        self.prep()
    
    def cleanup(self):
        obs.obs_scene_release(self.scene_obj)
        obs.obs_source_release(self.source)

    def prep(self):
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

def trigger_set_width(props, prop):
    si = SceneItem(name="Video Capture Device")
    si.set_width(1000)
    si.cleanup()

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Set Width", trigger_set_width
    )
    return props


