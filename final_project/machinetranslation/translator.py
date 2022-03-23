"""creating an instance of the IBM watson language translator"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["AHdgFjFa4jPrE0EObvDOSrg_HAZ-ThGWptXQEi7e7Ifu"]
url = os.environ[
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/8f1a183b-beee-4530-b890-26db29dcc85d']

authenticator = IAMAuthenticator('AHdgFjFa4jPrE0EObvDOSrg_HAZ-ThGWptXQEi7e7Ifu')
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com")


def english_to_french(english_text):
    """
    translates english text to French
    """
    french_text = language_translator.translate(source='en', model_id='en-fr').get_result()
    return french_text.get("translated")[0].get("translation")


def french_to_english(french_text):
    """
    translates French text to english
    """
    english_text = language_translator.translate(source='fr', model_id='fr-en').get_result()
    return english_text.get("translate")[0].get("translation")
