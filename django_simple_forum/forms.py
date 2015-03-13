from django import forms
from django_simple_forum.models import Topic, Post, ProfaneWord
from tinymce.widgets import TinyMCE
from django.utils.translation import ugettext as _
from settings import *

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 30,},mce_attrs=settings.TINYMCE_BODY_CONFIG))
    class Meta:
        model = Post


class TopicForm(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True)

    class Meta():
        model = Topic
        fields = ('title',)


class PostForm(forms.ModelForm):
    body = forms.CharField(label=_('Body'), widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30, 'class':'my_tinymce'},
                mce_attrs = settings.TINYMCE_BODY_CONFIG,
            ))

    class Meta():
        model = Post
        exclude = ('creator', 'updated', 'created','topic', 'user_ip',)

    def clean_body(self):
        body = self.cleaned_data["body"]

        if DJANGO_SIMPLE_FORUM_FILTER_PROFANE_WORDS:
            profane_words = ProfaneWord.objects.all()
            bad_words = [w for w in profane_words if w.word in body.lower()]

            if bad_words:
                raise forms.ValidationError("Bad words like '%s' are not allowed in posts." % (reduce(lambda x,y: "%s,%s" % (x,y),bad_words)))

        return body
