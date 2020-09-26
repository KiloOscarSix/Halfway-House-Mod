init python:
    mod = Character("OscarSix", color="#0f0")

    gr = "{color=#0f0}"
    red = "{color=#f00}"
    blue = "{color=#00f}"

    MonroePath = "{color=#0f0}(Monroe Path)"
    EmilyPath = "{color=#0f0}(Emily Path)"
    EmilyLovePath = "{color=#0f0}(Emily Love Path)"
    EmilyCorruptionPath = "{color=#0f0}(Emily Corruption Path)"
    AshleyPath = "{color=#0f0}(Ashley Path)"
    SamanthaPath = "{color=#0f0}(Samantha Path)"
    LuisPath = "{color=#0f0}(Luis Path)"
    KuniedaPath = "{color=#0f0}(Kunieda Path)"


screen modOptions():
    tag menu
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 50
        spacing 100

        text "Walkthrough Options" style "modTextHeader"

        text "Turn on and off character paths" style "modTextBody" xcenter 0.5

    frame:
        xcenter 0.5
        ycenter 0.5
        padding (20, 20)
        grid 3 2:
            spacing 50
            style_prefix "check"

            textbutton "Monroe Path":
                action ToggleVariable("MonroePath", true_value="{color=#0f0}(Monroe Path)", false_value="")

            textbutton "Emily Path's":
                action [ToggleVariable("EmilyPath", true_value="{color=#0f0}(Emily Path)", false_value=""), ToggleVariable("EmilyLovePath", true_value="{color=#0f0}(Emily Love Path)", false_value=""), ToggleVariable("EmilyCorruptionPath", true_value="{color=#0f0}(Emily Corruption Path)", false_value="")]

            textbutton "Ashley Path":
                action ToggleVariable("AshleyPath", true_value="{color=#0f0}(Ashley Path)", false_value="")

            textbutton "Samantha Path":
                action ToggleVariable("SamanthaPath", true_value="{color=#0f0}(Samantha Path)", false_value="")

            textbutton "Luis Path":
                action ToggleVariable("LuisPath", true_value="{color=#0f0}(Luis Path)", false_value="")

            textbutton "Kunieda Path":
                action ToggleVariable("KuniedaPath", true_value="{color=#0f0}(Kunieda Path)", false_value="")

    textbutton _("Return") action ShowMenu("save"), Hide("modWalkthroughOptions"):
        yanchor 1.0
        pos (100, 1030)
        text_style "modTextButtonHeader"
