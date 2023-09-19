from django.urls import path

from .views import ContactListView, CreateContactView, ContactDetailView

urlpatterns = [
    path('', ContactListView.as_view(), name='all-contacts'),
    path('create/', CreateContactView.as_view(), name='create-contact'),
    path('detail/', ContactDetailView.as_view(), name='contact-detail')
]