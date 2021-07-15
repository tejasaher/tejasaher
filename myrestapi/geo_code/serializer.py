from rest_framework import serializers
from .models import geo_code

class geo_codeSerializer(serializers.ModelSerializer):
	
	class Meta:

		model = geo_code
		fields = '__all__'