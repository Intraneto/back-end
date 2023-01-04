"""
Intraneto Terminal

The original all-in-one terminal. Enhanced not only by AI, but also by human intelligence.




Text classification	assign a label to a given sequence of text
pipeline(task=“sentiment-analysis”)

Text generation	generate text that follows a given prompt
pipeline(task=“text-generation”)

Name entity recognition	assign a label to each token in a sequence (people, organization, location, etc.)
pipeline(task=“ner”)

Question answering	provide the answer to a question given some context
pipeline(task=“question-answering”)

Filling masked text	complete a text with masked tokens
pipeline(task=“fill-mask”)

Summarization	summarize a long text
pipeline(task=“summarization”)

Translation	translate a text in another language
pipeline(task=“translation_xx_to_yy”)

Feature extraction	extract the features of a text
pipeline(task=“feature-extraction”)

Text2Text generation	generate a text from a text input
pipeline(task=“text2text-generation”)

Text2Text Finetuning	generate a text from a text input and fine-tune the model on it
pipeline(task=“text2text-generation”, model=”sshleifer/tiny-gpt2”)

Zero-shot classification	assign a label to a given sequence of text without any training
pipeline(task=“zero-shot-classification”)


Text classification	assign a label to a given sequence of text
pipeline(task=“sentiment-analysis”)

Text generation	generate text that follows a given prompt
pipeline(task=“text-generation”)

Name entity recognition	assign a label to each token in a sequence (people, organization, location, etc.)
pipeline(task=“ner”)

Question answering	extract an answer from the text given some context and a question
pipeline(task=“question-answering”)

Fill-mask	predict the correct masked token in a sequence
pipeline(task=“fill-mask”)

Summarization	generate a summary of a sequence of text or document
pipeline(task=“summarization”)

Translation	translate text from one language into another
pipeline(task=“translation”)

Image classification	assign a label to an image	Computer vision
pipeline(task=“image-classification”)

Image segmentation	assign a label to each individual pixel of an image (supports semantic, panoptic, and instance segmentation)	Computer vision
pipeline(task=“image-segmentation”)

Object detection	predict the bounding boxes and classes of objects in an image	Computer vision
pipeline(task=“object-detection”)

Audio classification	assign a label to an audio file	Audio
pipeline(task=“audio-classification”)

Automatic speech recognition	extract speech from an audio file into text	Audio
pipeline(task=“automatic-speech-recognition”)

Visual question answering	given an image and a question, correctly answer a question about the image	Multimodal
pipeline(task=“vqa”)



GALACTICA is a stand-alone LM which is not instruction tuned. Because of this you need to use the correct prompts to get good results. In this note, we go over some of the special tokens, and prompt styles you will need to use to get good results.

We demonstrate some examples using the standard (6.7B) model below.

📚 Predict Citations:

🔢 Predict LaTeX:

🤔 Reasoning:

🧑‍🔬 Predict Protein Annotations:

🖱️ Free-Form Generation

❓ Question Answering

📄 Documents

📜 Summarization

💎 Entity extraction

👨‍🔬 IUPAC Name prediction



Voice commands:

# Dim the living room lights.
# Pause the Living Room speaker.
# Play [Playlist name] on [App Name].
# Play [Podcast name].
# Play [Song name] on [App Name].
# Play [Song name].
# Play [station name] on Google Play Music.
# Play some Bollywood music in the bedroom speakers.
# Play the football game on Chromecast on my TV.
# Play the latest podcast.
# Play the latest unplayed podcast.
# Set the oven to 300 degrees.
# Turn [light name] green OR Change [light name] to green.
# Turn on flashlight.
Get contact information for [Contact name].
Increase/decrease brightness.
Increase/decrease volume.
Open [App name].
Open [Website name] or Go to [website name].
Post to Facebook [Message].
Post to Google+ [Message].
Post to Twitter [Message].
Read texts from [Contact name].
Send a WhatsApp message to [contact name].. [message].
Send Email to [Contact name] Subject [your text] Message [your text].
Send text to [Contact name] saying [your text].
Set volume to [number].
Show Emails from [contact name].
Show me [Contact name] number.
Take a note.
Take a screenshot.
Take a selfie or Take a picture.
Take an audio note.
Turn on/off [Bluetooth, Wi-Fi, NFC].
Turn on/off silent mode.
Turn the thermostat temperature down to 50.
What is [Contact name] phone number?
"""
import json
import logging
import os
import random
import re
import subprocess
import sys
import threading
import wave
from asyncio import subprocess
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO

import flet
import lxml.html
import pyaudio
import speech_recognition as sr
from pyautogui import typewrite
from readability import Document
from scipy.io import wavfile

# from transformers import pipeline
from urllib3 import PoolManager

# Helper functions
_GetStringAfterMatch = lambda x, y: x.split(y)[-1].lstip()
_GetWordAfterMatch = lambda x, y: _GetStringAfterMatch(x, y).split(" ")[0]
_PWD = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
_WHITESPACE_HANDLER = lambda k: re.sub("\s+", " ", re.sub("\n+", " ", k.strip()))


def _GetAudioTranscript(r, audio):
    """Callback function for speech recognition."""
    # from queue import Queue  # Python 3 import
    # from threading import Thread
    # app._ListenMicrophoneQueue = Queue()
    # app._ListenMicrophoneQueue.put(audio)
    # audio = (
    #     app._ListenMicrophoneQueue.join()
    # )  # retrieve the next audio processing job from the main thread
    # if audio is None:
    #     break  # stop processing if the main thread is done

    # TODO: Allow to configure
    # recognize speech using Sphinx

    # try:
    #     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    # except sr.UnknownValueError:
    #     print("Sphinx could not understand audio")
    # except sr.RequestError as e:
    #     print("Sphinx error; {0}".format(e))

    # # recognize keywords using Sphinx
    # try:
    #     print('Sphinx recognition for "one two three" with different sets of keywords:')
    #     print(
    #         r.recognize_sphinx(
    #             audio, keyword_entries=[("one", 1.0), ("two", 1.0), ("three", 1.0)]
    #         )
    #     )
    #     print(
    #         r.recognize_sphinx(
    #             audio, keyword_entries=[("wan", 0.95), ("too", 1.0), ("tree", 1.0)]
    #         )
    #     )
    #     print(
    #         r.recognize_sphinx(
    #             audio, keyword_entries=[("un", 0.95), ("to", 1.0), ("tee", 1.0)]
    #         )
    #     )
    # except sr.UnknownValueError:
    #     print("Sphinx could not understand audio")
    # except sr.RequestError as e:
    #     print("Sphinx error; {0}".format(e))

    # # grammar example using Sphinx
    # try:
    #     print('Sphinx recognition for "one two three" for counting grammar:')
    #     print(r.recognize_sphinx(audio, grammar="counting.gram"))
    # except sr.UnknownValueError:
    #     print("Sphinx could not understand audio")
    # except sr.RequestError as e:
    #     print("Sphinx error; {0}".format(e))

    # try:
    #     # You can download the data here: http://download.tensorflow.org/models/speech_commands_v0.01.zip
    #     spoken = recognizer.recognize_tensorflow(
    #         audio,
    #         tensor_graph="speech_recognition/tensorflow-data/conv_actions_frozen.pb",
    #         tensor_label="speech_recognition/tensorflow-data/conv_actions_labels.txt",
    #     )
    #     print(spoken)
    # except sr.UnknownValueError:
    #     print("Tensorflow could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Tensorflow service; {0}".format(e))

    # # recognize preferred phrases using Google Cloud Speech
    # GOOGLE_CLOUD_SPEECH_CREDENTIALS = (
    #     r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
    # )
    # try:
    #     print(
    #         'Google Cloud Speech recognition for "numero" with different sets of preferred phrases:'
    #     )
    #     print(
    #         r.recognize_google_cloud(
    #             audio_fr,
    #             credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS,
    #             preferred_phrases=["noomarow"],
    #         )
    #     )
    #     print(
    #         r.recognize_google_cloud(
    #             audio_fr,
    #             credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS,
    #             preferred_phrases=["newmarrow"],
    #         )
    #     )
    # except sr.UnknownValueError:
    #     print("Google Cloud Speech could not understand audio")
    # except sr.RequestError as e:
    #     print(
    #         "Could not request results from Google Cloud Speech service; {0}".format(e)
    #     )

    # # recognize speech using Google Speech Recognition
    # try:
    #     # for testing purposes, we're just using the default API key
    #     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
    #     # instead of `r.recognize_google(audio, show_all=True)`
    #     print("Google Speech Recognition results:")
    #     pprint(
    #         r.recognize_google(audio, show_all=True)
    #     )  # pretty-print the recognition result
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print(
    #         "Could not request results from Google Speech Recognition service; {0}".format(
    #             e
    #         )
    #     )

    # # recognize speech using Google Cloud Speech
    # GOOGLE_CLOUD_SPEECH_CREDENTIALS = (
    #     r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
    # )
    # try:
    #     print("Google Cloud Speech recognition results:")
    #     pprint(
    #         r.recognize_google_cloud(
    #             audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, show_all=True
    #         )
    #     )  # pretty-print the recognition result
    # except sr.UnknownValueError:
    #     print("Google Cloud Speech could not understand audio")
    # except sr.RequestError as e:
    #     print(
    #         "Could not request results from Google Cloud Speech service; {0}".format(e)
    #     )

    # # recognize speech using Wit.ai
    # WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    # try:
    #     print("Wit.ai recognition results:")
    #     pprint(
    #         r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)
    #     )  # pretty-print the recognition result
    # except sr.UnknownValueError:
    #     print("Wit.ai could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Wit.ai service; {0}".format(e))

    # # recognize speech using Microsoft Bing Voice Recognition
    # BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    # try:
    #     print("Bing recognition results:")
    #     pprint(r.recognize_bing(audio, key=BING_KEY, show_all=True))
    # except sr.UnknownValueError:
    #     print("Microsoft Bing Voice Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print(
    #         "Could not request results from Microsoft Bing Voice Recognition service; {0}".format(
    #             e
    #         )
    #     )

    # # recognize speech using Houndify
    # HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
    # HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
    # try:
    #     print("Houndify recognition results:")
    #     pprint(
    #         r.recognize_houndify(
    #             audio,
    #             client_id=HOUNDIFY_CLIENT_ID,
    #             client_key=HOUNDIFY_CLIENT_KEY,
    #             show_all=True,
    #         )
    #     )
    # except sr.UnknownValueError:
    #     print("Houndify could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Houndify service; {0}".format(e))

    # # recognize speech using IBM Speech to Text
    # IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    # IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    # try:
    #     print("IBM Speech to Text results:")
    #     pprint(
    #         r.recognize_ibm(
    #             audio, username=IBM_USERNAME, password=IBM_PASSWORD, show_all=True
    #         )
    #     )  # pretty-print the recognition result
    # except sr.UnknownValueError:
    #     print("IBM Speech to Text could not understand audio")
    # except sr.RequestError as e:
    #     print(
    #         "Could not request results from IBM Speech to Text service; {0}".format(e)
    #     )

    # # recognize speech using Snowboy
    # SNOWBOY_MODEL = "INSERT SNOWBOY MODEL FILE HERE"  # Snowboy model files
    # try:
    #     print("Snowboy results:")
    #     pprint(r.recognize_snowboy(audio, model=SNOWBOY_MODEL, show_all=True))
    # except sr.UnknownValueError:
    #     print("Snowboy could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Snowboy service; {0}".format(e))

    # recognize speech using Whisper
    WHISPER_MODEL = "tiny"  # Whisper model files
    # Update screen with loading message
    app.query_one("#results", TextLog).write("Whisper is listening...")
    try:
        transcription = r.recognize_whisper(audio, model=WHISPER_MODEL, show_all=True)
        app.query_one("#results", TextLog).write(transcription)

        # use google for test
        # TExt to speech using macos
        subprocess.run("say " + transcription, shell=True)
        print("Whisper results:")
        pprint(transcription)
        typewrite(transcription)
        return transcription
    except sr.UnknownValueError:
        app.query_one("#results", TextLog).write("Whisper could not understand audio")
        subprocess.call("say " + "Whisper could not understand audio", shell=True)
    except Exception as e:
        app.query_one("#results", TextLog).write(
            "Could not request results from Whisper service; {0}".format(e)
        )
        subprocess.call(
            "say " + "Could not request results from Whisper service", shell=True
        )


def _GetDocumentClean(document: str, remove_html=False, summarise=False) -> str:
    """Clean a text document from markup and noise."""

    if summarise:
        document = Document(document).summary(html_partial=True)
    else:
        document = Document(document).content()
    if remove_html:
        document = re.sub(r"<[^>]*>", "", document)
    document = re.sub(r"\n", " ", document)
    document = re.sub(r"\s+", " ", document)
    document = document.strip()
    return document


def _GetImageTranscript(image):
    pytesseract.pytesseract.tesseract_cmd = "**Path to tesseract executable**"
    while True:
        cap = ImageGrab.grab(bbox=(700, 300, 1400, 900))
        image = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
        data = pytesseract.image_to_data(
            image, lang="eng", output_type=pytesseract.Output.DICT
        )
        for i in range(len(data["text"])):
            # Only output information for recognized text
            if int(data["conf"][i]) > 60:
                print(
                    f"Text: {data['text'][i]}, Coordinates: {data['left'][i]},{data['top'][i]}"
                )


def _GetManOptions(command: str) -> dict:
    # Explainshell.py
    """Get all the manual options for a command."""
    manual = _GetManPages(command)
    pattern = re.compile(r"(-[a-zA-Z0-9], --[a-zA-Z-]+)[ \t]+([^\n]*)")
    # pattern = re.compile(
    #     r"^((?:--|-|\b)[a-zA-Z-]+(?:\s*,\s*(?:--|-)?[a-zA-Z-]+)*)\s*(?:=\s*[^\s]+|\[?[^\[\]\s]+\]?|{[^}\s]+}|\s+[^\s|,]+[^\s,]*(?:\s*,\s*[^\s|,]+[^\s,]*)*)?\s*(?:\[OPTION\])?\s*(.*?)\s*$",
    #     re.DOTALL,
    # )
    options = {}
    for option, description in pattern.findall(manual):
        options[option] = description.strip()
    return options


def _GetManPage(command: str) -> str:
    """Get the manual for a command."""
    # TODO: Cache data
    try:
        manual = subprocess.check_output(
            f"man -P cat '{command}'",
            shell=True,
        ).decode("utf-8")
    except FileNotFoundError:
        manual = ""
    return manual


def _GetPipeline(checkpoint):
    """Generate code using a NLP model."""

    return pipeline(
        model=checkpoint,
        task="text-generation",
        tokenizer=checkpoint,
    )


def _GetSearchResults(query: str, engine: dict) -> list:
    """Get generic search results."""

    page = app._Http.request_encode_url("GET", engine["u"].replace("{{{s}}}", query))
    result_container = lxml.html.fromstring(page)
    # We get the results' Xpath from the engine
    # .find("div", class_="results")

    results = [result_container]
    # if result_container:
    #     result_elements = result_container.find_all("div")
    #     for result in result_elements:
    #         title_element = result.find("h3")
    #         link_element = result.find("a", title=True, rel="nofollow")
    #         if title_element and link_element:
    #             title = title_element.text.strip()
    #             link = link_element["href"]
    #             description_element = result.find("p")
    #             if description_element and len(description_element.text.strip()) > 30:
    #                 description = description_element.text.strip()
    #             else:
    #                 description = ""
    #                 results.append(
    #                     {"title": title, "link": link, "description": description}
    #                 )
    return results


def _GetSettings(settings):
    # Iterate over the sections and settings
    for section_name, section in settings.items():
        container = Container()
        # Create a label for the section
        label = Label(section_name)
        container.append(label)

        # Iterate over the settings in the section
        for setting_name, setting in section.items():
            # Create a label and input for the setting
            setting_label = Label(setting["label"])
            setting_input = Input(setting["value"])
            # container.(setting_label)
            container.append(setting_input)

            # Create a list view for the options
            options_list = ListView()
            for option in setting["options"]:
                options_list.append(ListItem(text=option))

            # When the input is clicked, show the options list
            def on_input_click(event):
                options_list.show()

            setting_input.on("click", on_input_click)

            # When an option is selected, update the input value and hide the options list
            def on_option_selected(event):
                setting_input.value = event.target.text
                options_list.hide()

            options_list.on("selected", on_option_selected)

    # Return the container widget
    return container


def _ListenFile(input: str) -> str:
    """Transcribe an audio file."""
    r = sr.Recognizer()
    with sr.AudioFile(input) as source:
        return _GetSpeech(r, r.record(source))


def _ListenMicrophone():
    """
    Listen to the user's voice and return the speech as a string.
    """

    r = sr.Recognizer()
    m = sr.Microphone(sample_rate=16000)
    with m as source:
        r.adjust_for_ambient_noise(source)
    return r.listen_in_background(m, _GetSpeech, phrase_time_limit=0.8)


def _LoadJSON(settings_file: str) -> dict:
    with open(settings_file, "r") as f:
        data = json.load(f)
    return data


def _OpenFileSearch(query: str) -> None:
    """Open the file search for the current platform."""

    if sys.platform == "darwin":
        subprocess.call(["open", "-R", query])
    elif sys.platform == "win32":
        subprocess.call(["explorer", query])
    elif sys.platform == "linux":
        subprocess.call(["xdg-open", query])
    elif sys.platform == "cygwin":
        subprocess.call(["cygstart", query])
    else:
        raise NotImplementedError("Unsupported platform")


def _ProcessSpeech(speech: str, current_actions=[]) -> str:
    print("Processing...")
    if len(speech) == 0:
        return "No speech detected"
    print(speech)
    if "typewriter" in current_actions:
        pyautogui.write(speech)
    if "i want to type" in speech.lower():
        print("Type mode: ON\n\n")
        current_actions.append("typewriter")
    elif "i don t want to type" in speech.lower():
        print("Type mode: OFF\n\n")
        current_actions.remove("typewriter")
    elif "i want to open" in speech.lower():
        print("Open app: ON")
        speech = speech.lower()
        _OpenApplication(_GetWordAfterMatch(speech, "i want to open"))
    elif "i want to find" in speech.lower():
        print("Open file search: ON")
        speech = speech.lower()
        _OpenFileSearch(_GetWordAfterMatch(speech, "i want to open"))
    elif "i want to know" in speech.lower():
        speech = speech.lower()
        subprocess.Popen(
            f"open https://www.google.com/search?q={_GetWordAfterMatch(speech, 'i want to know')}",
            shell=True,
        )
    else:
        # if "input dialog" in speech.lower():
        if "scroll down" in speech.lower():
            pyautogui.scroll(clicks=1)
    # subprocess.Popen(f"say '{speech}'", shell=True)
    if speech.startswith("run ") and len(speech.replace("run ", "")):
        subprocess.run("say", speech.split("run", 1)[1].strip(), "Right?")
        print(speech.split("run", 1)[1].strip(), "Right?")
        audio = r.listen(source, phrase_time_limit=1)
        speech = r.recognize_whisper(audio, translate=True, model="base")
        speech = speech.lower()
        if speech.startswith("yes"):
            msg = "Running command"
            print(subprocess.check_output(f"say {msg}", shell=True))
            out = subprocess.check_output(
                [speech.split("run", 1)[1].strip()], shell=True
            )
            print(out)
            print(subprocess.check_output(f"say {out}", shell=True))
    elif speech.startswith("manual pages ") and len(
        speech.replace("manual pages ", "")
    ):
        out = GetManPages(speech.split("manual pages", 1)[1].strip())
    if not out:
        out = speech


def _SaveSettingsJSON(settings_file, settings):
    with open(settings_file, "w") as f:
        json.dump(settings, f)


def _SaveSpeech(audio):
    # write audio to a WAV file
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())


def _ScreenTextLocator(pattern: str, image, click: bool = False):
    pass


def _ScreenReader():
    pass


def _UpdateSetting(settings, setting_name, new_value):
    # Find the section and setting
    for section_name, section in settings.items():
        if setting_name in section:
            # Update the setting value
            section[setting_name]["value"] = new_value
            break


def main(page: flet.Page):

    commands = [
        "Get contact information for [Contact name].",
        "Increase/decrease brightness.",
        "Increase/decrease volume.",
        "Open [App name].",
        "Open [Website name] or Go to [website name].",
        "Post to Facebook [Message].",
        "Post to Google+ [Message].",
        "Post to Twitter [Message].",
        "Read texts from [Contact name].",
        "Send a WhatsApp message to [contact name].. [message].",
        "Send Email to [Contact name] Subject [your text] Message [your text].",
        "Send text to [Contact name] saying [your text].",
        "Set volume to [number].",
        "Show Emails from [contact name].",
        "Show me [Contact name] number.",
        "Take a note.",
        "Take a screenshot.",
        "Take a selfie or Take a picture.",
        "Take an audio note.",
        "Turn on/off [Bluetooth, Wi-Fi, NFC].",
        "Turn on/off silent mode.",
        "Turn the thermostat temperature down to 50.",
        "What is [Contact name] phone number?",
    ]

    def textbox_changed(string):
        str_lower = string.control.value.lower()
        list_view.controls = (
            [list_items.get(n) for n in commands if str_lower in n.lower()]
            if str_lower
            else []
        )
        page.update()

    # STARTUP AUDIO
    _STARTUP_AUDIO_DIR = os.path.join(_PWD, "assets", "audio", "startup")
    _STARTUP_AUDIO_FILES = os.listdir(_STARTUP_AUDIO_DIR)
    _STARTUP_AUDIO_FILE = random.choice(_STARTUP_AUDIO_FILES)
    audio1 = flet.Audio(
        os.path.join(_STARTUP_AUDIO_DIR, _STARTUP_AUDIO_FILE), autoplay=True
    )
    page.overlay.append(audio1)
    audio1.play()
    page.update()

    _Settings = _LoadJSON(f"{_PWD}/data/settings.json")
    _DefaultPrompt = "facebook/galactica-125m"
    _ShellCommands = []
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.isdir(path):
            _ShellCommands += os.listdir(path)
    # commands += list(set(_ShellCommands))

    # Instant Answers
    _SearchEngines = _LoadJSON(f"{_PWD}/data/search-engines.json")
    _SearchBangs = [x["t"] for x in _SearchEngines]
    # commands += list(set(_SearchBangs))

    list_items = {
        name: flet.ListTile(
            title=flet.Text(name),
            leading=flet.Icon(flet.icons.ACCESSIBILITY),
            # on_click=lambda e: text_field.set_value("aaaa"),
        )
        for name in commands
    }

    text_field = flet.TextField(
        label="Smart prompt:",
        on_change=textbox_changed,
        autofocus=True,
        min_lines=3,
        shift_enter=True,
        max_lines=16,
        helper_text=f"AI Cloud: Disabled | AI Model: `{_DefaultPrompt}` | AI Training: Disabled",
    )
    list_view = flet.ListView(expand=1, spacing=10, padding=20)

    return flet.Column(
        [
            flet.Markdown(
                "# Intraneto Terminal\n\nThe original all-in-one terminal. Enhanced not only by AI, but also by human intelligence.\n\nType a command and see the magic, or just start by typing `help` or `tutorial`."
            ),
            text_field,
            list_view,
            flet.Markdown(
                """
                # Example

                This is an example of a markdown text.
                """,
                expand=1,
                code_theme="monokai",
            ),
        ],
        expand=1,
        alignment="center",
    )


# def _ModelTrainPrototype():

#     # Load the pre-trained BERT model and tokenizer
#     model, tokenizer = _GetModelTokenizer("bert-base-uncased")

#     # Load the manual pages and technical documentation dataset
#     manual_pages = ...
#     documentation = ...

#     # Define the training parameters

#     batch_size = 32
#     num_epochs = 10

#     # Create a dataloader for the manual pages and documentation dataset

#     dataloader = DataLoader(manual_pages + documentation, batch_size=batch_size)

#     # Define a question about the manual pages
#     question = "What is the syntax for the 'ls' command?"

#     # Fine-tune the model on the manual pages and documentation dataset

#     for epoch in range(num_epochs):
#         # Loop through the dataloader
#         for batch in dataloader:
#             # Extract the input text and question from the batch
#             input_text = batch["text"]
#             question = batch["question"]

#         # Tokenize the input text and question, and create the input tensor
#         input_tensor = tokenizer.encode_plus(input_text, question, return_tensors="pt")

#         # Use the model to predict the start and end positions of the answer in the input text
#         outputs = model(**input_tensor)
#         start_pos, end_pos = torch.max(outputs.start_logits, dim=1), torch.max(
#             outputs.end_logits, dim=1
#         )

#         # Compute the loss for the predicted answer
#         loss = ...

#         # Backpropagate the loss and update the model's parameters
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     # Use the fine-tuned model to answer the question
#     outputs = model(question)
#     answer = outputs.answer

#     # Print the predicted answer
#     print(answer)

#     # Ask the user for feedback on the predicted answer
#     feedback = input("Is the predicted answer correct? (1 for YES, 0 for NO)")

#     # Update the model's parameters based on the feedback
#     if feedback == "1":
#         # Compute the loss for the correct answer
#         loss = 0
#         # Backpropagate the loss and update the model's parameters
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
#     else:
#         # Compute the loss for the incorrect answer
#         loss = 1
#         # Backpropagate the loss and update the model's parameters
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
