from sys import exit

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        choices = [0,0,0]
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(choices)
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Start(Scene):
    def enter(self, choices):
        print "Do you want to go on an adventure?"
        choice = raw_input("> ")

        if choice == "No":
            print "Ok. Go home then."
            return "finished"
        elif choice == "Yes":
            return "opening"
        else:
            print "This is a Yes or No question."
            return "start"

class Opening(Scene):
    def enter(self, choices):
        print "Use entrance or climb up the side?"
        choice = raw_input("> ")
        
        if choice == "Entrance":
            return "entrance"
           
        elif choice == "Climb up the side":
            return "up_the_side"
            
        else:
            print "Error. Type 'Entrance' or 'Climb up the side'."
            return "opening"

class Entrance(Scene):
    def enter(self, choices):
        print "Use the hole in the ground or the open corridor?"
        choice = raw_input("> ")
        
        if choice == "Hole in the ground":
            return "hole_in_the_ground"
        
        elif choice == "Open corridor":
            return "open_corridor"
        
        else:
            print "Error. Type 'Hole in the ground' or 'Open corridor'."
            return "entrance"

class Hole_in_the_Ground(Scene):
    def enter(self, choices):
        print "Do you want to lower yourself in or jump down?"
        choice = raw_input("> ")
        
        if choice == "Lower myself down":
            return "caves"
        
        elif choice == "Jump down":
            print "You jump down and break your leg. You climb out"
            print "wearily and drag yourself back to town."
            return "finished"
        
        else:
            print "Error. Type 'Lower myself down' or 'Jump down'."
            return "hole_in_the_ground"

class Caves(Scene):
    def enter(self, choices):
        print "Use a torch or a flashlight?"
        choice1 = raw_input("> ")
        
        if choice1 == "Torch":
            choice1 = 1
        
        elif choice1 == "Flashlight":
            choice1 = 0
        
        else:
            print "Error. Type 'Torch' or 'Flashlight'."
            return "caves"
        
        print ""
        print "Go in the right cave or the left cave?"
        choice2 = raw_input("> ")
        
        if choice2 == "Left cave":
            if choice1 == 1:
                print "As you enter, dozens of snakes slither up from the floor."
                print "You try to ward them off with your torch and it works"
                print "You continue your adventure."
                return "ravine_room"
            else:
                print "The wind blows the torch out and you get lost in the dark."
                return "finished"
        
        elif choice2 == "Right cave":
            if choice1 == 1:
                print "As you enter, dozens of snakes slither up from the floor."
                print "You try to ward them off with your flashlight, but it"
                print "fails. The snakes bite you until the poison numbs your"
                print "body. You cannot continue your adventure."
                return "finished"
            else:
                print "Your battery dies and you get lost in the dark"
                return "finished"



class Ravine_Room(Scene):
    def enter(self, choices):
        print "You enter a room and find a ravine blocking the exit. Do you: swing to the exit"
        print "on a rope, use a wire that crosses the room like a tightrope, or run and jump"
        print "across the ravine?"
        choice = raw_input("> ")
        
        if choice == "Swing to the exit on a rope":
            choices[0] = 0
            print "You lasso your rope to an old support beam and swing across."
            return "hallway"
        
        elif choice == "Use a wire that crosses the room like a tightrope":
            print "You try to use a wire to cross the ravine. You make it halfway"
            print "across before the wire snaps under your wieght. You fall to"
            print "your death"
            return "finished"
        
        elif choice == "Run and jump across the ravine":
            choices[0] = 1
            print "You back up to get a running start. You run at full speed and jump as far"
            print "as you can. You land on the other side and continue on."
            return "hallway"
        
        else:
            print "Error. Type 'Swing to the exit on a rope', 'Use a wire"
            print "that crosses the room like a tightrope', or 'Run and"
            print "jump across the ravine'."
            return "ravine_room"
        
class Hallway(Scene):
    def enter(self, choices):
        print "You come across a long hallway that looks safe, too safe. Do you:"
        if choices[0] == 1:
            print "use your rope to test for traps, throw a rock to test for traps,"
            print "or walk in cautiously?"
        else:
            print "throw a rock to test for traps or walk in cautiously?"
        
        choice = raw_input("> ")
        
        if choice == "Use my rope to test for traps":
            print "You roll your rope across the floor. It reveals that there is"
            print "a hidden spike trap in the floor. You avoid the trap."
            choices[1] = 0
        
        elif choice == "Throw a rock to test for traps":
            print "The rock reveals no traps. You walk in and activate a hidden"
            print "spike trap and impail your foot. You bandage your foot but"
            print "it still hurts to walk. You have a limp now."
            choices[1] = 1
            return "amulet_room"
        
        elif choice == "Walk in cautiously":
            print "You walk in catiously and accidentaly fall over. Your wieght"
            print "activates the hidden spike trap and the trap impails you."
            print "You bandage up your body but you are in a lot of pain."
            print "You decide to try and head back to town."
            return "finished"
        
        else:
            print "Error. Type 'Use my rope to test for traps', 'Throw a rock to test"
            print "for traps', or 'Walk in cautiously'."
            return "hallway"
        
class Amulet_Room(Scene):
    def enter(self, choices):
        print "In the next room, you find an amulet on a pedestal. There is an inscription"
        print "next to it. It reads, 'Beware any who wish to take this amulet for"
        print "themselves For if you leave this temple with it, you will be burdened with"
        print "a curse. You'd think I'd tell what the curse is? Ha You'll have to find that"
        print "out for yourself.' Do you take the amulet or leave it where it is?"
        choice = raw_input("> ")
        
        if choice == "Take the amulet":
            print "You pick up the amulet and look at it. There appears to be an"
            print "inscription on it. However, you decide to decipher it later."
            print "You avoid the spike trap and head back to the ravine."
            choices[2] = 1
            return "exit_scene"
        
        elif choice == "Leave the amulet":
            print "You leave the Amulet where it is, fearing whatever curse it posesses."
            print "You avoid the spike trap and head back to the ravine."
            choices[2] = 0
            return "exit_scene"
        
        else:
            print "Error. Type 'Take the amulet' or 'Leave the amulet'."
            return "amulet_room"
        
class Exit_Scene(Scene):
    def enter(self, choices):
        print "You arrive at the ravine. Do you use your rope or jump across?"
        choice = raw_input("> ")
        
        if choices[0] == 1 and choices[1] == 1:
            print "You cannot swing across and you cannot jump across. You are stuck."
            return "finished"
        
        else:
            if choice == "Use rope":
                if choices[0] == 0:
                    print "You use your rope to swing across."
                else:
                    print "You cannot attach the rope from this side."
            
            elif choice == "Jump across":
                if choices[1] == 0:
                    print "You run and jump across the ravine."
                else:
                    print "You have a limp and cannot jump across"
        
        if choices[2] == 0:
            return "no_amulet_ending"
        else:
            return "amulet_ending"

class No_Amulet_Endng(Scene):
    def enter(self, choices):
        print "Without the amulet, you have nothing to show for your adventure."
        print "You return to town, defeated."
        return "finished"

class Amulet_Ending(Scene):
    def enter(self, choices):
        print "After you exit the temple, you discover that the amulet will not"
        print "come off of your hand, no matter how hard you shake. You remember"
        print "the inscription you noticed earlier and decide to read it. The"
        print "inscription says 'So you took the amulet even after I warned you."
        print "Well, if you ever want this amulet off of your hand, you will have"
        print "to go to another temple. What fun for you' You notice a rough"
        print "sketch of a temple on the amulet. You hurry back to town to try and"
        print "find the temple that matches the drawing."
        return "finished"

class Open_Corridor(Scene):
    def enter(self, choices):
        print "Check for traps or run in?"
        choice = raw_input("> ")
        
        if choice == "Check for traps":
            print "You find a presurized floor pannel and decide to avoid it."
            print "You move on to the next room."
            return "treasure_room"
        
        elif choice == "Run in":
            print "You trigger a trip wire and the wall shoots poison darts at you."
            print "You narrowly dodge them and decide this adventure isn't worth it."
            print "You head back to town."
            return "finished"
            
        else:
            print "Error. Type 'Check for traps' or 'Run in'."
            return "open_corridor"

class Up_The_Side(Scene):
    def enter(self, choices):
        print "Do you want to use your rope or free climb it?"
        choice = raw_input("> ")
        
        if choice == "Use rope":
            print "Attach your rope to a branch or the top of the temple?"
            choice = raw_input("> ")
            
            if choice == "Branch":
                print "While you scale the temple, the branch snaps and you fall down the side."
                print "Upon landing, you twist your ankle. You can't walk very well so you hobble"
                print "back to town."
                return "finished"
                
            elif choice == "Top of the temple":
                print "The rope stays attached and you make it to the top."
                return "top_of_the_temple"
            
            else:
                print "Error. Type 'Branch' or 'Top of the temple'."
                return "up_the_side"
        
        elif choice == "Free climb it":
            print "Are you sure? Do you want to reconsider or go for it?"
            choice = raw_input("> ")
            
            if choice == "Reconsider":
                print "You think that maybe this isn't a good idea and try to think of another way."
                print "However, you begin to question all of you life choices and wonder if anything"
                print "is worth it. You decide you need to rethink your life as you go back to town."
                return "finished"
            
            elif choice == "Go for it":
                print "You decide to ignore that little voice in your head that tells you that free-"
                print "climbing an old temple is not a good idea and go for it. However, Luck is on"
                print "your side and you reach the top."
                return "top_of_the_temple"
            
            else:
                print "Error. Type 'Reconsider' or 'Go for it'."
                return "up_the_side"

class Top_Of_The_Temple(Scene):
    def enter(self, choices):
        print "Use the stairs or the spooky tunnel?"
        choice = raw_input("> ")
        
        if choice == "Stairs":
            print "You fall down the stairs and break your neck. That's it. You're dead."
            return "finished"
        
        elif choice == "Spooky tunnel":
            print "You grudgingly go down the spooky tunnel. You are startled by everything."
            print "Even a little mouse. A mouse Somehow, you make it to the next room."
            return "treasure_room"
        
        else:
            print "Error. Type 'Stairs' or 'Spooky tunnel'."
            return "top_of_the_temple"

class Treasure_Room(Scene):
    def enter(self, choices):
        print "You find yourself in a room full of treasure Do you want to take the"
        print "treasure chest, the totem on a pedestal, or the sack?"
        choice = raw_input("> ")
        
        if choice == "Treasure chest":
            return "treasure_chest"
        elif choice == "Totem on pedestal":
            return "totem_on_pedestal"
        elif choice == "Sack":
            print "You take the sack an leave the temple with ease. You open the sack"
            print "to reveal that there is some gold and some jewels inside. You are rich!"
            print "You got 100 pieces of gold from the sack."
            return "finished"
        else:
            print "Error. Type 'Treasure chest', 'Totem on pedestal', or 'sack'."

class Treasure_Chest(Scene):
    def enter(self, choices):
        print "As you pick up the chest, the room starts collapsing around you."
        print "Do you go through the right or left cave?"
        choice = raw_input("> ")
        
        if choice == "Right cave":
            print "You escape the temple as it crumbles to the ground. You open"
            print "the chest and find that it is full of gold. You are rich!"
            print "You got 600 pieces of gold from the chest."
            return "finished"
        
        elif choice == "Left cave":
            print "Do you go through a narrow tunnel or turn back?"
            choice = raw_input("> ")
            
            if choice == "Narrow tunnel":
                print "You squeeze through the tunnel, but only barley make it out. In the process, you"
                print "break your foot. You open the chest and find that it is full of gold."
                print "Do you leave some behind to lighten your load or keep it all?"
                choice = raw_input("> ")
                
                if choice == "Lighten your load":
                    print "You empty some gold out of the chest to make your journey easier. You"
                    print "make it back with plenty of energy so nobody bothers you. You have to pay"
                    print "for the medical expenses for your foot. You are rich! You get 300 pieces of"
                    print "gold from the chest."
                    return "finished"
                
                elif choice == "Keep it all":
                    print "You dedide to keep all of your gold. The journey back is arduous, so you"
                    print "return with little energy. Local thugs notice your lack of energy and"
                    print "jump you. You lose almost all of your gold. You use the remaining gold to"
                    print "pay for medical expenses for your foot. You get nothing"
                    return "finished"
                
                else:
                    print "Error. Type 'Lighten your load' or 'Keep it all'."
                    return "treasure_chest"
            
            elif choice == "Turn back":
                print "You try to go the other way, but you get caught in the falling debris and are"
                print "crushed."
                return "finished"
            
            else:
                print "Error. Type 'Narrow tunnel' or 'Turn back'."
                return "treasure_chest"
        
        else:
            print "Error. Type 'Right cave' or 'Left cave'."
            return "treasure_chest"
    
class Totem_On_Pedestal(Scene):
    def enter(self, choices):
        print "A boulder falls through the ceiling and rolls towards you."
        print "Go through the right cave or the left cave?"
        choice = raw_input("> ")
        
        if choice == "Right cave":
            print "You escape the temple as it crumbles to the ground."
            return "sell_or_donate"
        
        elif choice == "Left cave":
            print "Do you go through a narrow tunnel or turn back?"
            choice = raw_input("> ")
            
            if choice == "Narrow tunnel":
                print "You squeeze through the tunnel, but only barley make it out. In the"
                print "process, you break your foot. Do you leave the totem behind to lighten"
                print "your load or take it with you?"
                choice = raw_input("> ")
                
                if choice == "Leave totem behind":
                    print "You return to town empty handed. You went on an amazing adventure but have"
                    print "nothing to show for it."
                    return "finished"
                
                elif choice == "Take totem with you":
                    print "You dedide to keep the totem. The journey back is tedious with the added weight,"
                    print "but you still return with some energy. Nobody bothers you. You return to town"
                    print "with the strange artifact."
                    return "sell_or_donate"
                
                else:
                    print "Error. Type 'Leave totem behind' or 'Take totem with you'."
                    return "totem_on_pedestal"
            
            elif choice == "Turn back":
                print "You try to go the other way, but you get squished by the boulder."
                return "finsihed"
            
            else:
                print "Error. Type 'Narrow tunnel' or 'Turn back'."
                return "totem_on_pedestal"
        
        else:
            print "Error. Type 'Right cave' or 'Left cave'."
            return "totem_on_pedestal"

class Sell_Or_Donate(Scene):
    def enter(self, choices):
        print "An archeologist tells you that it is valuble to"
        print "museums, but reccomends that you donate it."
        print "Do you sell it or donate it?"
        choice = raw_input("> ")
        
        if choice == "Sell":
            print "You sell the totem to the museum. You greedy bastard! You are rich!"
            print "You got 200 pieces of gold for the totem."
            return "finished"
        
        elif choice == "Donate":
            print "You donate the totem to the museum. They name the exhibit featuring the"
            print "totem in your name and you have your own section that depicts your adventure."
            return "finished"
        
        else:
            print "Error. Type 'Sell' or 'Donate"
            return "sell_or_donate"

class Finished(Scene):
    def enter(self, choices):
        print "Your adventure is over."
        return "finished"

class Map(object):
    
    scenes = {
        'start': Start(),
        'opening': Opening(),
        'entrance': Entrance(),
        'hole_in_the_ground': Hole_in_the_Ground(),
        'caves': Caves(),
        'ravine_room': Ravine_Room(),
        'hallway': Hallway(),
        'amulet_room': Amulet_Room(),
        'exit_scence': Exit_Scene(),
        'no_amulet_ending': No_Amulet_Endng(),
        'amulet_ending': Amulet_Ending(),
        'open_corridor': Open_Corridor(),
        'up_the_side': Up_The_Side(),
        'top_of_the_temple': Top_Of_The_Temple(),
        'treasure_room': Treasure_Room(),
        'treasure_chest': Treasure_Chest(),
        'totem_on_pedestal': Totem_On_Pedestal(),
        'sell_or_donate': Sell_Or_Donate(),
        'finished': Finished(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
a_game.play()