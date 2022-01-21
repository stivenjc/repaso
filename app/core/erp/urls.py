from django.urls import path

from core.erp.views.category.views import category_list, CategoryListViews

urlpatterns = [
    path('list', category_list),
    path('listviews', CategoryListViews.as_view())
]