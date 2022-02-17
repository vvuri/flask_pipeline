from django import forms

from .models import Category, News


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150,
#                             label='Заголовок',
#                             widget=forms.Textarea(attrs={
#                                 "class": "form-control",
#                                 "style": "height: 60px"
#                             }))
#     content = forms.CharField(label='Текст',
#                               required=False,
#                               widget=forms.Textarea(attrs={
#                                   "class": "form-control",
#                                   "style": "height: 300px"
#                               }))
#     is_publish = forms.BooleanField(label='Опубликовать сразу',
#                                     initial=True,
#                                     widget=forms.CheckboxInput(attrs={
#                                         "class": "form-check-input"
#                                     }))
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория:',
#                                       empty_label='Категория не выбрана',
#                                       widget=forms.Select(attrs={
#                                           "class": "form-control form-select"
#                                       }))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_publish', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control",
                                            "style": "height: 60px",
                                            'max_length': 150,
                                            'label': 'Заголовок'}),
            'content': forms.Textarea(attrs={"class": "form-control",
                                             "style": "height: 300px",
                                             'label': 'Текст',
                                             'required': False}),
            'is_publish': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


