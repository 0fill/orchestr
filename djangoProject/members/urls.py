from django.urls import path
from django.views.generic import ListView, DetailView
from .views import ContactCreateView, ContactUpdateView, ContactDeleteView, ContactListView, Member


urlpatterns = [
    path("",
         ContactListView.as_view(),
         name="members_list"),
    path("<int:pk>/",
         DetailView.as_view(template_name="Member_profile.html",
                                         model=Member),
         name="member_detail"),
    path("create/", ContactCreateView.as_view(), name="add_member"),
    path("update/<int:pk>/", ContactUpdateView.as_view(), name="edit_member"),
    path("delete/<int:pk>/", ContactDeleteView.as_view(), name="member_delete"),
]