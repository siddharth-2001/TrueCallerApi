import re
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from contacts.models import Contact
from spam_reports.models import SpamReport
from accounts.models import CustomUser as User
from accounts.serializers import UserSerializer
from contacts.serializers import ContactSerializer

class SearchView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        if 'query' not in request.data:
            return Response({"error": "Missing 'query' parameter"}, status=status.HTTP_400_BAD_REQUEST)
        
        try: 
            query = request.data['query']
            result = find_user_or_contact_list(query)
            
            return Response(result)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def find_user_or_contact_list(query):
    if re.search('[a-zA-Z]', query):
        return search_by_name(query)
    else:
        return search_by_phone(query)

def search_by_name(query):
    try:
        user = User.objects.get(name=query)
        return format_user_to_json(user)
    except ObjectDoesNotExist:
        contacts = Contact.objects.filter(name__contains=query)
        return format_contact_list_to_json(contacts)

def search_by_phone(query):
    try:
        user = User.objects.get(phone=query)
        return format_user_to_json(user)
    except ObjectDoesNotExist:
        contacts = Contact.objects.filter(phone__contains=query)
        return format_contact_list_to_json(contacts)

def format_user_to_json(user):
    data = UserSerializer(user).data
    spam_report_count = SpamReport.objects.filter(phone=user.phone).count()
    data['spam_reports'] = spam_report_count
    return data

def format_contact_list_to_json(contacts):
    data = ContactSerializer(contacts, many=True).data
    for item in data:
        spam_report_count = SpamReport.objects.filter(phone=item['phone']).count()
        item['spam_reports'] = spam_report_count
    return data
