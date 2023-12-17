from django.http import JsonResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated
from .serializers import Chargingspotserializer, Replyserializer,Reservatioinserializer,feedbackserializer,Postserializer
from .models import Chargingspot, Feedback, Location, Post, Reply,Reservation
from rest_framework import generics
from datetime import datetime
from rest_framework.response import Response



class ListChargingStations(generics.ListAPIView):
    queryset = Chargingspot.objects.all()
    serializer_class = Chargingspotserializer
    permission_classes = [IsAuthenticated]












     

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Chargingspot.objects.filter(place_id=location_id)


class CreateReservation(generics.CreateAPIView):  
    queryset = Reservation.objects.all()
    serializer_class =Reservatioinserializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 


class UpdateReservation(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = Reservatioinserializer
    permission_classes =[IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class DestroyReservation(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = Reservatioinserializer
    permission_classes =[IsAuthenticated]


class ListReservation(generics.ListAPIView):
    serializer_class = Reservatioinserializer
    queryset = Reservation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
    

class CreateFeedback(generics.CreateAPIView):
    serializer_class = feedbackserializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Listfeedback(generics.ListAPIView):
    serializer_class = feedbackserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chargingspot_id = self.kwargs.get('chargingspot_id')
        queryset = Feedback.objects.filter(chargingspot_id=chargingspot_id)
        return queryset


class Createpost(generics.CreateAPIView):
    serializer_class=Postserializer
    queryset = Post.objects.all()
    permission_classes =[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Listposts(generics.ListAPIView):
    serializer_class=Postserializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]


class Createreply(generics.CreateAPIView):
    serializer_class=Replyserializer
    queryset = Reply.objects.all()
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        post_id=self.kwargs.get('post_id')
        queryset = Reply.objects.filter(post_id=post_id)
        return queryset


class DeleteReservationTimeout(generics.DestroyAPIView):
    serializer_class = Reservatioinserializer
    queryset = Reservation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        now = datetime.now()
        return Reservation.objects.filter(endtime__lt=now)
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset ()
        queryset.delete()  
        return Response({"message": "Successfully deleted all the expired reservations"}, status=204)