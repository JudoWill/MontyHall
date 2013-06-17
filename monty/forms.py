__author__ = 'will'
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe


def make_img_choices(image_list):

    tmp = '<img src="%(img)s" alt="Door %(dnum)i" title="Door %(dnum)i" width="85" height="200">'

    choices = []
    for num, img in enumerate(image_list, 1):
        tdict = {
            'media_url': settings.MEDIA_URL,
            'img': img.img.url,
            'dnum': num
        }
        choices.append((num, mark_safe(_(tmp % tdict))))

    return choices


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """renders horizontal radio buttons.
    found here:
    https://wikis.utexas.edu/display/~bm6432/Django-Modifying+RadioSelect+Widget+to+have+horizontal+buttons
    """

    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


def ImageGuestForm(image_list, hide_player):

    choices = make_img_choices(image_list)

    if hide_player:
        class _GuessForm(forms.Form):
            player = forms.CharField(max_length=50, widget=forms.HiddenInput)
            guess = forms.ChoiceField(choices=choices,
                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))

    else:
        class _GuessForm(forms.Form):
            player = forms.CharField(max_length=50)
            guess = forms.ChoiceField(choices=choices,
                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    return _GuessForm
