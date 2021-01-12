import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class Waveshare75inchV2(DisplayImpl):
    def __init__(self, config):
        super(Waveshare75inchV2, self).__init__(config, 'Waveshare75inchv2')
        self._display = None

    def layout(self):
        fonts.setup(10, 9, 10, 35, 25, 9)
        self._layout['width'] = 800
        self._layout['height'] = 480
        self._layout['face'] = (0, 150)
        self._layout['name'] = (14, 80)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (76, 0)
        self._layout['uptime'] = (622, 0)
        self._layout['line1'] = [0, 53, 800, 53]
        self._layout['line2'] = [0, 420, 800, 420]
        self._layout['friend_face'] = (0, 338)
        self._layout['friend_name'] = (108, 360)
        self._layout['shakes'] = (0, 428)
        self._layout['mode'] = (724, 428)
        self._layout['status'] = {
            'pos': (352, 94),
            'font': fonts.status_font(fonts.Medium),
            'max': 72
        }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare v2 7.5 inch display")
        from pwnagotchi.ui.hw.libs.waveshare.v75inchv2.epd7in5v2 import EPD
        self._display = EPD()
        self._display.init()
        self._display.Clear()


    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.display(buf)

    def clear(self):
        self._display.Clear()
