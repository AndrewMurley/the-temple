from django.conf.urls import url, include
from django.contrib import admin
from . import views

#app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^finished$', views.finished, name='finished'),
    url(r'^opening$', views.opening, name='opening'),
    url(r'^entrance$', views.entrance, name='entrance'),
    url(r'^hole_in_the_ground$', views.hole_in_the_ground, name='hole_in_the_ground'),
    url(r'^jump_down_ending$', views.jump_down_ending, name='jump_down_ending'),
    url(r'^caves$', views.caves, name='caves'),
    url(r'^caves_torch$', views.caves_torch, name='caves_torch'),
    url(r'^caves_flashlight$', views.caves_flashlight, name='caves_flashlight'),
    url(r'^caves_torch_right', views.caves_torch_right, name='caves_torch_right'),
    url(r'^ravine_room$', views.ravine_room, name='ravine_room'),
    url(r'^caves_flashlight_right$', views.caves_flashlight_right, name='caves_flashlight_right'),
    url(r'^caves_flashlight_left$', views.caves_flashlight_left, name='caves_flashlight_left'),
    url(r'^hallway_00$', views.hallway_00, name='hallway_00'),
    url(r'^hallway_01$', views.hallway_01, name='hallway_01'),
    url(r'^hallway_02$', views.hallway_02, name='hallway_02'),
    url(r'^amulet_room_10$', views.amulet_room_10, name="amulet_room_10"),
    url(r'^amulet_room_11$', views.amulet_room_11, name="amulet_room_11"),
    url(r'^amulet_room_12$', views.amulet_room_12, name="amulet_room_12"),
]
