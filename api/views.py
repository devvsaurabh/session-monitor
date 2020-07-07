from django.shortcuts import render
from activity_app.models import User,ActivityPeriod
from django.http import Http404,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json

from api.serialize import UserSerializer,ActivitySerializer

# Create your views here.

@api_view(["GET"])
def users(request):
    try:
        data=User.objects.all()
        serializer = UserSerializer(data, many=True)
        output_dict = json.loads(json.dumps(serializer.data))
        final_dict = []

        for i in output_dict:
            data1 = ActivityPeriod.objects.filter(c_id=i['c_id'])
            serializer = ActivitySerializer(data1, many=True)
            output_dict1 = json.loads(json.dumps(serializer.data))
            activity_p = {'activity_periods':[]}
            for j in output_dict1:
                activity_p['activity_periods'].append(j)
            i.update(activity_p)
            final_dict.append(i)

        return JsonResponse({'data':final_dict})
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def userdata(request,c_id):
    try:
        data=User.objects.filter(c_id=c_id)
        serializer = UserSerializer(data, many=True)
        output_dict = json.loads(json.dumps(serializer.data))

        data1 = ActivityPeriod.objects.filter(c_id=c_id)
        serializer = ActivitySerializer(data1, many=True)
        output_dict1 = json.loads(json.dumps(serializer.data))

        activity_p = {'activity_periods':[]}
        for i in output_dict1:
            activity_p['activity_periods'].append(i)

        output_dict[0].update(activity_p)
        return JsonResponse(output_dict[0])
    except ValueError as e:
        return JsonResponse({'message':'Invalid UserId'})


@api_view(['GET'])
def delete(request,c_id):
    try:
        data=User.objects.get(c_id=c_id)
        data1 = ActivityPeriod.objects.filter(c_id=c_id)
        data.delete()
        data1.delete()
        return JsonResponse({'message':"Deleted Successfully"})
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update(self, request):
    d = request.data.get('c_id')
    user = User.objects.get(c_id=d)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

