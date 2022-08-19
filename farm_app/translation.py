from modeltranslation.translator import register, TranslationOptions
from farm_app.models import AboutUs, Main


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
