from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
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



    #path('search/', views.search, name='search'),
    #path('logout/', views.user_logout, name='logout'),
    #path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    #path('about/', views.about, name='about'),
    #path('add_category/', views.add_category, name='add_category'),
    #path('', views.index, name='index'),
    #path('category/<slug:category_name_slug>/', views.show_category, name ='show_category'),