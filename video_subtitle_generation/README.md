# Real-Time Subtitle Translator

A Python application that captures subtitles from your screen, performs OCR to read source language text (e.g. Chinese), translates it to target language (e.g. English), and overlays the translation in real-time (less than 1 second with GPU acceleration).

---

## Features

- **Screen capture** of a user-selected region.
- **OCR with EasyOCR** for Simplified Chinese (`ch_sim`).
- **Translation** using Argos Translate.
- **Overlay window** for displaying English subtitles on top of other windows.

---

## Requirements

- Python 3.10+
- Packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Set your capture region in `app.py`:

    ```bash
    region = {
        "top": 830,
        "left": 500,
        "width": 920,
        "height": 100,
    }
    ```

    >[!TIP]
    >The overlay should not overlap the capture region.

2. Run the app:

    ```bash
    python app.py
    ```

## Customization

- **Overlay position and size (`overlay.py`):**
  
  ```bash
    self.app.geometry("1000x120+400+800")  # width x height + x_offset + y_offset
    ```

- **Languages:**
  
  ```bash
  reader = easyocr.Reader(lang_list=['ch_sim'])
  from_lang = "zh"
  to_lang = "en"
  ```

    >[!TIP]
    >You can add or change the languages as supported by EasyOCR and Argos Translate as needed.

## TODOs

- [ ] Option for language specific model (both OCR and translation).
- [ ] Interactive region selection for screen capture.
- [ ] Context-aware translation (e.g. using a larger context window or a more advanced translation model).
