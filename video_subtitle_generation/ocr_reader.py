import easyocr


reader = easyocr.Reader(
    lang_list=['ch_sim'],   # Use 'ch_sim' for simplified Chinese, 'en' for English, etc.
    model_storage_directory='models/easyocr'
)


def start_ocr(image_queue, text_queue):
    last_text = ""

    while True:
        image = image_queue.get()

        result = reader.readtext(
            image,
            detail=0,
            paragraph=True
        )

        if not result:
            continue

        text = result[0].strip()

        if text and text != last_text:
            last_text = text
            print("OCR:", text)
            text_queue.put(text)
