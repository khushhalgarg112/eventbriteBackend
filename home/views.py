from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Auth, Event, Like
from .serializers import AuthSerializer, AuthRegSerializer, EventSerializer,LikeSerializer


class RegisterView(APIView):
    def post(self, request):
        # Deserialize the request data
        serializer = AuthRegSerializer(data=request.data)

        # Check if the data is valid
        if serializer.is_valid():
            username = serializer.validated_data['email']

            # Check if a user with the same username already exists
            if Auth.objects.filter(email=username).exists():
                return Response({"error": "Username already exists. Please log in instead.", "id": 10}, status=status.HTTP_400_BAD_REQUEST)
            
            # Create a new user
            serializer.save()
            return Response({"id": 11, "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            print("hello")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return Response({"error": "GET method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class LoginView(APIView):
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Check if a user with the provided username and password exists
            try:
                user = Auth.objects.get(email=username, password=password)
                if user:
                    return Response({"data": serializer.data, "id":11}, status=status.HTTP_200_OK)
            except Auth.DoesNotExist:
                return Response({"error": "Wrong username or password."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return Response({"error": "GET method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

class EventView(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": 11, "data": "Event Created Successfully"}, status=status.HTTP_201_CREATED)
        else:
            print("hello")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return Response({"error": "GET method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EventListView(APIView):
    def get(self, request):
        # Retrieve all Event objects from the database
        events = Event.objects.all()
        # Serialize the queryset
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
class LikeSaveView(APIView):
    def post(self,request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():

            id = serializer.validated_data['eventid']
            user = serializer.validated_data['user']

            # Check if a user with the same username already exists
            if Like.objects.filter(user=user, eventid=id).exists():
                return Response({"error": "Data Already Exist", "id": 10}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({"id": 11, "data": "Added to Like"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        likes = Like.objects.all()

        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)
    def delete(self, request):
        id = request.data.get('eventid')
        user = request.data.get('user')
        try:
            like_instance = Like.objects.get(eventid=id, user=user)
            like_instance.delete()
            return Response({"message": "Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist as e:
            print(f"Error: {e}")
            print(f"eventid: {id}, user: {user}")
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)


