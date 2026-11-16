from rest_framework import serializers
from studApp.models import StudModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
         model=User
         fields=['username','email','password']
        

class StudentSerializer(serializers.ModelSerializer):
    is_fee_paid=serializers.SerializerMethodField()
    def get_is_fee_paid(self,obj):
        if obj.is_fee_paid:
                return "Paid"
        return "pending"
    class Meta:
        model=User
        fields="__all__"
        
        
