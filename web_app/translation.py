from modeltranslation.translator import register, TranslationOptions
from web_app.models import Company


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'information')

