define jonah = Character("Jonah")
define camiel = Character("Camiel")

label start:
  jonah "Okay, who killed him?"

  camiel "idk"

  jonah "Camiel."

  camiel "what"

  menu:
    "Accuse Camiel":
      jump accuse_camiel

    "Investigate the .craw file":
      jump investigate_craw

label accuse_camiel:
  jonah "You did it."

  camiel "no"

  "BAD END"

  return

label investigate_craw:
  "You pick up the mysterious .craw file."

  jonah "Interesting..."

  camiel "we'll make the craw files"

  "TO BE CONTINUED"

  return