from django.urls import re_path as url
from ApiMethods import views


urlpatterns = [
    url(r'^AbcClient$', views.AbcClientApi),
    url(r'^AbcClient/([0-9]+)$', views.AbcClientApi),

    url(r'^AbcResource$', views.AbcResourceApi),
    url(r'^AbcResource/([0-9]+)$', views.AbcResourceApi),

    url(r'^AccessLog$', views.AccessLogApi),
    url(r'^AccessLog/([0-9]+)$', views.AccessLogApi),

    url(r'^Address$', views.AddressApi),
    url(r'^Address/([0-9]+)$', views.AddressApi),

    url(r'^ClientContacts$', views.ClientContactsApi),
    url(r'^ClientContacts/([0-9]+)$', views.ClientContactsApi),

    url(r'^Contact$', views.ContactApi),
    url(r'^Contact/([0-9]+)$', views.ContactApi),

    url(r'^Inventory$', views.InventoryApi),
    url(r'^Inventory/([0-9]+)$', views.InventoryApi),

    url(r'^ResourceType$', views.ResourceTypeApi),
    url(r'^ResourceType/([0-9]+)$', views.ResourceTypeApi),

    url(r'^StorageType$', views.StorageTypeApi),
    url(r'^StorageType/([0-9]+)$', views.StorageTypeApi)
]



