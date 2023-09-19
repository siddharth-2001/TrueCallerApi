from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser as User
from contacts.models import Contact
from .serializers import UserSerializer
from spam_reports.models import SpamReport
# Create your views here.

class UserListView(generics.ListAPIView):
   authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
   permission_classes = [IsAuthenticated]

   queryset = User.objects.all()
   serializer_class = UserSerializer
   

class CreateUserView(APIView):
   def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            Contact(user = instance,name = instance.name, phone = instance.phone).save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

class UserDetailView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format = None):
        user_id = request.data['id']

        try:
            user = User.objects.get(id = user_id)
            data = UserSerializer(user).data
            data['spam reports'] = SpamReport.objects.filter(phone = user.phone).count()
            if Contact.objects.filter(user = user, phone = request.user.phone).count() == 0:
                del data['email']
            
            return Response(data, status=status.HTTP_200_OK)
                                                              
        except ObjectDoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)