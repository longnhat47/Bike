
from django.urls import path

from bike.views import rentview, adminbikeview, CreateBike, EditBike, DeleteBike, rentfilterview

urlpatterns = [
    path('rentpage/', rentview, name='rentpage'),
    path('bike-type-page/<uuid:id>', rentfilterview, name='bike-type-page'),
    path('bike_admin/', adminbikeview, name='bike_admin'),
    path('add_bike/', CreateBike.as_view(), name='add_bike'),
    path('edit-bike/<uuid:pk>', EditBike.as_view(), name='update_bike'),
    path('delete-bike/<uuid:pk>', DeleteBike.as_view(), name='delete_bike'),
]
