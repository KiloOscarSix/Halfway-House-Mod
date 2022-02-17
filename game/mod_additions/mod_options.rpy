# Define commonly used hints or colours here
define gr = "{color=#0f0}"
define red = "{color=#f00}"
define blue = "{color=#00f}"

define MonroePath = "{color=#0f0}(Monroe Path)"
define EmilyPath = "{color=#0f0}(Emily Path)"
define EmilyLovePath = "{color=#0f0}(Emily Love Path)"
define EmilyCorruptionPath = "{color=#0f0}(Emily Corruption Path)"
define AshleyPath = "{color=#0f0}(Ashley Path)"
define SamanthaPath = "{color=#0f0}(Samantha Path)"
define LuisPath = "{color=#0f0}(Luis Path)"
define KuniedaPath = "{color=#0f0}(Kunieda Path)"

define mod = Character("The Warehouse", color="#0f0")
define config.gl2 = True


# Add any toggleable options here
screen mod_options():
    modal True
    style_prefix "mod_options"

    add "#23272a"

    vbox:
        xalign 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("mod_change_ingame_names")

        textbutton "Change Gallery Names" action ui.callsinnewcontext("mod_change_gallery_names")

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

    textbutton _("Return") action Hide("modOptions"):
        yanchor 1.0
        align (0.1, 0.9)


label mod_change_gallery_names:

    return


label mod_change_ingame_names:

    return

