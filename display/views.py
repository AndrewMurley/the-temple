from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

choices = [0, 0, 0]
def room_func(room_name):
    room_data = {
        "index": 
            {'prompt' : "Do you want to go on an adventure?",
            'inputs' : [("Yes", "/display/opening"), ("No", "/display/finished")],},\

        "opening":
            {'prompt' : "Use entrance or climb up the side?",
            'inputs' : [("Use entrance", "/display/entrance"), ("Climb up the side", "/display/up_the_side")],},
        
        "finished":
            {'prompt' : "Your adventure is over. Thank you for playing!",},
    }
    return room_data[room_name]

def index(request):
    text = room_func("index")
    return render(request, 'display/index.html', text)

def index2(request, room_name):
    text = room_func("finished")
    return render(request, 'display/index.html', text)

def opening(request):
    #return HttpResponse(request.POST['choice'])
    text = room_func("opening")
    return render(request, 'display/index.html', text)

def finished(request):
    text = room_func("finished")
    return render(request, 'display/index.html', text)

def entrance(request):
    text = {
        'prompt' : "Use the hole in the ground or the open corridor?",
        'inputs' : [("Hole in the ground", "/display/hole_in_the_ground"), ("Open corridor", "/display/open_corridor")],
        }
    return render(request, 'display/index.html', text)

def hole_in_the_ground(request):
    text = {
        'prompt' : "Do you want to lower yourself down or jump down?",
        'inputs' : [("Jump down", "/display/jump_down"), ("Lower myself down", "/display/caves")],
        }
    return render(request, 'display/index.html', text)

def jump_down(request):
    text = {
        'prompt' : "You jump down and break your leg. You climb out wearily and drag yourself back to town.",
        'inputs' : [("End", "/display/finished")],
        }
    return render(request, 'display/index.html', text)

def caves(request):
    text = {
        'prompt' : "Use a torch or a flashlight?",
        'inputs' : [("Torch", "/display/caves_torch"), ("Flashlight", "/display/caves_flashlight")],
        }
    return render(request, 'display/index.html', text)

def caves_torch(request):
    text = {
        'prompt' : "Go in the right cave or the left cave?",
        'inputs' : [("Right", "/display/caves_torch_right"), ("Left", "/display/ravine_room")],
        }
    return render(request, 'display/index.html', text)
    
def caves_flashlight(request):
    text = {
        'prompt' : "Go in the right cave or the left cave?",
        'inputs' : [("Right", "/display/caves_flashlight_right"), ("Left", "/display/caves_flashlight_left")],
        }
    return render(request, 'display/index.html', text)

def caves_torch_right(request):
    text = {
        'prompt' : "The wind blows the torch out and you get lost in the dark.",
        'inputs' : [("End", "/display/finished")],
        }
    return render(request, 'display/index.html', text)

def caves_flashlight_right(request):
    text = {
        'prompt' : "As you enter, dozens of snakes slither up from the floor. You try to ward them off with your flashlight, but it fails. The snakes bite you until the poison numbs your body. You cannot continue your adventure.",
        'inputs' : [("End", "/display/finished")],
        }
    return render(request, 'display/index.html', text)

def caves_flashlight_left(request):
    text = {
        'prompt' : "Your battery dies and you get lost in the dark.",
        'inputs' : [("End", "/display/finished")],
        }
    return render(request, 'display/index.html', text)

def ravine_room(request):
    text = {
        'prompt' : "As you enter, dozens of snakes slither up from the floor. You ward them off with your torch and continue your adventure. You enter a room and find a ravine blocking the exit. Do you: swing to the exiton a rope, use a wire that crosses the room like a tightrope, or run and jump, across the ravine?",
        'inputs' : [("Swing to the exit on a rope", "/display/hallway_00"), ("Use a wire that crosses the room like a tightrope", "/display/hallway_02"), ("Run and jump across the ravine", "/display/hallway_01")],
        }
    return render(request, 'display/index.html', text)

def hallway_00(request):
    text = {
        'prompt' : "You lasso your rope to an old support beam and swing across. You come across a long hallway that looks safe, too safe. Do you throw a rock to test for traps or walk in cautiously?",
        'inputs' : [("Throw a rock to test for traps", "/display/amulet_room_11"), ("Walk in cautiously", "/display/amulet_room_12")],
        }
    choices[0]=0
    return render(request, 'display/index.html', text)

def hallway_01(request):
    text = {
        'prompt' : "You back up to get a running start. You run at full speed and jump as far as you can. You land on the other side. Do you use your rope to test for traps, throw a rock to test for traps, or walk in cautiously?",
        'inputs' : [("Use rope to test for traps", "/display/amulet_room_10"), ("Throw a rock to test for traps", "/display/amulet_room_11"), ("Walk in cautiously", "/display/amulet_room_12")],
        }
    choices[0]=1
    return render(request, 'display/index.html', text)

def hallway_02(request):
    text = {
        'prompt' : "You try to use a wire to cross the ravine. You make it halfway across before the wire snaps under your wieght. You fall to your death",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def amulet_room_10(request):
    text = {
        'prompt' : "You roll your rope across the floor. It reveals that there is a hidden spike trap in the floor. You avoid the spike trap. In the next room, you find an amulet on a pedestal. There is an inscription next to it. It reads, 'Beware any who wish to take this amulet for themselves. If you leave this temple with it, you will be burdened with a curse. You'd think I'd tell what the curse is? Ha! You'll have to find that out for yourself.' Do you take the amulet or leave it where it is?",
        'inputs' : [("Take the amulet", "/display/take_the_amulet"), ("Leave the amulet", "/display/leave_the_amulet")],
        }
    choices[1]=0
    return render(request, 'display/index.html', text)

def amulet_room_11(request):
    text = {
        'prompt' : "The rock reveals no traps. You walk in and activate a hidden spike trap and impail your foot. You bandage your foot but it still hurts to walk. You have a limp now. In the next room, you find an amulet on a pedestal. There is an inscription next to it. It reads, 'Beware any who wish to take this amulet for themselves. If you leave this temple with it, you will be burdened with a curse. You'd think I'd tell what the curse is? Ha! You'll have to find that out for yourself.' Do you take the amulet or leave it where it is?",
        'inputs' : [("Take the amulet", "/display/take_the_amulet"), ("Leave the amulet", "/display/leave_the_amulet")],
        }
    choices[1]=1
    return render(request, 'display/index.html', text)

def amulet_room_12(request):
    text = {
        'prompt' : "You walk in catiously and accidentally fall over. Your wieght activates the hidden spike trap and the trap impails you. You bandage up your body but you are in a lot of pain. You decide to try and head back to town.",
        'inputs' : [("End", "/display/finished")],
        }
    return render(request, 'display/index.html', text)

def take_the_amulet(request):
    choices[2] = 1
    text = {
        'prompt' : "You pick up the amulet and look at it. There appears to be an inscription on it. However, you decide to decipher it later. You avoid the spike trap and head back to the ravine.",
        'inputs' : [("Continue", "/display/exit_scene")],
    }
    return render(request, 'display/index.html', text)

def leave_the_amulet(request):
    choices[2] = 0
    text = {
        'prompt' : "You leave the Amulet where it is, fearing whatever curse it posesses. You avoid the spike trap and head back to the ravine.",
        'inputs' : [("Continue", "/display/exit_scene")],
    }
    return render(request, 'display/index.html', text)

def exit_scene(request):
    if choices[0] == 1 and choices[1] == 1:
        text = {
            'prompt' : "You return to the ravine and discover that you cannot swing across nor jump across. You are stuck.",
            'inputs' : [("End", "/display/finished")],
        }
        return render(request, 'display/index.html', text)
    
    else:
        text = {
            'prompt' : "You arrive at the ravine. Do you use your rope or jump across?",
            'inputs' : [("Use rope", "/display/exit_scene_rope"), ("Jump across", "/display/exit_scene_jump")],
        }
        return render(request, 'display/index/html', text)

def exit_scene_rope(request):
    if choices[0] == 0 and choices[2] == 0:
        text = {
            'prompt' : "You use your rope to swing across.",
            'inputs' : [("Continue", "/display/no_amulet_ending")],
        }
        return render(request, 'display/index.html', text)
    
    elif choices [0] == 0 and choices[2] == 1:
        text = {
            'prompt' : "You use your rope to swing across.",
            'inputs' : [("Continue", "/display/amulet_ending")],
        }
        return render(request, 'display/index.html', text)
    
    elif choices [0] == 1:
        text = {
            'prompt' : "You cannot attach the rope from this side.",
            'inputs' : [("Continue", "/display/exit_scene")],
        }
        return render(request, 'display/index.html', text)
    
    else:
        text = {
            'prompt' : "Error.",
            'inputs' : [("Continue", "/display/exit_scene")]
        }
        return render(request, 'display/index.html', text)

def exit_scene_jump(request):
    if choices [1] == 0 and choices[2] == 0:
        text = {
            'prompt' : "You run and jump across the ravine.",
            'inputs' : [("Continue", "/display/no_amulet_ending")],
        }
        return render(request, 'display/index.html', text)
    
    elif choices [1] == 0 and choices[2] == 1:
        text = {
            'prompt' : "You run and jump across the ravine.",
            'inputs' : [("Continue", "/display/amulet_ending")],
        }
        return render(request, 'display/index.html', text)
    
    elif choices [1] == 1:
        text = {
            'prompt' : "You have a limp and cannot jump across.",
            'inputs' : [("Continue", "/display/exit_scene")],
        }
        return render(request, 'display/index.html', text)
    
    else:
        text = {
            'prompt' : "Error.",
            'inputs' : [("Continue", "/display/exit_scene")]
        }
        return render(request, 'display/index.html', text)

def no_amulet_ending(request):
    text = {
        'prompt' : "Without the amulet, you have nothing to show for your adventure. You return to town, defeated.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def amulet_ending(request):
    text = {
        'prompt' : "After you exit the temple, you notice an inscription on the amulet. It reads, 'Congratulations! You have managed to survive the first temple. You could stop now and return home, or you could follow these instructions to find a more dangerous, more rewarding temple. The choice is yours.'",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def open_corridor(request):
    text = {
        'prompt' : "Check for traps or run in?",
        'inputs' : [("Check for traps", "/display/check"), ("Run in", "/display/run_in")], #Add continue for prompt
    }
    return render(request, 'display/index.html', text)

def check(request):
    text = {
        'prompt' : "You find a presurized floor pannel and decide to avoid it. You move on to the next room.",
        'inputs' : [("Continue", "/display/treasure_room")],
    }
    return render(request, 'display/index.html', text)

def run_in(request):
    text = {
        'prompt' : "You trigger a trip wire and the wall shoots poison darts at you. You narrowly dodge them and decide this adventure isn't worth risking your life for. You head back to town.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def up_the_side(request):
    text = {
        'prompt' : "Do you want to use your rope or free climb it?",
        'inputs' : [("Use rope", "/display/up_the_side_rope"), ("Free climb", "/display/up_the_side_free")],
    }
    return render(request, 'display/index.html', text)

def up_the_side_rope(request):
    text = {
        'prompt' : "Attach your rope to a branch or the top of the temple?",
        'inputs' : [("Branch", "/display/up_the_side_rope_branch"), ("Top of the temple", "/display/up_the_side_rope_top")],
    }
    return render(request, 'display/index.html', text)

def up_the_side_rope_branch(request):
    text = {
        'prompt' : "While you scale the temple, the branch snaps and you fall down the side. Upon landing, you twist your ankle. You can't walk very well so you hobble back to town.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def up_the_side_rope_top(request):
    text = {
        'prompt' : "The rope stays attached and you make it to the top.",
        'inputs' : [("Continue", "/display/top_of_the_temple")],
    }
    return render(request, 'display/index.html', text)

def up_the_side_free(request):
    text = {
        'prompt' : "Are you sure? Do you want to reconsider or go for it?",
        'inputs' : [("Go for it", "/display/up_the_side_free_go"), ("Reconsider", "/display/up_the_side_free_reconsider")],
    }
    return render(request, 'display/index.html', text)

def reconsider(request):
    text = {
        'prompt' : "You think that maybe this isn't a good idea and try to think of another way. However, you begin to question all of you life choices and wonder if anything is worth it. You decide you need to rethink your life as you go back to town.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def go_for_it(request):
    text = {
        'prompt' : "You decide to ignore that little voice in your head that tells you that free-climbing an old temple is not a good idea and go for it. However, luck is on your side and you reach the top.",
        'inputs' : [("Continue", "/display/top_of_the_temple")],
    }
    return render(request, 'display/index.html', text)

def top_of_the_temple(request):
    text = {
        'prompt' : "Use the stairs or the spooky tunnel?",
        'inputs' : [("Stairs", "/display/stairs"),("Spooky tunnel", "/display/spooky_tunnel")]
    }
    return render(request, 'display/index.html', text)

def stairs(request):
    text = {
        'prompt' : "You fall down the stairs and break your neck. That's it. You're dead.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def spooky_tunnel(request):
    text = {
        'prompt' : "You grudgingly go down the spooky tunnel. You are startled by everything. Even a little mouse. A mouse! Somehow, you make it to the next room.",
        'inputs' : [("Continue", "/display/treasure_room")],
    }
    return render(request, 'display/index.html', text)

def treasure_room(request):
    text = {
        'prompt' : "You find yourself in a room full of treasure Do you want to take the treasure chest, the totem on a pedestal, or the sack?",
        'inputs' : [("Treasure chest", "/display/treasure_chest"), ("Totem on pedestal", "/display/totem_on_pedestal"), ("Sack", "/display/sack")],
    }
    return render(request, 'display/index.html', text)

def sack(request):
    text = {
        'prompt' : "You take the sack an leave the temple with ease. You open the sack to reveal that there is some gold and some jewels inside. You are rich! You got 100 pieces of gold from the sack.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def treasure_chest(request):
    text = {
        'prompt' : "As you pick up the chest, the room starts collapsing around you. Do you go through the right or left cave?",
        'inputs' : [("Right cave", "/display/treasure_chest_right"), ("Left cave", "/display/treasure_chest_left")],
    }
    return render(request, 'display/index.html', text)

def treasure_chest_right(request):
    text = {
        'prompt' : "You escape the temple as it crumbles to the ground. You open the chest and find that it is full of gold. You are rich! You got 600 pieces of gold from the chest.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def treasure_chest_left(request):
    text = {
        'prompt' : "Do you go through a narrow tunnel or turn back?",
        'inputs' : [("Narrow tunnel", "/display/treasure_chest_narrow"),("Turn back", "/display/treasure_chest_turn_back")],
    }
    return render(request, 'display/index.html', text)

def treasure_chest_narrow(request):
    text = {
        'prompt' : "You squeeze through the tunnel and just barley make it out. In the process, you break your foot. You open the chest and find that it is full of gold. Do you leave some behind to lighten your load or keep it all?",
        'inputs' : [("Lighten your load", "/display/treasure_chest_lighten"), ("Keep it all", "/display/treasure_chest_keep")],
    }
    return render(request, 'display/index.html', text)

def treasure_chest_lighten(request):
    text = {
        'prompt' : "You empty some gold out of the chest to make your journey easier. You make it back with plenty of energy so nobody bothers you. You have to pay for the medical expenses for your foot. You are rich! You get 300 pieces of gold from the chest.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def treasure_chest_keep(request):
    text = {
        'prompt' : "You dedide to keep all of your gold. The journey back is arduous, so you return with little energy. Local thugs notice your lack of energy and jump you. You lose almost all of your gold. You use the remaining gold to pay for medical expenses for your foot. You get nothing.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def treasure_chest_turn_back(request):
    text = {
        'prompt' : "You try to go the other way, but you get caught in the falling debris and crushed.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def totem_on_pedestal(request):
    text = {
        'prompt' : "A boulder falls through the ceiling and rolls towards you. Go through the right cave or the left cave?",
        'inputs' : [("Right cave", "/display/totem_right"),("Left cave", "/display/totem_left")],
    }
    return render(request, 'display/index.html', text)

def totem_right(request):
    text = {
        'prompt' : "You escape the temple as it crumbles to the ground.",
        'inputs' : [("Continue", "/display/sell_or_donate")],
    }
    return render(request, 'display/index.html', text)

def totem_left(request):
    text = {
        'prompt' : "Do you go through a narrow tunnel or turn back?",
        'inputs' : [("Narrow tunnel", "/display/totem_narrow"),("Turn back", "/display/totem_turn")],
    }
    return render(request, 'display/index.html', text)

def totem_narrow(request):
    text = {
        'prompt' : "You squeeze through the tunnel, but only barley make it out. In the process, you break your foot. Do you leave the totem behind to lighten your load or take it with you?",
        'inputs' : [("Leave totem behind", "/display/totem_leave"),("Take totem with you", "/display/totem_keep")],
    }
    return render(request, 'display/index.html', text)

def totem_leave(request):
    text = {
        'prompt' : "You return to town empty handed. You went on an amazing adventure but have nothing to show for it.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def totem_keep(request):
    text = {
        'prompt' : "You dedide to keep the totem. The journey back is tedious with the added weight, but you still return with some energy. Nobody bothers you. You return to town with the strange artifact.",
        'inputs' : [("Continue", "sell_or_donate")],
    }
    return render(request, 'display/index.html', text)

def totem_turn(request):
    text = {
        'prompt' : "You try to go the other way, but you get squished by the boulder.",
        'inputs' : [("Continue", "/display/finsihed")],
    }
    return render(request, 'display/index.html', text)

def sell_or_donate(request):
    text = {
        'prompt' : "An archeologist tells you that it is valuble to museums, but reccomends that you donate it. Do you sell it or donate it?",
        'inputs' : [("Sell", "/display/sell"),("Donate", "/display/donate")],
    }
    return render(request, 'display/index.html', text)

def sell(request):
    text = {
        'prompt' : "You, being the greedy bastard that you are, sell the totem to the museum. You are rich! You got 200 pieces of gold for the totem.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

def donate(request):
    text = {
        'prompt' : "You donate the totem to the museum. They name the exhibit featuring your totem after you and they dedicate a scetion to your adventure.",
        'inputs' : [("End", "/display/finished")],
    }
    return render(request, 'display/index.html', text)

#def (request):
    #text = {
        #'prompt' : "",
        #'inputs' : "",
    #}
    #return render(request, 'display/index.html', text)