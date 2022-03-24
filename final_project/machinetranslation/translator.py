"""creating an instance of the IBM watson language translator"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ[{"apikey"}]
url = os.environ[{"url"}]

authenticator = IAMAuthenticator('AHdgFjFa4jPrE0EObvDOSrg_HAZ-ThGWptXQEi7e7Ifu')
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com")


def english_to_french(text1):
    """
    translates english text to French
    """
    french_text = language_translator.translate(source='en', text=text1,  model_id='en-fr').get_result()
    return french_text.get("translated")[0].get('translation')


def french_to_english(text1):
    """
    translates French text to english
    """
    english_text = language_translator.translate(source='fr', text=text1, model_id='fr-en').get_result()
    return english_text.get("translate")[0].get('translated')
