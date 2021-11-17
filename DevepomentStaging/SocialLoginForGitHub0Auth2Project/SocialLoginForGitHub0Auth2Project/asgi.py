"""
ASGI config for SocialLoginForGitHub0Auth2Project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialLoginForGitHub0Auth2Project.settings')

application = get_asgi_application()
