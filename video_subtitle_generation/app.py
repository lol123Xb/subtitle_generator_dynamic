import threading
import queue
from screen_capture import start_capture
from ocr_reader import start_ocr
from translator import start_translation
from overlay import SubtitleOverlay


image_queue = queue.Queue()
text_queue = queue.Queue()
overlay_queue = queue.Queue()


def start_background(region):
    threading.Thread(target=start_capture, args=(region, image_queue), daemon=True).start()
    threading.Thread(target=start_ocr, args=(image_queue, text_queue), daemon=True).start()
    threading.Thread(target=start_translation, args=(text_queue, overlay_queue), daemon=True).start()


if __name__ == "__main__":
    # screen size 1920x1080, capture region for subtitles, adjust as needed
    region = {
        "top": 830,
        "left": 500,
        "width": 920,
        "height": 100,
    }

    start_background(region)

    overlay = SubtitleOverlay(overlay_queue)
    overlay.run()
