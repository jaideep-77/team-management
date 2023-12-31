from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.MemberList.as_view(), name="members"),
    path('addMember', views.MemberAdd.as_view(), name="add-member"),
    path('editMember/<pk>', views.MemberEdit.as_view(), name="edit-member"),
    path('deleteMember/<pk>', views.MemberDelete.as_view(), name="delete-member"),
]