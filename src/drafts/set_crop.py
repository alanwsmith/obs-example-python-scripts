import obspython as obs

class SceneItem():
    def __init__(self, name):
        self.name = name 
        self.prep()

    def prep(self):
        self.scene_ref = obs.obs_frontend_get_current_scene()
        self.scene_obj = obs.obs_scene_from_source(self.scene_ref)
        self.item = obs.obs_scene_find_source(self.scene_obj, self.name)
        self.crop = obs.obs_sceneitem_crop()
        obs.obs_sceneitem_get_crop(self.item, self.crop)

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


def set_crop(props, prop):
    si = SceneItem(name="Video Capture Device")
    si.crop_left(300)
    si.crop_right(300)
    si.crop_top(300)
    si.crop_bottom(300)


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Set Crop", set_crop 
    )
    return props

