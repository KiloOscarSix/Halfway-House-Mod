init python:
    class CheatItem:
        """
        Base cheat data class for storing the attributes of cheat options

        Attributes:
            catagory (str): Generic catagory name for organising cheat items
            name (str): Display name for cheat option
            action (str, optinal): Action to take when cheat button is clicked
        """

        cheats = {}

        def __init__(self, catagory, name, action=None):
            self.catagory = catagory
            self.name = name
            self.action = action

            CheatItem.cheats.setdefault(self.catagory, []).append(self)


    class CheatSliderItem(CheatItem):
        """
        Slider type cheat item

        Attributes:
            catagory (str): Generic catagory name for organising cheat items
            name (str): Display name for cheat option
            variable (str, optional): Attached variable for cheat option. Defaults to ""
            min_value (int, optional): The minimum value the slider type can obtain. Defaults to 0
            max_value (int, optional): The maximum value the slider type can obtain. Defaults to 0
        """

        def __init__(self, catagory, name, variable, min_value=0, max_value=0):
            CheatItem.__init__(self, catagory, name)

            self.variable = variable
            self.min_value = min_value
            self.max_value = max_value


    CheatSliderItem("Emily", "Love Points", "emLP", max_value=50)
    CheatSliderItem("Emily", "Corruption Points", "emCP", max_value=50)

    CheatSliderItem("Ashley", "Corruption Points", "asCP", max_value=50)

    CheatSliderItem("Samantha", "Corruption Points", "sgCP", max_value=50)

    CheatSliderItem("Luis", "Friendship Points", "luFP", max_value=20)

    CheatSliderItem("Monroe", "Friendship Points", "omFP", max_value=10)
    CheatSliderItem("Monroe", "Infraction Points", "omIP", max_value=3)

    CheatSliderItem("Other", "Hollis Anger", "ep3_HOanger", max_value=5)


screen mod_cheat_menu():
    tag mod_cheats
    zorder 100
    modal True
    style_prefix "mod_cheat_menu"

    default cheats = []

    add "mod_additions/images/cheat_background.png"

    fixed:
        xysize (1536, 99)
        pos (85, 13)

        hbox:
            align (0.5, 0.5)
            spacing 100

            for catagory, cheat_items in CheatItem.cheats.items():
                textbutton catagory:
                    action [Function(renpy.retain_after_load), SetScreenVariable("cheats", cheat_items)]
                    selected False

    fixed:
        style_prefix "mod_cheat_values"

        vpgrid:
            cols 4

            xalign 0.5
            ypos 150
            xspacing 100
            yspacing 60

            style_prefix "check"

            for cheat in cheats:
                if isinstance(cheat, CheatSliderItem):
                    vbox:
                        spacing 10

                        text cheat.name style "mod_cheat_values_text"
                        fixed:
                            xysize (352, 42)

                            bar value VariableValue(cheat.variable, cheat.max_value - cheat.min_value, offset=cheat.min_value)
                            text "{}".format(getattr(store, cheat.variable)) align(0.5, 0.5)

                else:
                    textbutton cheat.name:
                        action ToggleVariable(cheat.variable, true_value=cheat.true_value, false_value=cheat.false_value)
                        text_style "modTextButtonBody"

    imagebutton:
        action [Hide("mod_cheat_values"), Hide("mod_cheats")]
        idle "mod_additions/images/back_button.png"
        hover Transform("mod_additions/images/back_button.png", matrixcolor=BrightnessMatrix(0.2))
        pos (1666, 50)


