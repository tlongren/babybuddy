# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from core.models import Timer


register = template.Library()


@register.inclusion_tag('core/timer_nav.html', takes_context=True)
def timer_nav(context, active=True):
    request = context['request'] or None
    timers = Timer.objects.filter(active=active)
    perms = context['perms'] or None
    # The 'next' parameter is currently not used.
    return {'timers': timers, 'perms': perms, 'next': request.path}
