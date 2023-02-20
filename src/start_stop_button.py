import obspython as obs

################################################
# This one works. The check for the
# stop button happens every tick which
# means that if the tick is long it could
# take a while for the stop to register.
# That could be deal with but it's not
# something I need at the moment. 
# 
# Also, one tick fires after the Stop
# button is hit. 
################################################


global running
running = False

def do_tick():
    obs.blog(300, "tick")
    if running == False:
        obs.remove_current_callback()

def start(props, prop):
    obs.blog(300, "Starting Test")
    global running 
    running = True
    obs.timer_add(do_tick, 400)

def stop(props, prop):
    obs.blog(300, "Stopping Test")
    global running 
    running = False

def script_description():
    return "A basic set of start/stop buttons for controlling a script"

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "start_button", "Start", start
    )

    obs.obs_properties_add_button(
        props, "stop_button", "Stop", stop
    )

    return props


