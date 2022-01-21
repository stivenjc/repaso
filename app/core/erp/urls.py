from django.urls import path

from core.erp.views.category.views import category_list, CategoryListViews

urlpatterns = [
    path('list', category_list, name='category_list2'),
    path('listviews', CategoryListViews.as_view(), name='category_list')
]