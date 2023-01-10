class Gestures(object):
    def __init__(self):
        self.prev_state = "Hold"
        self.state = "Hold"

    def recognize_gesture(self, f_x, f_y, sf_x, sf_y, palm_x, palm_y):
        self.prev_state = self.state
        if abs(f_x - palm_x) <= 150 and palm_y - f_y >= 150:
            self.state = "Playing"
        elif abs(f_x - palm_x) <= 150 and abs(palm_y - sf_y) >= 150:
            self.state = "Hold"
        elif f_x - palm_x <= -150 and abs(palm_y - f_y) <= 150:
            self.state = "Next"
        elif f_x - palm_x >= 150 and abs(palm_y - f_y) <= 150:
            self.state = "Previous"

        if self.prev_state != self.state:
            print(self.state)
