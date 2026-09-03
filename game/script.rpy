define jonah = Character("Jonah")
define natye = Character("Natye")

default has_craw_file = False

label start:
  scene black

  "The Stardance server had gone unusually quiet."

  jonah "That's never a good sign."

  natye "yeah probably not"

  menu:
    "Check the desk":
      jump check_desk

    "Question natye":
      jump question_natye

label check_desk:
  "You find a suspicious .craw file."

  $ has_craw_file = True

  jonah "Interesting."

  jump question_natye

label question_natye:
  if has_craw_file:
    jonah "I found this on the desk."

    natye "we'll make the craw files"

    jonah "That is an incredibly suspicious thing to say right now."

  else:
    jonah "Did you see anything?"

    natye "no"

  return