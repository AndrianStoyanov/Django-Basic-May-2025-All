from django import forms

# from posts import models
# from posts.choices import LanguageChoices
from posts.models import Post
# from posts.validators import BadWordValidator

    # Option 1
# class PostForm(forms.Form):
    # title = forms.CharField(max_length=100)
    # content = forms.TextField(
    #     validators=[BadWordValidator(
    #         bad_words=['bad_word_1', 'bad_word_2'],
    #     )]
    # )
    # author = forms.CharField(max_length=50)
    # created_at = forms.DateTimeField(auto_now_add=True)
    # language = forms.CharField(
    #     max_length=20,
    #     choices=LanguageChoices,
    #     default=LanguageChoices.OTHER,
    # )

    # Option 2


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'content', 'language', 'author') or
        fields = '__all__'
        widgets = {
            'language': forms.RadioSelect(
                attrs={'class': 'radio-select'},
            ),
        }
        help_texts = {
            'title': 'This is the help text.',
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Search for post...'},),
    )

# Examples forms
# class MyForm(forms.Form):
#     CHOICES = [('option 1', 'Option 1'), ('option 2', 'Option 2')]
#     my_name = forms.CharField(
#         max_length=10,
#         required=True,
#         # initial='Hello World',
#         label='My Name is',
#         help_text='Support when write the forms',
#         # widget=forms.Textarea(
#         #     attrs={'cols': 80, 'style': "color:blue", 'placeholder': 'Enter your name'},
#         widget=forms.PasswordInput()
#     )
    # my_text = forms.CharField(
    #     widget=forms.Textarea()
    # )
    # my_number = forms.IntegerField()
    # radio = forms.ChoiceField(
    #     choices=CHOICES,
    #     widget=forms.RadioSelect,
    # )
    # multiple_select = forms.MultipleChoiceField(
    #     choices=CHOICES,
    #     widget=forms.CheckboxSelectMultiple,
    # )
    # date = forms.DateField(
    #     # widget=forms.DateInput(format='%Y-%m-%d'),
    #     widget=forms.SelectDateWidget,
    # )