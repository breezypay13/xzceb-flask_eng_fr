"""creating an instance of the IBM watson language translator"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import IAMTokenManager
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["AHdgFjFa4jPrE0EObvDOSrg_HAZ-ThGWptXQEi7e7Ifu"]
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/8f1a183b-beee-4530-b890-26db29dcc85d']

iam_token_manager = IAMTokenManager(apikey='AHdgFjFa4jPrE0EObvDOSrg_HAZ-ThGWptXQEi7e7Ifu')
token = iam_token_manager.get_token()
language_translator = LanguageTranslatorV3 (version='2022-03-15')

language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com")

def english_to_french(english_text):
    """translates english text to french"""
    source = (english_text)
    target = ("French")
    french_text = source(target)
    return french_text

def french_to_english(french_text):
    """translates french text to english"""
    source = (french_text)
    target = ("English")
    english_text = source(target)
    return english_text
    