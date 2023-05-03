from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf import settings


import friends.views as friends
import help_translation.views as help_translation



admin.site.site_header = "Администрирование сайта"
admin.site.site_title = "Администрирование сайта"
admin.site.index_title = "Добро пожаловать!"

router = DefaultRouter()


router.register('friends', friends.FriendsView)
router.register('help_translation', help_translation.HelpTranlationView)
router.register('autopay_delete', help_translation.AutoPayView)

schema_view = get_schema_view(
    openapi.Info(
        title='',
        default_version='v1',
        description='',
        contact=openapi.Contact(email=''),
        license=openapi.License(name='MIT')
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger')),
    path('docs<str:format>', schema_view.without_ui()),
    path('swagger.json', schema_view.without_ui(), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
