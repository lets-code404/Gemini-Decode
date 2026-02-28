import io
import os
from typing import Optional

from dotenv import load_dotenv
from google.api_core import exceptions as google_exceptions
import google.generativeai as genai
from PIL import Image, UnidentifiedImageError
import streamlit as st


APP_TITLE = "Gemini Decode: Multilanguage Document Extraction by Gemini Pro"
MODEL_NAME = "gemini-1.5-flash"


@st.cache_resource(show_spinner=False)
def configure_model() -> genai.GenerativeModel:
    """Configure and return the Gemini model once per Streamlit session."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Add it to your environment or .env file."
        )

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def load_uploaded_image(uploaded_file) -> Optional[Image.Image]:
    """Safely decode an uploaded image file and return a PIL image object."""
    if uploaded_file is None:
        return None

    try:
        image_bytes = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_bytes))
        image.load()
        return image
    except (UnidentifiedImageError, OSError):
        st.error("The uploaded file is not a valid image. Please upload JPG or PNG.")
        return None


def get_response(model: genai.GenerativeModel, input_text: str, image: Image.Image) -> str:
    """Send the prompt and image to Gemini and return the response text."""
    prompt = input_text.strip() or "Extract and summarize key information from this document."
    response = model.generate_content([prompt, image])
    return getattr(response, "text", "No response text was returned by the model.")


def format_generation_error(exc: Exception) -> str:
    """Map provider exceptions to safe, user-actionable messages."""
    if isinstance(exc, google_exceptions.PermissionDenied):
        raw_message = str(exc)
        if "CONSUMER_SUSPENDED" in raw_message:
            return (
                "Your Google API key is suspended or disabled. "
                "Generate a new key in Google AI Studio, ensure billing/project access is active, "
                "then update GOOGLE_API_KEY in your .env file."
            )
        return (
            "Permission denied by Gemini API. Verify that your GOOGLE_API_KEY is valid and has "
            "access to the Generative Language API."
        )

    if isinstance(exc, google_exceptions.Unauthenticated):
        return "Authentication failed. Check GOOGLE_API_KEY in your .env file."

    if isinstance(exc, google_exceptions.ResourceExhausted):
        return "Quota exceeded. Please wait and retry or increase your Gemini API quota."

    return "The model request failed. Please try again in a moment."


st.set_page_config(page_title=APP_TITLE)
st.header(APP_TITLE)
st.caption(
    "Upload a multilingual document image and ask Gemini to extract, summarize, or translate it."
)

try:
    model = configure_model()
except RuntimeError as error:
    st.error(str(error))
    st.stop()

input_prompt = st.text_input(
    "Input prompt",
    placeholder="e.g., Translate this document to English and summarize in bullet points.",
)
uploaded_file = st.file_uploader(
    "Choose an image of the document", type=["jpg", "jpeg", "png"]
)
image = load_uploaded_image(uploaded_file)

if image is not None:
    st.image(image, caption="Uploaded image", use_container_width=True)

if st.button("Submit", type="primary"):
    if image is None:
        st.warning("Please upload a document image before submitting.")
    else:
        with st.spinner("Analyzing document..."):
            try:
                response_text = get_response(model, input_prompt, image)
            except Exception as exc:  # noqa: BLE001
                st.error(format_generation_error(exc))
            else:
                st.subheader("Bot Response")
                st.write(response_text)
