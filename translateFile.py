from translate import Translator

def translateToEnglish(word)->str:
        translator= Translator(to_lang="en")
        translation = translator.translate(word)
        return translation

def translateToRomanian(word)->str:
        translator= Translator(to_lang="ro")
        translation = translator.translate(word)
        return translation