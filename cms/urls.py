from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

handler400 = 'handler400'
handler403 = 'handler403'
handler404 = 'handler404'
handler500 = 'handler500'

urlpatterns = []

"""
Below commented codes can be used to add reset password feature for admin area
"""
# from django.contrib.auth import views as auth_views
# urlpatterns = [
#     path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
#     path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
# ]

urlpatterns += [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('posts.urls')),
    path('', include('core.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Custom CMS Administration'
admin.site.index_title = 'Admin Panel'
admin.site.site_title = 'Custom CMS'

def handler400(request, exception=None):
    data = {'message': 'Bad Request'}
    return render(request, 'error.html', data)

def handler403(request, exception=None):
    data = {'message': 'Forbidden'}
    return render(request, 'error.html', data)

def handler404(request, exception=None):
    data = {'message': 'Page not found'}
    return render(request, 'error.html', data)

def handler500(request, exception=None):
    data = {'message': 'Server Error'}
    return render(request, 'error.html', data)