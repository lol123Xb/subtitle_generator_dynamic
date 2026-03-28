import mss
import numpy as np
import time


CAPTURE_INTERVAL = 0.5  # Capture every 0.5 seconds

def start_capture(region, image_queue):
    with mss.mss() as sct:
        while True:
            img = sct.grab(region)
            frame = np.array(img)
            image_queue.put(frame)
            time.sleep(CAPTURE_INTERVAL)
