from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Section, MainSection


class MainSectionInlineFormset(BaseInlineFormSet):
    
    def clean(self):
        self.is_main_counter = 0
        for form in self.forms:
            form_data = form.cleaned_data
            if form_data and form_data['is_main']:
                self.is_main_counter += 1
        if self.is_main_counter > 1:
            raise ValidationError('Основным может быть только один раздел.')
        if self.is_main_counter == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
             # вызываем базовый код переопределяемого метода


class MainSectionInline(admin.TabularInline):
    model = MainSection
    formset = MainSectionInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [MainSectionInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['tag_name']