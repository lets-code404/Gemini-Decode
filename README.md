# Gemini Decode Application

Gemini Decode is a Streamlit app that extracts, summarizes, and translates text from multilingual document images using Google's Gemini model.

## What was improved
- Added robust API key validation (clean error if `GOOGLE_API_KEY` is missing).
- Removed sensitive API-key logging from startup.
- Added safer image decoding with user-friendly validation errors.
- Cached Gemini model initialization to avoid redundant setup work.
- Added default prompt fallback when users submit without custom text.
- Added loading and error states for better debugging and UX.

## Requirements
Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY="your-google-api-key"
```

## Run locally

```bash
streamlit run app.py
```

## Usage
1. Upload a `.jpg`, `.jpeg`, or `.png` document.
2. Optionally enter an instruction (for example: *"Translate to English and summarize in 5 bullets"*).
3. Click **Submit** to get Gemini's response.
