__author__ = 'will'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'step_one.html', 'monty.views.step_one', name='step_one'),
    url(r'step_two.html', 'monty.views.step_two', name='step_two'),
    url(r'final_step.html', 'monty.views.final_step', name='final_step'),
    url(r'stats.html', 'monty.views.stats', name='stats'),
    #url(r'$', 'monty.views.step_one', name='step_one')
)