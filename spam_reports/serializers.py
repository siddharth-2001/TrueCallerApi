import re
from rest_framework import serializers

from .models import SpamReport

class SpamReportSerializer(serializers.ModelSerializer):
     
    def validate(self, data):

        if len(data['name']) < 3:
            raise serializers.ValidationError('Name must be longer than 2 characters')
        
        elif len(data['phone']) < 10 or re.search('[a-zA-Z]', data['phone']):
            raise serializers.ValidationError('Enter a valid mobile number')
        
        return data
        
    class Meta:
        model = SpamReport
        fields = ['name', 'phone', 'reported_at']