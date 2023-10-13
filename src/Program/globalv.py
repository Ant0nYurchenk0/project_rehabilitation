task_state= "none"
start_time = None
elapsed_time = None
total_duration = None

def set_state(new_state: str):
    global task_state
    task_state = new_state

def get_state()->str:
    global task_state
    return task_state

min_tracking_confidence= 0.5

def get_min_tracking_confidence():
    global min_tracking_confidence 
    return min_tracking_confidence

min_detection_confidence= 0.5

def get_min_detection_confidence():
    global min_detection_confidence
    return min_detection_confidence

