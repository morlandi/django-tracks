import pytz
import datetime
from django.utils import timezone
from django.conf import settings
from django.utils import formats


def format_datetime(dt, include_time=True):
    """
    Here we adopt the following rule:
    1) format date according to active localization
    2) append time in military format
    """
    if dt is None:
        return ''

    if isinstance(dt, datetime.datetime):
        try:
            dt = timezone.localtime(dt)
        except:
            local_tz = pytz.timezone(getattr(settings, 'TIME_ZONE', 'UTC'))
            dt = local_tz.localize(dt)
    else:
        assert isinstance(dt, datetime.date)
        include_time = False

    use_l10n = getattr(settings, 'USE_L10N', False)
    text = formats.date_format(dt, use_l10n=use_l10n, format='SHORT_DATE_FORMAT')
    if include_time:
        text += dt.strftime(' %H:%M:%S')
    return text
