import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

lt.set_service_url(url)


def english_to_french(english_text):
    french_text = lt.translate(text = english_text, model_id = 'en-fr').get_result()
    translated_english = french_text['translations'][0]['translation']
    return translated_english

def french_to_english(french_text):
    english_text = lt.translate(text = french_text, model_id = 'fr-en').get_result()
    translated_french = english_text['translations'][0]['translation']
    return translated_french
