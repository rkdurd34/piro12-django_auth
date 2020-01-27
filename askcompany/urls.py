from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views
from django.shortcuts import redirect

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('', lambda req: redirect('blog:post_list'), name="root"),
    #path("accounts/", include('django.contrib.auth.urls')),
    path('accounts/', include("accounts.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
