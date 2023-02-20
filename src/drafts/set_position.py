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

    def set_position(self, x, y):
        pos = obs.vec2()
        pos.x = x
        pos.y = y
        obs.obs_sceneitem_set_pos(self.item, pos)


def trigger_set_position_values(props, prop):
    si = SceneItem(name="Video Capture Device")
    si.set_position(300, 300)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Set Position", trigger_set_position_values
    )
    return props

