from django.urls import path

from core.erp.views.category.views import category_list, CategoryListViews, CategoryCreateView

app_name = 'erp'
urlpatterns = [
    path('category/list2/', category_list, name='category_list2'),
    path('category/list/', CategoryListViews.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
]