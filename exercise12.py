from googletrans import Translator

translator = Translator ()
text = input ("Enter text: ")
language = input ("Enter language: ")
translate = input ("Translate to: ")

translated = translator.translate (text=text, src=language, dest=translate)
print (f"Translate text: {translated.text}")
    