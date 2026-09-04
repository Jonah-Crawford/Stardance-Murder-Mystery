define bird      = Character("BirBuh")
define capy      = Character("Capy")
define craw      = Character("Craw")
define fazin     = Character("Fazin")
define gizzy     = Character("Gizzy")
define gl2011    = Character("GameLord")
define jam       = Character("Jam")
define keyboard  = Character("Keyboard")
define louis     = Character("Louis")
define matei     = Character("Matei")
define mixid     = Character("Mixid")
define nayte     = Character("Nayte")
define rupnil    = Character("Rupnil")
define tej       = Character("Tejaswa")
define trkl      = Character("Trkl")
define water     = Character("Water")

define narrator  = Character(None)
define unknown   = Character("???")

default player_name = "You"

define player = Character("[player_name]")

default saw_programme = False
default saw_cable = False
default saw_power_bank = False
default heard_wifi_question = False
default saw_fs_message = False

default current_act = 0
default collected_evidence = []

init python:
  evidence_data = {
    "Programme Schedule": [
      "The timetable for the Stardance Party",
      "The launch was supposed to be complete by 20:30",
      "The launch was supposed to be complete by 20:30"
    ],

    "Blood Sample": [
      "A small sample of Craw's blood, waiting on analysis",
      "The substance found on the stage was theatrical blood",
      "The substance found on the stage was theatrical blood"
    ],

    "Weapon Missing": [
      "No obvious murder weapon can be found",
      "No murder weapon was ever found",
      "There was no murder weapon"
    ],

    "Effects Log": [
      "Craw's laptop triggered several stage effects at 20:07",
      "The blackout, sound and smoke were deliberately programmed",
      "The blackout, sound and smoke were part of Craw's plan"
    ],

    "Fraud Squad Message": [
      "Craw received an unusual notification shortly before the presentation",
      "The message concerned an active Fraud Squad investigation",
      "The Fraud Squad investigation gave Craw a reason to disappear"
    ],

    "Scheduled Messages" : [
      "Craw told Nayte to stop making scheduled messages after 20:30",
      "Craw expected to be available by 20:30",
      "Craw expected to be available by 20:30"
    ],

    "Basement System" : [
      "The basement shows evidence of being used by the murderer",
      "Craw used the basement to disappear",
      "Craw used the basement to disappear"
    ]

  }

  def add_evidence(evidence):
    evidence = evidence.title()

    if evidence not in collected_evidence:
      collected_evidence.append(evidence)
      renpy.notify("Evidence added: " + evidence)

  def get_evidence(evidence):
    try:
      return evidence_data[evidence.title()][current_act]
    except:
      return evidence.title()


label start:
  scene black

  pause 1.0

  transform definition_fade:
    on show:
      alpha 0.0
      linear 0.75 alpha 1.0

    on hide:
      linear 0.75 alpha 0.0

  screen centered_left_text(text):
    modal True

    key "dismiss" action [
      Hide("centered_left_text", transition=Dissolve(0.75)),
      Return()
    ]

    button:
      xfill True
      yfill True
      background None
      action [
        Hide("centered_left_text", transition=Dissolve(0.75)),
        Return()
      ]

    frame:
      xalign 0.5
      yalign 0.5
      background None

      text text:
        text_align 0.0

  call screen centered_left_text(
    "{font=TimesNewRoman.ttf}Fraud Squad\n\n  Fraud {i}noun{/i} {font=DejaVuSerif.ttf}{size=-5}/frɔːd/{/size}{font=TimesNewRoman.ttf}\n     the crime of getting money by deceiving people\n\n  Squad {i}noun{/i} {font=DejaVuSerif.ttf}{size=-5}/skwɒd/{/size}{font=TimesNewRoman.ttf}\n     a small group of people trained to work together as a unit{/font}\n\n\n\n\n\n\n{/font}click to continue{/font}"
  ) with Dissolve(0.75)

  pause 1.0

  narrator "19:00"

  scene launch_hall
  with dissolve

  narrator "For months, Stardance had existed almost entirely as messages, commits, project pages and questionable uses of compute time"

  narrator "Tonight, for once, everyone was in the same room"

  narrator "The occasion was the release of Crawssembly 2.0, a programming language written by 'The Craw'"

  narrator "Although calling it a Crawssembly launch was unfair"

  narrator "Half the room had brought projects of their own"

  narrator "Laptops covered almost every available table"

  narrator "Someone had found speakers"

  narrator "Someone else had found considerably more extension leads than seemed safe"

  narrator "And at the far end of the room, a small stage had been assembled for the main presentation"

  $ player_name = renpy.input("What's your name?", default="").strip()

  if player_name == "":
    $ player_name = "You"

  narrator "You had arrived early enough to catch the end of setup, but late enough to avoid being given anything important to do"

  narrator "Probably ideal"

  transform pfp:
    xalign 0.5
    yalign 0.42
    zoom 0.8

  transform pfp_left:
    xalign 0.15
    yalign 0.42
    zoom 0.8

  transform pfp_right:
    xalign 0.85
    yalign 0.42
    zoom 0.8

  transform pfp_big:
    xalign 0.5
    yalign 0.42
    zoom 1.5

  show craw at pfp
  with dissolve

  craw "Hey [player_name], I'm glad you could come! We've had a great turnout, thanks to your help. We couldn't have done it without you"

  player "This looks very professional Craw"

  craw "Well it wasn't all me of course. Like merge sort, we've divided and conquered"

  player "{i}Did he seriously come up with that on the spot?{/i}"

  craw "Preparing for this has given me a good distraction from... well.."

  narrator "Craw seems to come closer and lowers his voice"

  hide craw
  with dissolve

  show craw at pfp_big
  with dissolve

  craw "A distraction from this Fraud Squad investigation on me, I've got a meeting with them after this"

  hide craw
  with dissolve

  show craw at pfp
  with dissolve

  craw "Anyways, I hope you enjoy the many projects Stardancers have created"

  narrator "Craw smiles and leaves you to explore the room"

  hide craw
  with dissolve

  jump party_hub


default met_nayte = False
default met_rupnil = False
default met_keyboard = False
default met_fazin = False
default met_jam = False


label party_hub:
  scene launch_hall

  if met_nayte and met_rupnil and met_keyboard and met_fazin and met_jam:
    jump party_transition

  narrator "The launch doesn't look ready yet"

  narrator "You look around the room"

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

  scene launch_hall

  show nayte at pfp
  with dissolve

  narrator "Nayte is sitting beside a laptop, apparently engaged in an argument with a terminal"

  player "What are you using?"

  nayte "Zed"

  player "Of course"

  nayte "Nano is better than Vim"

  player "Craw would approve"

  nayte "Just use :qa"

  player "That's Vim"

  nayte "Yeah"

  show tej at pfp_left
  with dissolve

  tej "Emacs is better though"

  player "Where did you come from??"

  show louis at pfp_right
  with dissolve

  louis "Nvim >>>>"

  player "Is this a mass ping in real life?"

  pause 1.0

  hide tej
  with dissolve

  hide louis
  with dissolve

  narrator "Nayte looks back at the screen, unfazed"

  pause 1.0

  player "...I'll leave you to it then"

  hide nayte
  with dissolve

  jump party_hub


label meet_rupnil:
  $ met_rupnil = True

  scene launch_hall

  show rupnil at pfp
  with dissolve

  narrator "Rupnil is looking through a Git repository"

  player "What are you working on?"

  rupnil "Nothing important"

  player "That sounds reassuring"

  rupnil "Craw's been asking me weird programming questions all afternoon"

  player "How weird?"

  rupnil "Craw weird"

  player "Ah"

  rupnil "He gave me a small routine to write for the presentation"

  player "What does it do?"

  rupnil "No idea"

  player "But you wrote it?"

  rupnil "I know what the code does"

  rupnil "I don't know why he wants it"

  player "Fair distinction"

  hide rupnil
  with dissolve

  jump party_hub


label meet_keyboard:
  $ met_keyboard = True

  scene launch_hall

  show keyboard at pfp
  with dissolve

  narrator "Keyboard is standing beside a second laptop and staring at a terminal window"

  keyboard "Ahh I forgot to turn on my ssh server"

  player "Strong start"

  keyboard "Fixed now"

  narrator "A successful connection appears"

  keyboard "Craw wanted me to test whether this thing stays reachable from downstairs"

  player "Downstairs?"

  keyboard "The basement"

  $ heard_wifi_question = True

  player "Why does Crawssembly need basement Wi-Fi?"

  keyboard "I don't know"

  keyboard "Probably something for the demo"

  player "Naturally... I've heard lots about it"

  narrator "Keyboard types something else"

  keyboard "ssh craw@92.237 blah blah blah"

  player "Is that actually Craw's address?"

  keyboard "idk"

  player "lol ok"

  hide keyboard
  with dissolve

  jump party_hub


label meet_fazin:
  $ met_fazin = True

  scene launch_hall

  show fazin at pfp
  with dissolve

  narrator "Fazin is standing near the lighting controls"

  player "Are you responsible for all this?"

  fazin "Some of it"

  player "That answer inspires confidence"

  fazin "Craw wanted the ending to be dramatic"

  player "How dramatic?"

  fazin "Lights"

  fazin "Sound"

  fazin "Smoke"

  player "That seems excessive for a programming language"

  fazin "People like to be niche and different I guess"

  player "Apparently"

  fazin "It's a really brandable name too"

  player "Smoke...?"

  fazin "Huh?"

  player "Never mind"

  hide fazin
  with dissolve

  jump party_hub


label meet_jam:
  $ met_jam = True

  scene launch_hall

  show jam at pfp
  with dissolve

  narrator "Jam is crouched beside an open equipment case"

  player "What have you got there?"

  jam "Controller board"

  player "For your project?"

  jam "No"

  player "Craw's?"

  jam "Sure"

  player "Do you know what he's using it for?"

  jam "No"

  jam "He asked for two relay outputs"

  player "And you just gave him one?"

  jam "Yeah"

  player "Reasonable"

  jam "Is there a url that needs shortening?"

  player "Not currently"

  jam "Ok :("

  hide jam
  with dissolve

  jump party_hub


label inspect_programme:
  $ saw_programme = True

  narrator "A printed programme has been left on one of the tables"

  narrator "19:30 — Stardance project showcase"

  narrator "20:00 — Crawssembly 2.0"

  narrator "20:30 — Launch complete"

  narrator "Various project names fill the space between"

  narrator "Someone has added a handwritten note beneath the schedule"

  narrator "\"PLEASE DO NOT SHIP DURING PRESENTATIONS\""

  narrator "Someone else has crossed out \"DO NOT\""

  jump party_hub


label party_transition:
  scene launch_hall

  narrator "19:09"

  narrator "A notification sounds nearby"

  show craw at pfp
  with dissolve

  narrator "Craw glances down at his phone"

  narrator "For just a moment, his expression changes"

  player "Everything alright?"

  craw "Yep"

  narrator "He locks the screen almost immediately"

  $ saw_fs_message = True

  player "That was convincing"

  craw "I'm glad"

  player "What was it?"

  craw "Nothing important"

  narrator "Before you can ask anything else, somebody calls Craw from across the room"

  craw "I've got approximately twenty things left to do"

  craw "Enjoy yourself"

  hide craw
  with dissolve

  narrator "He disappears into the crowd"

  jump project_showcase


label project_showcase:
  scene stage
  with dissolve

  narrator "19:30"

  narrator "The project showcase begins"

  narrator "For the next twenty minutes, the room becomes a rapid sequence of demonstrations"

  narrator "Websites"

  narrator "Hardware"

  narrator "Games"

  narrator "Tools whose purposes become less clear the longer their creators explain them"

  narrator "Craw spends most of it near the back of the audience"

  narrator "Almost"

  narrator "At 19:50, you notice him get up"

  narrator "He walks over to his laptop"

  narrator "Types something"

  narrator "Waits"

  narrator "Then closes the terminal and returns"

  show craw at pfp
  with dissolve

  player "What was that?"

  craw "Arming the nuclear device"

  player "Right"

  craw "You asked"

  hide craw
  with dissolve

  narrator "He sits back down"

  narrator "There are ten minutes until his presentation"

  jump final_conversation


label final_conversation:
  scene stage

  narrator "19:55"

  show craw at pfp
  with dissolve

  craw "How's the evening been?"

  player "Nobody has set anything on fire"

  craw "Yet"

  player "Are you nervous?"

  craw "Not really"

  craw "I've run the presentation enough times"

  player "Including whatever the final demonstration is?"

  craw "Especially that"

  player "Nobody will tell me what it is"

  craw "That would rather defeat the purpose of a surprise"

  narrator "Someone near the stage gestures towards Craw"

  craw "That's me"

  player "Good luck"

  craw "Thanks"

  craw "I'll see you after the presentation"

  hide craw
  with dissolve

  narrator "Craw walks towards the stage"

  narrator "You don't think anything of the wording"

  jump crawssembly_presentation


label crawssembly_presentation:
  scene stage

  narrator "20:00"

  narrator "The lights dim"

  show craw at pfp
  with dissolve

  craw "Right"

  craw "Hello, everyone"

  craw "For anyone who somehow arrived here without knowing why we're here"

  craw "This is Crawssembly"

  narrator "A title appears on the projector"

  narrator "CRAWSSEMBLY 2.0"

  craw "The original idea was fairly simple"

  craw "Assembly languages are powerful"

  craw "They're also very good at making people decide they no longer want to learn assembly languages"

  craw "So the goal was to build something low-level enough that you can see what the machine is actually doing"

  craw "...without requiring you to fight the machine before you've even started"

  narrator "He works through several demonstrations"

  narrator "Graphics"

  narrator "Memory"

  narrator "Networking"

  narrator "A few features produce applause"

  narrator "One produces a noise from the speakers that Craw insists was intentional"

  craw "And that brings us to 2.0"

  narrator "The final slide appears"

  craw "A rather unreasonable amount has changed"

  craw "Some of you in this room are responsible for parts of it"

  craw "Some of you are responsible for bugs in it"

  craw "You know who you are"

  narrator "A few people laugh"

  craw "But there's one last thing"

  narrator "Craw glances towards his laptop"

  craw "I promised a final demonstration"

  craw "So"

  craw "Let's make it memorable"

  jump apparent_murder


label apparent_murder:
  scene stage

  narrator "20:07:03"

  scene black

  narrator "The lights go out"

  pause 1.0

  narrator "20:07:04"

  narrator "{size=+12}CRASH.{/size}"

  pause 1.0

  narrator "For several seconds, nobody moves"

  scene stage
  show craw at pfp
  with vpunch

  narrator "Then the emergency lights flicker on"

  narrator "Craw is lying on the stage"

  narrator "There is blood beneath him"

  player "Craw?"

  narrator "Someone screams"

  narrator "Several people rush forwards at once"

  narrator "Then smoke begins pouring across the stage"

  fazin "Wait"

  fazin "THATS NOT SUPPOSED TO-"

  narrator "An alarm starts"

  narrator "The room erupts"

  narrator "People are pushed towards the exits"

  narrator "You lose sight of the stage"

  scene black
  with fade

  hide craw

  narrator "20:08"

  narrator "Outside, nobody seems quite certain what just happened"

  nayte "Craw dead?"

  keyboard "what the"

  rupnil "BRO WHAAA"

  jam "..."

  fazin "No no no"

  narrator "Someone calls for help"

  narrator "Someone else is already trying to get back inside"

  player "He's still in there"

  narrator "The smoke begins to clear"

  scene stage
  with fade

  narrator "You follow the others back towards the stage"

  narrator "The emergency lights are still on"

  narrator "The laptop is still running"

  narrator "The blood is still there"

  narrator "But Craw isn't"

  pause 1.0

  player "Where's the body?"

  narrator "Nobody answers"

  jump act_one_begin


label act_one_begin:
  scene stage

  narrator "Ten minutes ago, this was a launch party"

  narrator "Now Craw is missing"

  narrator "There is blood on the stage"

  narrator "Nobody saw what happened during the blackout"

  narrator "And somehow, during the evacuation"

  narrator "the body disappeared"

  scene black

  pause 1.0

  centered "{size=+12}WHO KILLED CRAW?{/size}"

  pause 1.0

  scene launch_hall
  with fade

  jump investigation_hub


default investigated_stage = False
default investigated_laptop = False
default questioned_witnesses = False


label investigation_hub:
  scene launch_hall

  if investigated_stage and investigated_laptop and questioned_witnesses:
    jump first_investigation_complete

  narrator "There are still too many unanswered questions"

  menu:
    "Investigate the stage" if not investigated_stage:
      jump investigate_stage

    "Inspect Craw's laptop" if not investigated_laptop:
      jump investigate_laptop

    "Question witnesses" if not questioned_witnesses:
      jump question_witnesses


label investigate_stage:
  $ investigated_stage = True

  scene stage
  with dissolve

  narrator "You approach the stage"

  narrator "People have mostly backed away from the spot where Craw fell"

  narrator "The emergency lights give everything an unpleasant red tint"

  narrator "The blood is still there"

  player "If someone attacked him here"

  narrator "You look around the floor"

  narrator "Nothing"

  narrator "No knife"

  narrator "No gun"

  narrator "No obvious blunt object"

  narrator "Nothing that looks remotely capable of explaining what you saw"

  $ add_evidence("Weapon Missing")

  player "So where's the weapon?"

  narrator "Nobody nearby seems to have an answer"

  narrator "You crouch beside the blood"

  narrator "There isn't much you can determine just by looking at it"

  narrator "You take a small sample"

  $ add_evidence("Blood Sample")

  $ details = get_evidence("Blood Sample")

  narrator "Blood Sample: [details]"

  player "Not exactly conclusive"

  narrator "But if Craw was injured here, this is the only physical trace he left behind"

  jump investigation_hub


label investigate_laptop:
  $ investigated_laptop = True

  scene stage
  with dissolve

  narrator "Craw's laptop is still sitting beside the stage"

  narrator "The terminal he used during the presentation is still open"

  player "He was typing something here at 19:50"

  narrator "You scroll backwards through the terminal output"

  narrator "Most of it is incomprehensible"

  narrator "Build logs"

  narrator "Network messages"

  narrator "Crawssembly output"

  narrator "Then you notice several lines carrying timestamps"

  narrator "20:07:03 — LIGHTING BLACKOUT"

  narrator "20:07:04 — AUDIO IMPACT"

  narrator "20:07:09 — STAGE SMOKE"

  pause 0.5

  player "..."

  player "Those aren't logs from after the fact"

  narrator "The commands were prepared before the presentation"

  $ add_evidence("Effects Log")

  player "Somebody deliberately programmed everything that happened"

  narrator "The blackout"

  narrator "The crash"

  narrator "Even the smoke"

  player "Fazin"

  narrator "You remember your conversation before the presentation"

  scene launch_hall_flashback
  with dissolve

  show fazin at pfp
  with dissolve

  fazin "{i}Craw wanted the ending to be dramatic{/i}"

  fazin "{i}Lights{/i}"

  fazin "{i}Sound{/i}"

  fazin "{i}Smoke{/i}"

  hide fazin
  with dissolve

  scene launch_hall
  with dissolve

  player "Right"

  narrator "That suddenly sounds considerably less innocent"

  jump investigation_hub


label question_witnesses:
  $ questioned_witnesses = True

  scene launch_hall
  with dissolve

  narrator "The room is full of people trying to reconstruct the same seven seconds"

  narrator "Unfortunately, almost everyone has a different version"

  show matei at pfp
  with dissolve

  player "Did you actually see anyone near Craw when the lights went out?"

  matei "No"

  player "Nothing?"

  matei "It was dark"

  player "Fair"

  hide matei
  with dissolve

  show capy at pfp
  with dissolve

  capy "I saw Craw leave the audience earlier"

  player "When?"

  capy "Before his presentation"

  player "Around 19:50?"

  capy "Probably"

  player "Where did he go?"

  capy "His laptop"

  player "I saw that too"

  hide capy
  with dissolve

  narrator "Nothing useful"

  narrator "Then you remember something from much earlier"

  scene launch_hall_flashback
  with dissolve

  show craw at pfp
  with dissolve

  narrator "19:09"

  narrator "A notification"

  narrator "Craw looking at his phone"

  narrator "His expression changing"

  craw "{i}Nothing important{/i}"

  hide craw
  with dissolve

  scene launch_hall
  with dissolve

  narrator "At the time, it hadn't seemed worth pursuing"

  narrator "Now almost everything seems worth pursuing"

  $ add_evidence("Fraud Squad Message")

  player "What exactly did you get yourself into, Craw?"

  jump investigation_hub


label first_investigation_complete:

  narrator "You stop and try to put everything together"

  narrator "Craw collapsed during a blackout"

  narrator "There is blood, but no weapon"

  narrator "The blackout was programmed"

  narrator "So were the crash and the smoke"

  narrator "And shortly before all of this, Craw received a message he refused to explain"

  player "The blackout wasn't an accident"

  player "Someone planned this"

  pause 1.0

  player "And I know who controlled the effects"

  narrator "{b}Fazin{/b}"

  jump confront_fazin


label confront_fazin:
  scene launch_hall

  show fazin at pfp
  with dissolve

  player "Fazin"

  fazin "Huh?"

  player "We need to talk about the stage effects"

  fazin "What about them?"

  player "The blackout happened at exactly 20:07:03, according to Craw's laptop"

  fazin "Yeah, that sounds about right"

  player "The impact sound happened one second later"

  fazin "..."

  player "Then the smoke started"

  fazin "..."

  player "That sequence was programmed"

  fazin "I know"

  pause 1.0

  player "You know?"

  fazin "I made it"

  pause 1.0

  player "You made the blackout in which Craw was apparently murdered"

  fazin "When you say it like that it sounds bad"

  player "How else would you like me to say it?"

  fazin "Idk"

  player "Why didn't you tell anyone?"

  fazin "Because Craw disappeared during the effects {i}I{/i} programmed"

  fazin "Do you think I wanted to walk over and announce that?"

  player "Who asked you to make them?"

  fazin "Craw"

  pause 1.0

  player "...Craw?"

  fazin "Yeah"

  player "He specifically asked for a blackout?"

  fazin "Yeah"

  player "And the sound?"

  fazin "Yeah"

  player "And the smoke?"

  fazin "Yeah"

  player "Exactly at those times?"

  fazin "Pretty much"

  player "Why?"

  fazin "He said it was for the final demo"

  player "You didn't ask what the demo was?"

  fazin "I did"

  player "And?"

  fazin "He didn't tell me"

  player "...Of course he didn't"

  narrator "You look back towards the empty stage"

  narrator "The conditions surrounding Craw's apparent murder.."

  narrator "...were requested by Craw himself"

  pause 1.0

  player "That doesn't make any sense"

  fazin "Yeah"

  fazin "That's what I've been saying"

  hide fazin
  with dissolve

  jump fazin_revelation


label fazin_revelation:
  scene launch_hall
  with dissolve

  narrator "The evidence has changed"

  narrator "The blackout wasn't used to interrupt Craw's presentation"

  narrator "The blackout was part of his presentation"

  player "So what was he actually demonstrating?"

  narrator "There is one obvious place to look"

  narrator "Craw's laptop"

  narrator "{i}New objective: Search Craw's laptop more thoroughly{/i}"

  jump deeper_laptop_search


label deeper_laptop_search:
  scene stage
  with dissolve

  narrator "You return to Craw's laptop"

  narrator "This time, you aren't looking for the presentation"

  narrator "You're looking for everything around it"

  narrator "The terminal is still open"

  narrator "A few directories sit beside the presentation files"

  player "Come on.."

  narrator "You start searching"

  pause 1.0

  narrator "Most of it is exactly what you'd expect"

  narrator "Build scripts"

  narrator "Crawssembly binaries"

  narrator "Documentation"

  narrator "Several files with names that explain absolutely nothing"

  player "Naturally"

  narrator "Then one directory catches your attention"

  narrator "\"launch_final\""

  player "That's subtle"

  narrator "Inside are several files"

  narrator "\"effects.json\""

  narrator "\"death.craw\""

  narrator "\"network.cfg\""

  narrator "\"controller.map\""

  pause 1.0

  player "...death.craw?!?"

  narrator "You open it"

  narrator "The code is Crawssembly"

  narrator "Which is unfortunate"

  player "I have no idea what any of this means"

  narrator "But one thing is immediately obvious"

  narrator "Several lines are marked with comments"

  narrator "\"RUPNIL ROUTINE\""

  pause 1.0

  player "Oh"

  narrator "You open controller.map"

  narrator "Two outputs are listed"

  narrator "\"relay_0\""

  narrator "\"relay_1\""

  player "Jam"

  narrator "Then network.cfg"

  narrator "A familiar host appears"

  narrator "The same machine Keyboard was testing earlier"

  pause 1.0

  player "Right"

  narrator "Three people"

  narrator "Three pieces of the same system"

  narrator "And none of them mentioned this"

  narrator "{i}New leads: Rupnil, Jam, Keyboard.{/i}"

  jump technical_leads_hub


default questioned_rupnil = False
default questioned_jam = False
default questioned_keyboard = False


label technical_leads_hub:
  scene launch_hall
  with dissolve

  if questioned_rupnil and questioned_jam and questioned_keyboard:
    jump technical_leads_complete

  menu:
    "Question Rupnil" if not questioned_rupnil:
      jump question_rupnil

    "Question Jam" if not questioned_jam:
      jump question_jam

    "Question Keyboard" if not questioned_keyboard:
      jump question_keyboard


label question_rupnil:
  $ questioned_rupnil = True

  scene launch_hall

  show rupnil at pfp
  with dissolve

  player "Rupnil"

  rupnil "What"

  player "I found something on Craw's laptop"

  rupnil "Ok"

  player "\"death.craw\""

  pause 1.0

  rupnil "Oh"

  player "That's all you've got?"

  rupnil "What do you want me to say"

  player "Your name is in it"

  rupnil "Yeah"

  player "You wrote part of a file called death.craw"

  rupnil "Yeah"

  pause 2.0

  player "Rupnil"

  rupnil "Craw asked me to"

  player "Of course he did"

  rupnil "He gave me a routine to write"

  player "What routine?"

  rupnil "Timing and control stuff"

  player "Control of what?"

  rupnil "No idea"

  player "You said that earlier"

  rupnil "Because it's still true"

  player "You wrote the code"

  rupnil "I know what the code does"

  rupnil "I don't know what the hardware does"

  player "Explain"

  rupnil "It waits for events"

  rupnil "Then it sends values to two outputs"

  player "What outputs?"

  rupnil "Whatever Craw connected them to"

  player "And you didn't ask?"

  rupnil "I did"

  player "And?"

  rupnil "He said it was for the presentation"

  player "Did you know about the blackout?"

  rupnil "No"

  player "The smoke?"

  rupnil "No"

  player "The crash?"

  rupnil "No"

  player "Did you know Craw was under investigation?"

  pause 1.0

  rupnil "..."

  player "Rupnil?"

  rupnil "Yeah"

  player "Fraud Squad?"

  rupnil "Yeah"

  player "How long?"

  rupnil "A while"

  player "And you didn't think that was relevant?"

  rupnil "To him disappearing?"

  rupnil "Now, yes"

  pause 0.5

  player "You realise how this looks"

  rupnil "Yeah"

  rupnil "Not great"

  player "That's one way of putting it"

  hide rupnil
  with dissolve

  jump technical_leads_hub


label question_jam:
  $ questioned_jam = True

  scene launch_hall

  show jam at pfp
  with dissolve

  player "Jam"

  jam "Yeah?"

  player "I found controller.map"

  jam "Ok"

  player "Two relay outputs"

  jam "Yeah"

  player "The board you gave Craw"

  jam "Yeah"

  pause 1.0

  player "Do you want to elaborate?"

  jam "Not really"

  player "Please do"

  jam "He asked for a controller"

  jam "I gave him one"

  player "What was it controlling?"

  jam "Don't know"

  player "You didn't wire it?"

  jam "No"

  player "Did you test it?"

  jam "Yeah"

  player "How?"

  jam "Both outputs switched"

  player "And that was enough?"

  jam "He said it was"

  player "Did Craw tell you what the relays were connected to?"

  jam "No"

  player "Did he tell you why he needed two?"

  jam "No"

  pause 1.0

  player "This is remarkably unhelpful"

  jam "Sorry"

  player "When did you give it to him?"

  jam "During setup"

  player "Before 18:00?"

  jam "Probably"

  player "Did he take it anywhere?"

  jam "Downstairs"

  pause 1.0

  player "Downstairs where?"

  jam "No idea"

  player "Basement?"

  jam "Probably"

  player "Right"

  jam "Is there a url that needs shortening?"

  player "Jam"

  jam "Sorry"

  hide jam
  with dissolve

  jump technical_leads_hub


label question_keyboard:
  $ questioned_keyboard = True

  scene launch_hall

  show keyboard at pfp
  with dissolve

  player "Keyboard"

  keyboard "Yeah?"

  player "The machine you were testing earlier"

  keyboard "What about it?"

  player "It's in Craw's network configuration"

  keyboard "Yeah"

  player "You knew that?"

  keyboard "I configured it"

  pause 1.0

  player "Wonderful"

  keyboard "What"

  player "Where is it?"

  keyboard "Downstairs"

  player "Basement?"

  keyboard "Yeah"

  player "What exactly did Craw ask you to do?"

  keyboard "Make sure it stayed reachable"

  player "From where?"

  keyboard "His laptop"

  player "Why?"

  keyboard "For the demo"

  player "Everyone keeps saying that"

  keyboard "Because that's what he said"

  player "Did the machine stay connected during the presentation?"

  keyboard "Probably"

  player "Can you check?"

  keyboard "Yeah"

  narrator "Keyboard takes the laptop"

  narrator "A few seconds pass"

  pause 3.0

  keyboard "Oh"

  player "What?"

  keyboard "It got traffic"

  player "When?"

  keyboard "20:08"

  pause 1.0

  player "That was after Craw disappeared"

  keyboard "Yeah"

  player "From where?"

  keyboard "Same local endpoint"

  player "The basement?"

  keyboard "Looks like it"

  pause 1.0

  narrator "Someone used Craw's system from the basement at 20:08"

  pause 1.0

  narrator "One minute after the apparent murder"

  pause 1.0

  player "Show me"

  keyboard "huh"

  player "You and Jam will show me the basement, just to be safe"

  hide keyboard
  with dissolve

  show keyboard at pfp_left
  with dissolve

  show jam at pfp_right
  with dissolve

  jam "I've nothing better to do ig"

  keyboard "Fine..."

  hide keyboard
  with dissolve

  hide jam
  with dissolve

  scene corridor
  with fade

  show keyboard at pfp_left
  with dissolve

  show jam at pfp_right
  with dissolve

  narrator "You, Jam, and Keyboard make your way downstairs, where you are met with a dark corrdior"

  keyboard "This is where I tested the network from"

  player "What about these doors at the ends?"

  keyboard "Locked, I can't seem to get past"

  jam "This hardware looks like an electronic-logging lock, someone would need access to get them open. "

  narrator "Nothing looks out of the ordinary"

  pause 1.0

  narrator "Until..."

  player "Wait just a moment..."

  pause 1.0

  narrator "You spot a tiny red drop on the floor by one of the locked doors"

  player "I think someone else has been down here since the murder"

  $ add_evidence("Basement System")

  jam "You don't mean..."

  player "I can't say for sure at this point..."

  player "I should get back to the others, a riot could start at any moment"

  hide keyboard
  with dissolve

  hide jam
  with dissolve

  scene launch_hall
  with dissolve

  jump technical_leads_hub


label technical_leads_complete:
  scene launch_hall
  with dissolve

  narrator "The picture is getting worse"

  narrator "Rupnil wrote part of the control software"

  narrator "Jam supplied the hardware"

  narrator "Keyboard configured the network"

  narrator "Fazin programmed the blackout"

  narrator "All of them were acting on Craw's instructions"

  player "So Craw built the whole thing.."

  player "...but split it between different people"

  narrator "Nobody appears to have known what anyone else was doing"

  narrator "Except Craw"

  pause 1.0

  player "Why?"

  pause 1.0

  narrator "A notification sound cuts through the room"

  player "..."

  nayte "Uh"

  narrator "Several phones light up at once"

  player "What now?"

  narrator "A new message has appeared in Stardance"

  pause 1.0

  narrator "\"@The_Craw  20:12\""

  narrator "\"Crawssembly 2.0 is now live btw\""

  pause 1.0

  player "..."

  keyboard "what"

  rupnil "BRO"

  fazin "Huh?"

  jam "..."

  player "Craw just posted"

  narrator "At 20:12"

  narrator "Five minutes after his apparent death"

  pause 1.0

  nayte "Whoops.."

  jump posthumous_message


label posthumous_message:
  scene launch_hall

  show nayte at pfp
  with dissolve

  player "What did you say Nayte?"

  pause 1.0

  nayte "Uhh..."

  pause 1.0

  player "Do you know anything about this message?"

  pause 1.0

  nayte "Yeah.."

  player "Why did Craw just post?"

  nayte "Scheduled message"

  pause 1.0

  player "What?"

  nayte "I scheduled it"

  pause 1.0

  player "YOU scheduled it?"

  nayte "Yeah"

  player "Why did you not mention this?"

  nayte "Nobody asked"

  player "Craw is missing"

  nayte "Yeah"

  player "And his account just posted"

  nayte "Yeah"

  player "And you knew why"

  nayte "Yeah"

  pause 1.0

  player "..."

  nayte "What"

  player "When did he ask you to schedule it?"

  nayte "Earlier"

  player "{i}Well obviously...{/i} What exactly did he ask for?"

  nayte "Launch message at 20:12"

  player "Anything else?"

  nayte "Couple things"

  player "How many?"

  nayte "Few"

  player "Until when?"

  nayte "20:30"

  pause 1.0

  player "Why 20:30?"

  nayte "He said don't schedule anything after that"

  player "Why?"

  nayte "Said he'd handle it himself"

  pause 1.0

  player "He expected to be available after 20:30"

  nayte "I guess"

  narrator "That detail lodges itself somewhere in the back of your mind"

  $ add_evidence("Scheduled Messages")

  narrator "For now, there is a more immediate problem"

  player "If Craw planned these messages.."

  player "...then he knew he wouldn't be here to send them"

  hide nayte
  with dissolve

  jump act_one_midpoint


label act_one_midpoint:
  scene stage
  with dissolve

  narrator "You return to the stage"

  narrator "The same facts now mean something completely different"

  narrator "The blackout was planned"

  narrator "The smoke was planned"

  narrator "The network system was planned"

  narrator "Even Craw's activity after the presentation was planned"

  player "He knew something was going to happen"

  narrator "But knowing something would happen..."

  narrator "...doesn't explain why he disappeared"

  pause 1.0

  player "Unless somebody used his own plan against him"

  narrator "And one person knew more about that plan than anyone else"

  pause 1.0

  player "Rupnil"

  narrator "{i}New objective: Reconstruct the murder.{/i}"

  jump reconstruct_murder


label reconstruct_murder:
  scene launch_hall
  with dissolve

  narrator "If Rupnil knew more than everyone else, there should be evidence of it"

  player "Motive"

  player "Means"

  player "Opportunity"

  player "Start with motive"

  narrator "Craw's laptop is still logged into Stardance"

  narrator "You search his recent messages"

  narrator "Most are useless"

  narrator "\"vestige ship\""

  narrator "\"when ship\""

  narrator "\"2 hour devlog when\""

  narrator "\"Crawssembly is NOT an esolang\""

  player "This may take a while"

  narrator "Then you find a conversation with Rupnil"

  pause 1.0

  narrator "\"Rupnil: delete .ssh\""

  narrator "\"Craw: absolutely not\""

  narrator "\"Rupnil: im warning you\""

  narrator "\"Craw: you will never take .ssh from me\""

  narrator "\"Rupnil: we'll see\""

  pause 1.0

  player "..."

  player "That sounds considerably worse without context"

  $ add_evidence("Rupnil Messages")

  narrator "{i}New evidence: Rupnil Messages{/i}"

  jump investigate_rupnil_motive


label investigate_rupnil_motive:
  scene launch_hall

  show water at pfp
  with dissolve

  player "Did Craw and Rupnil ever argue?"

  water "Constantly"

  player "Seriously?"

  water "No"

  player "..."

  water "But constantly"

  player "What about .ssh?"

  water "Oh yeah"

  water "That was serious"

  player "How serious?"

  water "Rupnil wanted it gone"

  player "And Craw refused"

  water "Yeah"

  player "So there was a dispute"

  water "If you want to call it that"

  player "I do"

  water "Then yes"

  player "What about arguments with anyone else?"

  water "Apart from the common nano debates, not really"

  player "Interesting..."

  player "Ok, thank you Water"

  pause 0.5

  hide water
  with dissolve

  player "So rupnil had motive, his arguments with Craw's .ssh folder could manifest..."

  player "This isn't enough to prove any guilt though... I need to find means and opportunity"

label investigate_rupnil_means:
  scene launch_hall

  show rupnil at pfp
  with dissolve

  player "I need you to show me exactly what your code does"

  rupnil "I already told you"

  player "Show me"

  rupnil "Why"

  player "Humour me"

  rupnil "Fine"

  narrator "Rupnil opens death.craw"

  rupnil "This waits"

  rupnil "This checks the trigger"

  rupnil "This sends the first output"

  rupnil "Then after the delay it sends the second"

  player "Could you change those outputs?"

  rupnil "Obviously"

  player "Could you trigger them manually?"

  rupnil "Yeah"

  pause 1.0

  player "Remotely?"

  rupnil "If the endpoint is reachable"

  pause 1.0

  player "Keyboard made it reachable"

  rupnil "Apparently"

  player "From the basement"

  rupnil "Yeah"

  player "And you knew the protocol"

  rupnil "I wrote the routine"

  pause 1.0

  player "So you had the means"

  rupnil "Means to do what"

  player "Control Craw's system"

  rupnil "So did Craw..."

  pause 1.0

  player "Craw is missing"

  pause 1.0

  rupnil "I noticed"

  hide rupnil
  with dissolve

  player "So Rupnil could have accessed the system from the basement to trigger his code"

  player "He could have written the very program that killed Craw..."

  jump investigate_alibis


label investigate_alibis:
  scene launch_hall

  narrator "The project showcase gives you something you hadn't considered"

  narrator "A timetable"

  narrator "And therefore, alibis"

  show bird at pfp
  with dissolve

  bird "Fazin was with me when Craw started presenting"

  player "The whole time?"

  bird "Until the lights went out"

  hide bird

  show gizzy at pfp
  with dissolve

  gizzy "Jam was near the equipment table"

  player "At 20:07?"

  gizzy "Yeah"

  hide gizzy

  show mixid at pfp
  with dissolve

  mixid "Keyboard was beside me"

  player "You're sure?"

  mixid "Pretty sure"

  hide mixid

  show gl2011 at pfp
  with dissolve

  player "What about Rupnil?"

  gl2011 "..."

  player "What?"

  gl2011 "I don't know"

  player "You don't remember seeing him?"

  gl2011 "Not during the end"

  pause 1.0

  hide gl2011
  with dissolve

  narrator "Four contributors"

  narrator "Three witnesses"

  narrator "One gap"

  player "Rupnil"

  $ add_evidence("Missing Alibi")

  jump inspect_execution_log


label inspect_execution_log:
  scene stage
  with dissolve

  player "No alibi, means, motive, and opportunity to slip downstairs..."

  player "But does it match the laptop logs?"

  narrator "You compare death.craw against the execution log"

  narrator "One entry stands out"

  narrator "\"20:06:58 — MODULE rupnil_control loaded\""

  narrator "\"20:07:03 — EXEC\""

  pause 1.0

  player "20:07:03"

  narrator "The exact second the lights went out"

  player "Rupnil's module"

  narrator "Loaded five seconds before Craw's apparent murder"

  $ add_evidence("Execution Log")

  jump murder_reconstruction


label murder_reconstruction:
  scene black
  with fade

  centered "{size=+10}RECONSTRUCT THE MURDER{/size}"

  scene stage
  with dissolve

  narrator "You have enough information to construct a theory"

  narrator "If Craw was murdered, the killer needed four things"

  narrator "Motive"

  narrator "Means"

  narrator "Opportunity"

  narrator "And knowledge of Craw's plan"

  jump murder_reconstruction_contol


label murder_reconstruction_contol:

  menu:
    "Who had knowledge of the control system?"

    "Rupnil":
      player "Rupnil wrote the control routine"
      jump murder_reconstruction_means

    "Fazin":
      player "Fazin only knew about the effects"
      narrator "That doesn't explain the controller"
      jump murder_reconstruction_contol

    "Jam":
      player "Jam supplied the hardware, but didn't know what it controlled"
      jump murder_reconstruction_contol

    "Keyboard":
      player "Keyboard configured the network, but didn't know the routine"
      jump murder_reconstruction_contol


label murder_reconstruction_means:

  menu:
    "Who had means?"

    "Rupnil":
      player "Rupnil knew how death.craw worked"
      jump murder_reconstruction_motive

    "Fazin":
      player "Fazin had no access to the system"
      jump murder_reconstruction_means

    "Jam":
      player "Jam doesn't know what his hardware controlled"
      jump murder_reconstruction_means

    "Keyboard":
      player "Keyboard had access, but didn't write the death.craw script"
      jump murder_reconstruction_means


label murder_reconstruction_motive:

  menu:
    "Who had motive?"

    "Rupnil":
      player "Rupnil had been known to argue with Craw"
      jump murder_reconstruction_final

    "Fazin":
      player "Fazin seemed happy to help Craw with lighting"
      jump murder_reconstruction_motive

    "Jam":
      player "Jam seemed happy to help Craw with hardware"
      jump murder_reconstruction_motive

    "Keyboard":
      player "Keyboard seemed happy to help Craw with networking"
      jump murder_reconstruction_motive


label murder_reconstruction_final:

  narrator "It's becoming clear now what happened..."

  pause 1.0

  scene stage_flashback
  with fade

  narrator "20:07:03"

  narrator "Craw begins the final demonstration"

  show craw at pfp_left
  show rupnil at pfp_right
  with dissolve

  narrator "The system is already armed"

  narrator "Craw expects a theatrical blackout"

  narrator "What he doesn't expect..."

  narrator "...is somebody else taking control"

  scene black

  narrator "Rupnil triggers the sequence"

  narrator "The lights go out"

  narrator "The impact sound hides whatever happens next"

  narrator "In the darkness, Craw is attacked"

  narrator "The smoke forces everyone away"

  hide craw
  with dissolve

  hide rupnil
  with dissolve

  narrator "Then the killer uses the basement system"

  narrator "The controller opens a route away from the stage"

  narrator "Craw's body is moved before anyone returns"

  scene launch_hall

  narrator "The scheduled messages make it look as though Craw planned to disappear"

  narrator "And by the time anyone understands what happened..."

  narrator "...the killer is gone"

  pause 1.0

  jump accuse_rupnil


label accuse_rupnil:
  scene launch_hall
  with fade

  narrator "You gather everyone together"

  show rupnil at pfp
  with dissolve

  rupnil "Why is everyone looking at me"

  player "Because I know what happened"

  rupnil "Oh no"

  player "Craw planned the blackout"

  player "He planned the smoke"

  player "He planned the network"

  player "He even planned messages to be sent after the presentation"

  rupnil "Yeah"

  player "But he didn't plan to die"

  pause 1.0

  rupnil "Probably not"

  player "Someone used his own system against him"

  player "Someone who understood death.craw"

  player "Someone who knew about the Fraud Squad investigation"

  player "Someone whose whereabouts at 20:07 cannot be confirmed"

  pause 1.0

  player "You"

  pause 2.0

  rupnil "what"

  pause 1.0

  rupnil "BRO WHAAA"

  player "Your module executed seconds before the blackout"

  rupnil "Because Craw ran it"

  player "You could access the system remotely"

  rupnil "So could Craw"

  player "You knew what the code did"

  rupnil "Yeah because I wrote it"

  player "And nobody saw you during the murder"

  rupnil "I was getting a drink"

  player "Convenient"

  rupnil "..."

  rupnil "ok"

  pause 1.0

  rupnil "where's craw then"

  player "What?"

  rupnil "where's his body"

  pause 2.0

  rupnil "You said I killed him on stage"

  player "Yes"

  rupnil "then moved him"

  player "During the evacuation"

  rupnil "how"

  player "Through the basement"

  rupnil "you checked that?"

  pause 1.0

  player "..."

  rupnil "did anyone see me carrying craw"

  player "No"

  rupnil "did any camera see me"

  player "..."

  rupnil "do you even know if someone can get from the stage to outside that way"

  pause 1.0

  rupnil "you've explained everything"

  rupnil "except the murder"

  pause 2.0

  player "..."

  rupnil "and the body"

  pause 1.0

  rupnil "mostly the body"

  jump missing_body_investigation


label missing_body_investigation:
  scene black
  with fade

  centered "{size=+10}WHERE IS CRAW?{/size}"

  pause 1.0

  scene launch_hall

  narrator "You had been so focused on identifying a killer..."

  narrator "...that you'd treated Craw's disappearance as something the killer must have accomplished"

  narrator "But that isn't evidence"

  narrator "It's an assumption"

  player "Start again"

  player "How could a body leave this room?"

  jump exit_investigation


label exit_investigation:
  scene launch_hall
  with dissolve

  narrator "There are only a handful of ways out of the building"

  player "If Rupnil moved Craw's body..."

  player "...he had to use one of them"

  jump check_exit_hub


define checked_front = False
define checked_side = False
define checked_service = False


label check_exit_hub:

  if checked_front and checked_side and checked_service:
    jump reconsider_body

  menu:
    "Check main exit" if not checked_front:
      jump check_front_exit

    "Check side exit" if not checked_side:
      jump check_side_exit

    "Check service exit" if not checked_service:
      jump check_service_exit


label check_front_exit:

  $ checked_front = True

  scene launch_hall

  show trkl at pfp
  with dissolve

  player "You were outside during the evacuation, right?"

  trkl "Yeah"

  player "Did you see Rupnil leave?"

  trkl "Eventually"

  player "Eventually?"

  trkl "With everyone else"

  player "Was he carrying anything?"

  trkl "No"

  player "Did you see anyone carrying Craw?"

  trkl "No"

  player "Could someone have got past you?"

  trkl "Probably"

  player "Carrying a person?"

  pause 1.0

  trkl "Probably not"

  hide trkl
  with dissolve

  narrator "The front exit doesn't work"

  jump check_exit_hub


label check_side_exit:

  $ checked_side = True

  scene launch_hall

  show louis at pfp
  with dissolve

  player "What about the side entrance?"

  louis "Locked"

  player "The whole time?"

  louis "After the alarm, yeah"

  player "Could it be opened from inside?"

  louis "Probably"

  player "Did anyone?"

  louis "The alarm log would show it"

  player "There's an alarm log?"

  louis "It's an emergency exit"

  player "Right"

  narrator "You check"

  narrator "The door wasn't opened between 20:00 and 20:20"

  hide louis
  with dissolve

  narrator "Two exits eliminated"

  jump check_exit_hub


label check_service_exit:

  $ checked_service = True

  scene corridor
  with dissolve

  narrator "That leaves the service exit"

  narrator "Unlike the others, it isn't watched continuously"

  player "Finally"

  narrator "You remember Jam saying the locks electronally log access"

  player "JAM! GET DOWN HERE!"

  show jam at pfp
  with dissolve

  narrator "Jam comes running down"

  jam "WHAT HAPPENED??"

  player "No rush... I just wanted to ask you where these locks keep their logs"

  pause 1.0

  jam "You made me run for that?"

  pause 1.0

  player "..."

  pause 1.0

  jam "Fine. It looks like they connect to this access panel here"

  narrator "Jam points to a yellowed box attached to the wall"

  player "Can you access the logs?"

  jam "Sure, just give me a moment"

  pause 4.0

  jam "{i}I'm in{/i}"

  jam "Looks like the door opened at 19:43, and again at 20:26"

  pause 1.0

  player "..."

  player "Nobody carried Craw through the service exit"

  player "Then how did Rupnil get the body out?"

  pause 1.0

  narrator "For the first time, you don't have an answer"

  jump check_exit_hub


label reconsider_body:
  scene launch_hall
  with dissolve

  player "Maybe the body never left"

  narrator "That would solve the exits"

  narrator "It would also mean Craw is still somewhere inside"

  show tej at pfp
  with dissolve

  tej "We've checked the main rooms"

  player "All of them?"

  tej "Main hall, toilets, kitchen, upstairs rooms"

  player "Storage?"

  tej "Checked"

  player "Backstage?"

  tej "Checked"

  player "And?"

  tej "Nothing"

  hide tej
  with dissolve

  player "So he didn't leave"

  player "And he isn't here"

  pause 1.0

  player "That's impossible"

  narrator "Unless one of those statements is wrong"

  jump blood_result


label blood_result:
  scene launch_hall

  show gl2011 at pfp
  with dissolve

  gl2011 "About that blood"

  player "What about it?"

  gl2011 "It's not blood"

  pause 2.0

  player "What?"

  gl2011 "It's theatrical"

  player "Theatrical blood?"

  gl2011 "Yeah"

  pause 1.0

  player "You're sure?"

  gl2011 "Unless Craw's circulatory system contains corn syrup"

  pause 1.0

  player "..."

  hide gl2011
  with dissolve

  pause 2.0

  player "What the f*ck is going on"

  pause 2.0

  $ current_act = 1

  narrator "The evidence has changed"

  $ details = get_evidence("Blood Sample")

  narrator "Blood Sample: [details]"

  pause 1.0

  player "There was no blood"

  narrator "No weapon"

  player "No body"

  narrator "No evidence that Craw was ever injured"

  pause 1.0

  player "Oh."

  jump rethink_murder


label rethink_murder:
  scene stage
  with dissolve

  narrator "You return to where Craw fell"

  narrator "Nothing about the scene has physically changed"

  narrator "Only your interpretation of it"

  player "Suppose nobody attacked Craw"

  narrator "The blackout"

  player "Craw requested it"

  narrator "The impact"

  player "Craw requested it"

  narrator "The smoke"

  player "Craw requested it"

  narrator "The blood"

  player "Fake"

  narrator "The missing weapon"

  player "There wasn't one"

  pause 1.0

  player "Then Craw didn't disappear after the murder"

  player "The disappearance was the trick"

  pause 1.0

  narrator "You look at the stage again"

  narrator "This time, you aren't looking for a weapon"

  narrator "You're looking for a way out"

  jump search_stage_escape


label search_stage_escape:
  scene stage

  narrator "Behind the presentation equipment, several cables disappear beneath the stage"

  narrator "You move one aside"

  player "Wait"

  narrator "One section of panelling doesn't quite line up with the rest"

  narrator "You pull at it"

  pause 1.0

  narrator "It moves"

  narrator "Behind it is a narrow service passage"

  pause 2.0

  player "..."

  player "You've got to be kidding me"

  scene corridor
  with dissolve

  narrator "The passage runs beneath the stage"

  narrator "And towards the basement"

  pause 1.0

  player "The basement"

  narrator "The same basement where Keyboard recorded traffic at 20:08"

  narrator "The same basement where you found the red drop"

  pause 1.0

  player "That wasn't evidence of somebody moving Craw"

  player "That was evidence of Craw moving himself"

  jump final_act_one_deduction


label final_act_one_deduction:
  scene black
  with fade

  narrator "Five people helped construct the system"

  narrator "Five people appeared to be involved in Craw's death"

  narrator "But none of them knew the whole plan"

  narrator "There was only one person connecting every piece"

  pause 1.0

  centered "{size=+10}WHO ORGANISED THE MURDER OF CRAW?{/size}"

  jump choose_organiser


label choose_organiser:
  menu:
    "Rupnil":
      player "Rupnil knew the software..."
      player "...but not the hardware, effects or schedule"
      jump choose_organiser

    "Fazin":
      player "Fazin knew the effects..."
      player "...but nothing else"
      jump choose_organiser

    "Jam":
      player "Jam supplied the hardware..."
      player "...without knowing what it controlled"
      jump choose_organiser

    "Keyboard":
      player "Keyboard configured the network..."
      player "...without knowing why"
      jump choose_organiser

    "Nayte":
      player "Nayte scheduled the messages..."
      player "...because somebody told him to"
      jump choose_organiser

    "Craw":
      jump craw_deduction


label craw_deduction:
  scene stage
  with dissolve

  player "Craw"

  pause 2.0

  narrator "Fazin didn't choose the blackout"

  narrator "Craw did"

  narrator "Jam didn't design the system"

  narrator "Craw commissioned it"

  narrator "Keyboard didn't decide to connect the basement"

  narrator "Craw asked him to"

  narrator "Rupnil didn't decide what death.craw was for"

  narrator "Craw gave him the specification"

  narrator "Nayte didn't decide when Craw should appear online"

  narrator "Craw gave him the schedule"

  pause 1.0

  player "Nobody murdered Craw"

  pause 1.0

  player "Craw murdered Craw"

  pause 2.0

  rupnil "what"

  nayte "oh"

  fazin "Huh?"

  jam "..."

  keyboard "what the"

  player "Not literally"

  pause 1.0

  player "He faked his own death"

  scene black
  with fade

  centered "{size=+12}CASE CLOSED{/size}"

  pause 2.0

  centered "{size=-5}probably{/size}"

  pause 2.0

  jump trapped_craw


label trapped_craw:
  scene black

  pause 2.0

  narrator "Somewhere beneath the building"

  pause 2.0

  unknown "..."

  pause 1.0

  unknown "Hello?"

  pause 2.0

  unknown "Can anyone hear me?"

  pause 2.0

  unknown "..."

  pause 1.0

  unknown "Bugger"

  pause 2.0

  centered "{size=+12}END OF ACT I{/size}"

  centered "{size=+8}Thanks for testing Act I!{/size}"
  pause 1.0
  centered "Please send me any bugs, confusing clues, or moments where you guessed the twist early."
  return




