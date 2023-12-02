from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard_page'),
    path('edit-profile', views.EditUserProfliePage.as_view(), name='edit-profile-page'),
    path('change-password', views.ChangePasswordPage.as_view(), name='change-password-page'),
    path('my-shopping', views.MyShopping.as_view(), name='user_shopping_page'),
    path('my-shopping-detail/<order_id>', views.my_shopping_detail, name='user_shopping_detail_page'),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail-count', views.change_order_detail_count, name='change_order_detail_count_ajax'),
]
