from  crud.models import Bio
from rest_framework import serializers

class BioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bio
        #Fields = '__all__'
        exclude = ()