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


def ImageGuestForm(image_list):

    choices = make_img_choices(image_list)

    class _GuessForm(forms.Form):
        guess = forms.ChoiceField(choices=choices,
                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    return _GuessForm

class GuessForm(forms.Form):

    guess = forms.ChoiceField(choices=[(1, 1), (2, 2), (3, 3)],
                              widget=forms.RadioSelect)

