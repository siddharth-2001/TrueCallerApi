from django.urls import path


from .views import SpamReportListView, CreateSpamReportView

urlpatterns = [
    path('', SpamReportListView.as_view(), name='spam-report-list'),
    path('report/', CreateSpamReportView.as_view(), name='create-spam-report')
]