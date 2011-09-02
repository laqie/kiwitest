def settings_processor(request):
    from django.conf import settings
    return  dict(settings=settings)
  