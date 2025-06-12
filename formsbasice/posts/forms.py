from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory, formset_factory

from posts.mixins import ReadOnlyFieldsMixin
from posts.models import Post, Comment


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
        fields = '__all__'

        widgets = {
            'language': forms.RadioSelect(
                attrs={'class': 'radio-select'},
            )
        }
        error_messages = {
            'author': {
                'max_length': "Hey thats a lot",
            }
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if not author.isalpha():
            raise ValidationError('Author name should contain only letters')

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title.lower() in content.lower():
            raise ValidationError("The post title shouldn't be included in the content!")

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.author = post.author.capitalize()

        if commit:
            post.save()

        # send_notifications()...

        return post


class PostCreateForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyFieldsMixin, PostBaseForm):
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search for posts...'},
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        labels = {
            'content': '',
        }

        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add a comment...',
                }
            )
        }


CommentFormSet = formset_factory(CommentForm, extra=1)

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