from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("card/<slug:pk>", views.card, name="card"),
    path("collection/<int:pk>", views.collection, name="collection"),
    path(
        "collection/create",
        views.CreateCollectionView.as_view(),
        name="create-collection",
    ),
    path("adv-search", views.AdvSearchView.as_view(), name="adv-search"),
]
