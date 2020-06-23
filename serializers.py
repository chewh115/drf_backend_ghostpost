from rest_framework.serializers import ModelSerializer
from .models import BoastOrRoast

class BoastOrRoastSerializer(ModelSerializer):
    class Meta:
        model = BoastOrRoast
        fields = (
            'boast_or_roast', 
            'title', 
            'post', 
            'up_votes', 
            'down_votes', 
            'submit_time')