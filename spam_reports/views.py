from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import SpamReport
from .serializers import SpamReportSerializer

# Create your views here.


class SpamReportListView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer


class CreateSpamReportView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer

    def perform_create(self, serializer):
        SpamReport.objects.filter(reported_by = self.request.user, phone = self.request.data['phone']).delete()
        serializer.save(reported_by=self.request.user)