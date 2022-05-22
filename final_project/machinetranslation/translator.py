"""
Translator module
Translate English to French
Translate French to English
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """
    Convert English to French
    """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    print(json.dumps(french_text.get("translations")[0].get(
        "translation"), indent=2, ensure_ascii=False))
    return french_text.get("translations")[0].get("translation")


def french_to_english(french_text):
    """
    Convert French to English
    """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    print(json.dumps(english_text.get("translations")[0].get(
        "translation"), indent=2, ensure_ascii=False))
    return english_text.get("translations")[0].get("translation")


