from django import forms
from .models import blogs

class blogs_form(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ("author", "title", "created_on", "blog_header", "body",)

    def save(self):
        user = super(blogs_forms, self).save(commit=False)
        user.title = self.cleaned_data["title"]
        user.blog_header = self.cleaned_data["blog_header"]
        user.body = self.cleaned_data["body"]
        return user