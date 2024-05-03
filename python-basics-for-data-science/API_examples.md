
#you will need the following library 
!pip install ibm_watson wget
#you will need the following library 
!pip install ibm_watson wget
Speech to Text

20 cells hidden
Language Translator
First we import LanguageTranslatorV3 from ibm_watson. For more information on the API click here

from ibm_watson import LanguageTranslatorV3
The service endpoint is based on the location of the service instance, we store the information in the variable URL. To find out which URL to use, view the service credentials.

url_lt=''
You require an API key, and you can obtain the key on the Dashboard.

apikey_lt=''
API requests require a version parameter that takes a date in the format version=YYYY-MM-DD. This lab describes the current version of Language Translator, 2018-05-01

version_lt='2018-05-01'
we create a Language Translator object language_translator:

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator
We can get a Lists the languages that the service can identify. The method Returns the language code. For example English (en) to Spanis (es) and name of each language.

from pandas import json_normalize
​
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
We can use the method translate. This will translate the text. The parameter text is the text, Model_id is the type of model we would like to use use we use list the language. In this case, we set it to 'en-es' or English to Spanish. We get a Detailed Response object translation_response

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response
The result is a dictionary.

translation=translation_response.get_result()
translation
We can obtain the actual translation as a string as follows:

spanish_translation =translation['translations'][0]['translation']
spanish_translation 
We can translate back to English

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
We can obtain the actual translation as a string as follows:

translation_eng=translation_new['translations'][0]['translation']
translation_eng
