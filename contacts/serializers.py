import re
from rest_framework import serializers
from .models import Contact
from django.core.validators import validate_email

class ContactSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if len(data['name']) < 3:
            raise serializers.ValidationError('Name must be longer than 2 characters')
        
        elif len(data['phone']) < 10 or re.search('[a-zA-Z]', data['phone']):
            raise serializers.ValidationError('Enter a valid mobile number')
        
        
        if 'email'  not in data:
            return data
        
        try:
            validate_email(data['email'])
        except Exception as e:
            raise serializers.ValidationError({'email': e.messages})
             
        return data
        

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']