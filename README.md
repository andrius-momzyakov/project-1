# project-1
Django-based typical web-application's template project 
## uristat application
#### settings.py
```
MIDDLEWARE = [
    ...,
    'uristat.uristat_middleware.UriStatMiddleware'
]
```
```
TEMPLATES = [
    {
        ...,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'uristat.context_processors.uristat_cnt',
            ],
        },
    },
]
```
```
INSTALLED_APPS_LOCAL = [ 
    ...,
    'uristat',
    ...
]    
```
## reg application
#### settings.py
```
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```
#### urls.py
```
urlpatterns = [
    ...,
    url(r'^login/$', mLoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^password_change/$', mPasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', mPasswordChangeDoneView.as_view(), name='password_change_done'),
    ...
]
```
