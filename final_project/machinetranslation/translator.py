"""
Creates a Language Translator Service between French and English.
"""
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    """
    Receives a text in English and returns its French translation.
    """
    french_text = MyMemoryTranslator(source = 'en-US', target='fr-FR'
    ).translate(english_text)
    return french_text
def french_to_english(french_text):
    """
    Receives a text in French and returns its English translation.
    """
    english_text = MyMemoryTranslator(source = 'en-US',target='fr-FR'
    ).translate(french_text)
    return english_text
