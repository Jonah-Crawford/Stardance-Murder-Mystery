define craw = Character("Craw")
define nayte = Character("Nayte")
define rupnil = Character("Rupnil")
define keyboard = Character("Keyboard")
define fazin = Character("Fazin")
define jam = Character("Jam")

define narrator = Character(None)

default player_name = "You"

define player = Character("[player_name]")

default met_nayte = False
default met_rupnil = False
default met_keyboard = False
default met_fazin = False
default met_jam = False

default saw_programme = False
default saw_cable = False
default saw_power_bank = False
default heard_wifi_question = False
default saw_fs_message = False


label start:
  scene black

  narrator "19:00."

  narrator "For months, Stardance had existed almost entirely as messages, commits, project pages and questionable uses of compute time."

  narrator "Tonight, for once, everyone was in the same room."

  narrator "The occasion was the release of Crawssembly 2.0, a programming language written by 'The Craw'."

  narrator "Although calling it a Crawssembly launch was slightly unfair."

  narrator "Half the room had brought projects of their own."

  narrator "Laptops covered almost every available table."

  narrator "Someone had found speakers."

  narrator "Someone else had found considerably more extension leads than seemed safe."

  narrator "And at the far end of the room, a small stage had been assembled for the main presentation."

  $ player_name = renpy.input("What's your name?", default="").strip()

  if player_name == "":
    $ player_name = "You"

  narrator "You had arrived early enough to catch the end of setup, but late enough to avoid being given anything important to do."

  narrator "Probably ideal."

  jump party_hub


label party_hub:
  scene black

  if met_nayte and met_rupnil and met_keyboard and met_fazin and met_jam:
    jump party_transition

  narrator "The launch doesn't begin for a while yet."

  narrator "You look around the room."

  menu:
    "Talk to Nayte" if not met_nayte:
      jump meet_nayte

    "Talk to Rupnil" if not met_rupnil:
      jump meet_rupnil

    "Talk to Keyboard" if not met_keyboard:
      jump meet_keyboard

    "Talk to Fazin" if not met_fazin:
      jump meet_fazin

    "Talk to Jam" if not met_jam:
      jump meet_jam

    "Look at the event programme" if not saw_programme:
      jump inspect_programme


label meet_nayte:
  $ met_nayte = True

  narrator "Nayte is sitting beside a laptop, apparently engaged in an argument with a terminal."

  player "What are you using?"

  nayte "zed btw"

  player "Of course."

  nayte "nano >> vim"

  player "Craw would approve."

  nayte "just use :qa"

  player "That's Vim."

  nayte "yeah"

  narrator "Nayte looks back at the screen."

  narrator "You decide not to investigate the contradiction."

  jump party_hub


label meet_rupnil:
  $ met_rupnil = True

  narrator "Rupnil is looking through a Git repository."

  player "What are you working on?"

  rupnil "Nothing important."

  player "That sounds reassuring."

  rupnil "Craw's been asking me weird programming questions all afternoon."

  player "How weird?"

  rupnil "Craw weird."

  player "Ah."

  rupnil "He gave me a small routine to write for the presentation."

  player "What does it do?"

  rupnil "No idea."

  player "You wrote it."

  rupnil "I know what the code does."

  rupnil "I don't know why he wants it."

  player "Fair distinction."

  narrator "Rupnil closes the repository."

  rupnil "Also you literally cannot get anything with fraud."

  player "What?"

  rupnil "Nothing."

  jump party_hub


label meet_keyboard:
  $ met_keyboard = True

  narrator "Keyboard is standing beside a second laptop and staring at a terminal window."

  keyboard "i forgot to turn on my ssh server"

  player "Strong start."

  keyboard "fixed now"

  narrator "A successful connection appears."

  keyboard "Craw wanted me to test whether this thing stays reachable from downstairs."

  player "Downstairs?"

  keyboard "basement"

  $ heard_wifi_question = True

  player "Why does Crawssembly need basement Wi-Fi?"

  keyboard "idk"

  keyboard "probably something for the demo"

  player "Naturally."

  narrator "Keyboard types something else."

  keyboard "ssh craw@92.23x.xx.xxx"

  player "Is that actually Craw's address?"

  keyboard "no"

  player "Good."

  jump party_hub


label meet_fazin:
  $ met_fazin = True

  narrator "Fazin is standing near the lighting controls."

  player "Are you responsible for all this?"

  fazin "some of it"

  player "That answer inspires confidence."

  fazin "Craw wanted the ending to be dramatic"

  player "How dramatic?"

  fazin "lights"

  fazin "sound"

  fazin "smoke"

  player "That seems excessive for a programming language."

  fazin "ppl like to be niche and different yk"

  player "Apparently."

  fazin "its a really brandable name too"

  player "Smoke?"

  fazin "huh?"

  player "Never mind."

  jump party_hub


label meet_jam:
  $ met_jam = True

  narrator "Jam is crouched beside an open equipment case."

  player "What have you got there?"

  jam "controller board"

  player "For your project?"

  jam "no"

  player "Craw's?"

  jam "sure"

  player "Do you know what he's using it for?"

  jam "no"

  jam "he asked for two relay outputs"

  player "And you just gave him one?"

  jam "yeah"

  player "Reasonable."

  jam "is there a url that needs shortening?"

  player "Not currently."

  jam "ok"

  jump party_hub


label inspect_programme:
  $ saw_programme = True

  narrator "A printed programme has been left on one of the tables."

  narrator "19:30 — Stardance project showcase"

  narrator "20:00 — Crawssembly 2.0"

  narrator "20:30 — Launch complete"

  narrator "Various project names fill the space between."

  narrator "Someone has added a handwritten note beneath the schedule."

  narrator "\"PLEASE DO NOT SHIP DURING PRESENTATIONS\""

  narrator "Someone else has crossed out \"DO NOT\"."

  jump party_hub


label party_transition:
  scene black

  narrator "19:09."

  narrator "A notification sounds nearby."

  narrator "Craw glances down at his phone."

  narrator "For just a moment, his expression changes."

  player "Everything alright?"

  craw "Yep."

  narrator "He locks the screen almost immediately."

  $ saw_fs_message = True

  player "That was convincing."

  craw "I'm glad."

  player "What was it?"

  craw "Nothing important."

  narrator "Before you can ask anything else, somebody calls Craw from across the room."

  craw "I've got approximately twenty things left to do."

  craw "Enjoy yourself."

  player "I'll try."

  narrator "He disappears into the crowd."

  jump project_showcase


label project_showcase:
  scene black

  narrator "19:30."

  narrator "The project showcase begins."

  narrator "For the next twenty minutes, the room becomes a rapid sequence of demonstrations."

  narrator "Websites."

  narrator "Hardware."

  narrator "Games."

  narrator "Tools whose purposes become less clear the longer their creators explain them."

  narrator "Craw spends most of it near the back of the audience."

  narrator "Almost."

  narrator "At 19:50, you notice him get up."

  narrator "He walks over to his laptop."

  narrator "Types something."

  narrator "Waits."

  narrator "Then closes the terminal and returns."

  player "What was that?"

  craw "Arming the nuclear device."

  player "Right."

  craw "You asked."

  narrator "He sits back down."

  narrator "There are ten minutes until his presentation."

  jump final_conversation


label final_conversation:
  scene black

  narrator "19:55."

  craw "How's the evening been?"

  player "Nobody has set anything on fire."

  craw "Yet."

  player "Are you nervous?"

  craw "Not really."

  craw "I've run the presentation enough times."

  player "Including whatever the final demonstration is?"

  craw "Especially that."

  player "Nobody will tell me what it is."

  craw "That would rather defeat the purpose of a surprise."

  narrator "Someone near the stage gestures towards Craw."

  craw "That's me."

  player "Good luck."

  craw "Thanks."

  craw "I'll see you after the presentation."

  narrator "Craw walks towards the stage."

  narrator "You don't think anything of the wording."

  jump crawssembly_presentation


label crawssembly_presentation:
  scene black

  narrator "20:00."

  narrator "The lights dim."

  craw "Right."

  craw "Hello, everyone."

  craw "For anyone who somehow arrived here without knowing why we're here..."

  craw "This is Crawssembly."

  narrator "A title appears on the projector."

  narrator "CRAWSSEMBLY 2.0"

  craw "The original idea was fairly simple."

  craw "Assembly languages are powerful."

  craw "They're also very good at making people decide they no longer want to learn assembly languages."

  craw "So the goal was to build something low-level enough that you can see what the machine is actually doing..."

  craw "...without requiring you to fight the machine before you've even started."

  narrator "He works through several demonstrations."

  narrator "Graphics."

  narrator "Memory."

  narrator "Networking."

  narrator "A few features produce applause."

  narrator "One produces a noise from the speakers that Craw insists was intentional."

  craw "And that brings us to 2.0."

  narrator "The final slide appears."

  craw "A rather unreasonable amount has changed."

  craw "Some of you in this room are responsible for parts of it."

  craw "Some of you are responsible for bugs in it."

  craw "You know who you are."

  narrator "A few people laugh."

  craw "But there's one last thing."

  narrator "Craw glances towards his laptop."

  craw "I promised a final demonstration."

  craw "So."

  craw "Let's make it memorable."

  jump apparent_murder


label apparent_murder:
  scene black

  narrator "20:07:03."

  narrator "The lights go out."

  pause 1.0

  narrator "20:07:04."

  narrator "{size=+12}CRASH.{/size}"

  pause 1.0

  narrator "For several seconds, nobody moves."

  narrator "Then the emergency lights flicker on."

  narrator "Craw is lying on the stage."

  narrator "There is blood beneath him."

  player "Craw?"

  narrator "Someone screams."

  narrator "Several people rush forwards at once."

  narrator "Then smoke begins pouring across the stage."

  fazin "wait"

  fazin "THATS NOT SUPPOSED TO—"

  narrator "An alarm starts."

  narrator "The room erupts."

  narrator "People are pushed towards the exits."

  narrator "You lose sight of the stage."

  scene black

  narrator "20:08."

  narrator "Outside, nobody seems quite certain what just happened."

  nayte "is craw dead"

  keyboard "what the"

  rupnil "BRO WHAAA"

  jam "..."

  fazin "no no no"

  narrator "Someone calls for help."

  narrator "Someone else is already trying to get back inside."

  player "He's still in there."

  narrator "The smoke begins to clear."

  narrator "You follow the others back towards the stage."

  narrator "The emergency lights are still on."

  narrator "The laptop is still running."

  narrator "The blood is still there."

  narrator "But Craw isn't."

  pause 1.0

  player "Where's the body?"

  narrator "Nobody answers."

  jump act_one_begin


label act_one_begin:
  scene black

  narrator "20:10."

  narrator "Ten minutes ago, this was a launch party."

  narrator "Now Craw is missing."

  narrator "There is blood on the stage."

  narrator "Nobody saw what happened during the blackout."

  narrator "And somehow, during the evacuation..."

  narrator "the body disappeared."

  centered "{size=+20}ACT I{/size}"

  centered "{size=+12}WHO KILLED CRAW?{/size}"

  narrator "To be continued."

  return