class Gestures(object):
    def __init__(self):
        self.prev_state = "Hold"
        self.state = "Hold"

    def recognize_gesture(self, f_x, f_y, sf_x, sf_y, palm_x, palm_y):
        """
        Function determining what gestrure was shown.

        Function sets state and previous state of the object.
        :param f_x : x position of significant finger (our case: index)
        :param f_y : y position of significant finger (our case: index)
        :param sf_x : x position of second significant finger (our case: thumb)
        :param sf_y : y position of second significant finger (our case: thumb)
        :param palm_x : x position of central palm element
        :param palm_y : y position of central palm element
        """
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
