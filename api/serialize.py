from rest_framework import serializers
from activity_app.models import User,ActivityPeriod


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('c_id','real_name','tz')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')




