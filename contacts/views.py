from rest_framework import  generics, status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


from .models import Contact
from .serializers import ContactSerializer
from spam_reports.models import SpamReport

# Create your views here.

class ContactListView(generics.ListAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class CreateContactView(generics.CreateAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        data = self.request.data
        Contact.objects.filter(user = self.request.user, phone = data['phone']).delete()
        serializer.save(user=self.request.user)


class ContactDetailView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format = None):
        contact_id = request.data['id']

        try:
            contact = Contact.objects.get(id = contact_id)
            data = ContactSerializer(contact).data
            data['spam reports'] = SpamReport.objects.filter(phone = contact.phone).count()
            return Response(data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
       
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)