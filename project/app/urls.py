from django.urls import path
from .views import CreateReservation, ListChargingStations,ListReservation,CreateFeedback,Listfeedback,Createpost,Listposts,Createreply,UpdateReservation,DestroyReservation,DeleteReservationTimeout,Register

urlpatterns = [
    #
    path('register/',Register.as_view(),name='register'),
    path('charging-stations/<int:location_id>/', ListChargingStations.as_view(), name='charging_stations_by_location'),
    path('reservation/',CreateReservation.as_view(),name='reservation'),
    path('listreservations/',ListReservation.as_view(),name='reservationlist'),
    path('feedback/',CreateFeedback.as_view(),name='addfeedback'),
    path('feedbacklist/<int:chargingspot_id>/',Listfeedback.as_view(),name='charging-poin-tfeedback'),
    path('createpost/',Createpost.as_view(),name='addpost'),
    path('listposts/',Listposts.as_view(),name='listposts'),
    path('replypost/<int:post_id>/', Createreply.as_view(),name='reply'),
    path('updatereservation/<int:pk>/',UpdateReservation.as_view(),name='updatereservation'),
    path('deletereservation/<int:pk>/',DestroyReservation.as_view(),name='delete-reservation'),
    path('delete-reservations/', DeleteReservationTimeout.as_view(), name='delete_reservations')
] 
