import argostranslate.translate

from_lang = "zh"    # Use 'zh' for Chinese, 'en' for English, etc.
to_lang = "en"

installed_languages = argostranslate.translate.get_installed_languages()
from_ln = [l for l in installed_languages if l.code == from_lang]
to_ln = [l for l in installed_languages if l.code == to_lang]

if not installed_languages or not from_ln or not to_ln:
    import argostranslate.package
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_lang and x.to_code == to_lang, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
    installed_languages = argostranslate.translate.get_installed_languages()
    from_ln = [l for l in installed_languages if l.code == from_lang]
    to_ln = [l for l in installed_languages if l.code == to_lang]

print([(l.name, l.code) for l in installed_languages])
translation = from_ln[0].get_translation(to_ln[0])


def start_translation(text_queue, overlay_queue):
    while True:
        text = text_queue.get()

        translated = translation.translate(text)

        print("Translated:", translated)

        overlay_queue.put(translated)
