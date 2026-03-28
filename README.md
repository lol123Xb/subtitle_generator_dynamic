# Real-Time Subtitle Generators

This repository contains two separate projects for generating real-time subtitles.

The aim is to solve the problem of inability to understand the content of videos due to language barriers, by providing real-time subtitles that can be translated into any language.

1. **Audio-based Subtitle Generator** (`audio_subtitle_generator`)  
   Generates subtitles by capturing system audio, transcribing speech, and displaying them as an overlay.

2. **Video-based Subtitle Generator** (`video_subtitle_generation`)  
   Generates subtitles by capturing video screen regions, performing OCR on on-screen subtitles (e.g., in Chinese), translating them, and displaying English translations as an overlay.

>
>Both projects utilize multi-threaded pipelines to ensure real-time performance and are designed to be modular for easy extension and customization.
>
>Both can run offline once the necessary models and dependencies are set up.

---

## 1. Audio-based Subtitle Generator

**Location:** `audio_subtitle_generator/`

Generates real-time subtitles from **system audio**.

### Features

- Captures system audio using FFmpeg
- Transcribes speech using Faster-Whisper
- Translates speech to English
- Displays live subtitle overlay

### Pipeline

```text
System Audio
     ↓
FFmpeg Audio Capture
     ↓
Audio Queue
     ↓
Whisper Transcription
     ↓
Text Queue
     ↓
Subtitle Overlay Window
```

## 2. Video-based Subtitle Generator

**Location:** `video_subtitle_generation/`

Generates real-time subtitles by capturing on-screen subtitles from videos, performing OCR and translation, and displaying them in an overlay.

### Features-

- Screen capture of user-selected region
- OCR using EasyOCR to extract on-screen subtitles
- Translates from any language to any language using Argos Translate
- Overlay window for live subtitles

### Pipeline-

```bash
Screen Capture
     ↓
Image Queue
     ↓
OCR (EasyOCR)
     ↓
Text Queue
     ↓
Context-aware Translation (Argos Translate)
     ↓
Overlay Queue
     ↓
Subtitle Overlay Window
```
