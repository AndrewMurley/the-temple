from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    text = {
        'prompt' : "Do you want to go on an adventure?",
        'inputs' : [("Yes", "/display/opening"), ("No", "/display/finished")],
        }
    return render(request, 'display/index.html', text)

def opening(request):
    #return HttpResponse(request.POST['choice'])
    text = {
        'prompt' : "Use entrance or climb up the side?",
        'inputs' : [("Use entrance", "/display/entrance"), "Climb up the side"],
        }
    return render(request, 'display/index.html', text)

def finished(request):
    text = {
        'prompt' : "Your adventure is over. Thank you for playing!",
        }
    return render(request, 'display/index.html', text)

def entrance(request):
    text = {
        'prompt' : "Use the hole in the ground or the open corridor?",
        'inputs' : ["Hole in the ground", "Open corridor"],
        }
    return render(request, 'display/index.html', text)

def hole_in_the_ground(request):
    text = {
        'prompt' : "Do you want to lower yourself down or jump down?",
        'inputs' : ["Jump down", "Lower myself down"],
        }
    return render(request, 'display/index.html', text)

def jump_down_ending(request):
    text = {
        'prompt' : "You jump down and break your leg. You climb out wearily and drag yourself back to town.",
        'inputs' : "End",
        }
    return render(request, 'display/index.html', text)

def caves(request):
    text = {
        'prompt' : "Use a torch or a flashlight?",
        'inputs' : ["Torch", "Flashlight"],
        }
    return render(request, 'display/index.html', text)

def caves_torch(request):
    text = {
        'prompt' : "Go in the right cave or the left cave?",
        'inputs' : ["Right", "Left"],
        }
    return render(request, 'display/index.html', text)
    
def caves_flashlight(request):
    text = {
        'prompt' : "Go in the right cave or the left cave?",
        'inputs' : ["Right", "Left"],
        }
    return render(request, 'display/index.html', text)

def caves_torch_right(request):
    text = {
        'prompt' : "The wind blows the torch out and you get lost in the dark.",
        'inputs' : "End",
        }
    return render(request, 'display/index.html', text)

def caves_flashlight_right(request):
    text = {
        'prompt' : "As you enter, dozens of snakes slither up from the floor. You try to ward them off with your flashlight, but it fails. The snakes bite you until the poison numbs your body. You cannot continue your adventure.",
        'inputs' : "End",
        }
    return render(request, 'display/index.html', text)

def caves_flashlight_left(request):
    text = {
        'prompt' : "Your battery dies and you get lost in the dark.",
        'inputs' : "End",
        }
    return render(request, 'display/index.html', text)

def ravine_room(request):
    text = {
        'prompt' : "As you enter, dozens of snakes slither up from the floor. You ward them off with your torch and continue your adventure. You enter a room and find a ravine blocking the exit. Do you: swing to the exiton a rope, use a wire that crosses the room like a tightrope, or run and jump, across the ravine?",
        'inputs' : ["Swing to the exit on a rope", "Use a wire that crosses the room like a tightrope", "Run and jump across the ravine"],
        }
    return render(request, 'display/index.html', text)

def hallway_00(request):
    text = {
        'prompt' : "You lasso your rope to an old support beam and swing across. You come across a long hallway that looks safe, too safe. Do you throw a rock to test for traps or walk in cautiously?",
        'inputs' : ["Throw a rock to test for traps", "Walk in cautiously"],
        }
    #choices[0]=0
    return render(request, 'display/index.html', text)

def hallway_01(request):
    text = {
        'prompt' : "You back up to get a running start. You run at full speed and jump as far as you can. You land on the other side. Do you use your rope to test for traps, throw a rock to test for traps, or walk in cautiously?",
        'inputs' : ["Use rope to test for traps", "Throw a rock to test for traps", "Walk in cautiously"],
        }
    #choices[0]=1
    return render(request, 'display/index.html', text)

def hallway_02(request):
    text = {
        'prompt' : "You try to use a wire to cross the ravine. You make it halfway across before the wire snaps under your wieght. You fall to your death",
        'inputs' : "End",
    }
    return render(request, 'display/index.html', text)

def amulet_room_10(request):
    text = {
        'prompt' : "You roll your rope across the floor. It reveals that there is a hidden spike trap in the floor. You avoid the spike trap. In the next room, you find an amulet on a pedestal. There is an inscription next to it. It reads, 'Beware any who wish to take this amulet for themselves. If you leave this temple with it, you will be burdened with a curse. You'd think I'd tell what the curse is? Ha! You'll have to find that out for yourself.' Do you take the amulet or leave it where it is?",
        'inputs' : ["Take the amulet", "Leave the amulet"],
        }
    #choices[1]=0
    return render(request, 'display/index.html', text)

def amulet_room_11(request):
    text = {
        'prompt' : "The rock reveals no traps. You walk in and activate a hidden spike trap and impail your foot. You bandage your foot but it still hurts to walk. You have a limp now. In the next room, you find an amulet on a pedestal. There is an inscription next to it. It reads, 'Beware any who wish to take this amulet for themselves. If you leave this temple with it, you will be burdened with a curse. You'd think I'd tell what the curse is? Ha! You'll have to find that out for yourself.' Do you take the amulet or leave it where it is?",
        'inputs' : ["Take the amulet", "Leave the amulet"],
        }
    #choices[1]=1
    return render(request, 'display/index.html', text)

def amulet_room_12(request):
    text = {
        'prompt' : "You walk in catiously and accidentaly fall over. Your wieght activates the hidden spike trap and the trap impails you. You bandage up your body but you are in a lot of pain. You decide to try and head back to town.",
        'inputs' : "End",
        }
    return render(request, 'display/index.html', text)