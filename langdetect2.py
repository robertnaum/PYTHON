from langdetect import detect_langs

text_to_detect = "This is a text. \
                    Dies ist ein Text. "

detected_languages = detect_langs(text_to_detect)
for language in detected_languages:
    print(language.lang, language.prob)