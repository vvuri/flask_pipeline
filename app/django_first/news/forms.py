from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150,
                            label='Заголовок',
                            widget=forms.Textarea(attrs={
                                "class": "form-control",
                                "style": "height: 60px"
                            }))
    content = forms.CharField(label='Текст',
                              required=False,
                              widget=forms.Textarea(attrs={
                                  "class": "form-control",
                                  "style": "height: 300px"
                              }))
    is_publish = forms.BooleanField(label='Опубликовать сразу',
                                    initial=True,
                                    widget=forms.CheckboxInput(attrs={
                                        "class": "form-check-input"
                                    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='Категория:',
                                      empty_label='Категория не выбрана',
                                      widget=forms.Select(attrs={
                                          "class": "form-control form-select"
                                      }))
