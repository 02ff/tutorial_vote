from django.contrib import admin
from .models import Question, Choice


class Choiceinline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [Choiceinline]




admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)