from django.conf.urls import url, include
import xadmin
#xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()


urlpatterns = [
    url(r'^', xadmin.site.urls),
    url(r'^chpa/', include('visible.url')),
]
