from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('about/', views.AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('restricted/', views.RestrictedView.as_view(), name='restricted'),
    path('register_profile/', views.RegisterProfileView.as_view(), name="register_profile"),
    path('goto/', views.GotoView.as_view(), name='goto'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    path('suggest/', views.CategorySuggestionView.as_view(), name='suggest'),
    path('search_add_page/', views.SearchAddPageView.as_view(), name='search_add_page'),
]
