









init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("text")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)


init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 800
    yanchor .7

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







init -501 screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.0

            textbutton _("Hide") action HideInterface()
            textbutton _("Back") action Rollback()


            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Cheat") action Show("cheatMenu") xoffset 700






init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")











init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:
            textbutton _("Mod Options") action Show("modOptions")

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")



        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if not _in_replay and main_menu:
            textbutton "Scenes" action ShowMenu("scenes")



        textbutton _("Readme") action ShowMenu("readme")

        if main_menu:
            textbutton _("Patrons") action ShowMenu ("credits")


        if renpy.variant("pc"):





            textbutton _("Quit") action Quit(confirm=not main_menu)




init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








init -501 screen main_menu():
    tag menu



    style_prefix "main_menu"


    add "main_menu_slide"


    frame


    vbox align (.50,.50) pos (.060,.95):
        imagebutton auto "gui/button/Patreon_Logo_%s.png" action OpenURL('https://www.patreon.com/azrd')



    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version:
    font "White On Black.ttf"
    xalign 1.0
    color "#cccccc"

init -1 style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

init -1 style main_menu_vbox:
    xalign 0.9
    xoffset 25
    xmaximum 1200
    yalign 1.0
    yoffset -30

init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    properties gui.text_properties("title")

init -1 style main_menu_version:
    properties gui.text_properties("version")











init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background



    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")




init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 420
    yfill True

init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

init -1 style game_menu_viewport:
    xsize 1380

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 15

init -1 style game_menu_label:
    xpos 75
    ysize 180

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









init -501 screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size










init -501 screen save():
    tag menu


    use file_slots(_("Save"))


init -501 screen load():
    tag menu


    use file_slots(_("Load"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

                        if FileLoadable(slot):
                            imagebutton:
                                idle "gui/button/button_delete_idle.png"
                                hover "gui/button/button_delete_hover.png"

                                action FileDelete(slot)

                                xalign 1.0
                                xoffset 15
                                yoffset -60



            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _(".") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(".") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text:
    size 65
    font "Old Press.ttf"

init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text
init -1 style slot_button is gui_button
init -1 style slot_button_text:
    size 15
    xalign 0.5
    color '#ADADAD'
    yoffset 5
    font "White On Black.ttf"
init -1 style slot_time_text:
    size 15
    color '#ADADAD'
    xalign 0.5
    yoffset 5
    font "White On Black.ttf"
init -1 style slot_name_text:
    size 15
    color '#ADADAD'
    xalign 0.5
    yoffset 5
    font "White On Black.ttf"

init -1 style page_label:
    xpadding 75
    ypadding 5

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")









init -501 screen preferences():
    tag menu


    use game_menu(_("Options"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                        style "mute_all_button"


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text:
    size 30
    font "White On Black.ttf"
init -1 style radio_button is gui_button
init -1 style radio_button_text:
    size 35
    font "Old Press.ttf"
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text:
    size 30
    font "White On Black.ttf"
init -1 style check_button is gui_button
init -1 style check_button_text:
    size 35
    font "Old Press.ttf"
init -1 style check_vbox is pref_vbox
init -1 style slider_label is pref_label
init -1 style slider_label_text:
    size 30
    font "White On Black.ttf"
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text:
    size 35
    font "Old Press.ttf"
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text:
    size 35
    font "Old Press.ttf"

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 338

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 525

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 675










init -501 screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define -1 gui.history_allow_tags = set()


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 375
    right_padding 30

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0














init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "small"
    xsize 675



init -501 screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.03


            textbutton _("Hide") action HideInterface()
            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Menu") action ShowMenu()
            textbutton _("Cheat") action Show("cheatMenu")

init -1 style quick_button_text:
    variant "touch"
    size 30


init -1 style choice_vbox:
    variant "touch"
    xalign 0.5
    ypos 620
    yanchor .7
    spacing 50

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

init -1 style window:
    variant "touch"
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/phone/textbox.png", xalign=0.5, yalign=1.0)

init -1 style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 510

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 600

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 900

init -501 screen INT():
    add "gui/innertought.png"

init 499 image main_menu_slide:
    "gui/main_menu.webp" with fade1
    pause 8
    "EP5/ep5_end.webp" with fade1
    pause 8
    "EP4/ep4_end.webp" with fade1
    pause 8
    "EP1/ep1_OMpresent.webp" with fade1
    pause 8
    "EP1/ep1_SGEMASdinner10.webp" with fade1
    pause 8
    "EP3/ep3_SGhospitalroom10.webp" with fade1
    pause 8
    "EP4/ep4_EMSGcoffeeshop45.webp" with fade1
    pause 8
    "EP1/ep1_EMkitchenhelp1a.webp" with fade1
    pause 8
    "EP2/ep2_SGdrive10.webp" with fade1
    pause 8
    "EP1/ep1_LUplroom12.webp" with fade1
    pause 8
    "EP6/ep6_EMKUhospital86.webp" with fade1
    pause 8
    "EP5/ep5_EMASlivingroom69.webp" with fade1
    pause 8
    "EP2/ep2_EMASSGkitchen9.webp" with fade1
    pause 8
    "EP3/ep3_SGhospitalroom138.webp" with fade1
    pause 8
    "EP5/ep5_SGPLbathroom62a.webp" with fade1
    pause 8
    "EP6/ep6_stationtrans62.webp" with fade1
    pause 8
    "EP3/ep3_SGWallpaperthing.webp" with fade1
    pause 8
    "EP6/ep6_end.webp" with fade1
    pause 8
    "EP6/ep6_plroom102.webp" with fade1
    pause 8
    "EP6/ep6_stationtrans11.webp" with fade1
    pause 8
    repeat

init -501 screen readme():
    tag menu

    use game_menu(_("Readme"), scroll="viewport"):
        style_prefix "readme"

        hbox:
            box_wrap True
            label _("Probation Penalty:")
            text _("This game has fail states but it would be very hard to actually get a game over. You have 3 chances to mess up, if you run out you get a visit from [OM] and he will take you back to juvie and it's game over. But if you treat him well and gain friendship points you can trade some in for another chance each time. Only if you run out of both will be it over.")
            text _("                    ")
        hbox:
            box_wrap True
            label _("[EM] Relations:")
            text _("[EM] has both Affection Points and Corruption Points. You can do both good things and dirty things to her and gain both points. Love points will mostly only effect the ending you get in the future, while corruption points effect the level of dirtiness in her sex scenes and dialog. She'll still reject some actions and report you to [OM] if the points are too low though.")
            text _("                    ")
        hbox:
            box_wrap True
            label _("[SG]&[AS] Relations:")
            text _("[SG] and [AS] only have Corruption Points. The points behave the same as with [EM]'s. You get different scenes and dialog depending on how high the points are. Too low and you'll get rejected and reported.")
            text _("                    ")
        hbox:
            box_wrap True
            label _("[LU] Relations:")
            text _("[LU] Friendship Points are mostly used to see if he'll agree to any of your scheming. He will never report you no matter what you do.")
            text _("                    ")
        hbox:
            box_wrap True
            label _("Scene Replay:")
            text _("The scenes in Scene Replay only use default player name. A scene with multiple versions only have replay on the optimal path. For example only the best choices and highest love/horny points version will have a replay, if you don't get those they won't even unlock.")
            text _("                    ")
            text _("The \"refresh\" button in the scene replay menu will reload the game so you don't have to restart the game if unlocked scenes don't appear. Don't use this on Android. It will just quit the game.")
            text _("                    ")
        hbox:
            box_wrap True
            label _("Branching Path:")
            text _("Sometimes a multiple choice menu will lead to a branching path later on. There's no right or wrong choice to make. Your decision will just lead you to different events.")
            text _("                    ")
        hbox:
            box_wrap True
            label _("Alt Camera:")
            text _("Some scenes have alternate camera angle. When available a flashing icon will appear on the top right of the screen. The first instance of this is on a miss-able event at the start of EP2.")

init -1 style readme_text:
    size 25
    ypos 0
    font "Calibri.ttf"
init -1 style readme_label_text:
    size 40
    yoffset 5
    font "Old Press.ttf"

init -501 screen credits():
    tag menu

    use game_menu(_("Patrons"), scroll="viewport"):
        style_prefix "credits"

        hbox pos (1,300):
            box_wrap True
            label _("")
            text _("                       ")
            text _("                A Bellator - ajonid - Alexander Pluntke - Berrie Waterink  - Bob Bailey - Cireful - DodgyNomad - Dominick March - dtgr")
            text _("                      Eden - Falidam - I am Jack's username - Fluffy - gabbledub - Guto Williams - I am Jack's username - Imtiaz Razak")
            text _("                         Justin Benjamin - KP472 - lewis j lorenz - Mark L - Markell Johnson - MIXTURE - Nicholas - Nicholas Gowen")
            text _("                                Niclas Plenter - NomadPG - Phillip Frabott - RestoWyntar - Robert Wolf - Ryan Schwegel - TYR")
            text _("                                                                 Valkyrie65 - Walle - William Dewall - Zyler Gamer")
            text _("                                                                                                                                  ")
            text _("                                                                 Special thanks to Bison and Peem for proofreading.")
            text _("                                                              Also a big thank you to all my patrons no matter the tier.")


init -1 style credits_text:
    size 25
    ypos 0
    font "Calibri.ttf"
init -1 style credits_label_text:
    size 40
    yoffset 5
    font "Old Press.ttf"

init -501 screen credits():
    tag menu
    variant "touch"

    use game_menu(_("Patrons"), scroll="viewport"):
        style_prefix "credits"

        hbox pos (1,300):
            box_wrap True
            label _("")
            text _("                       ")
            text _("                A Bellator - ajonid - Alexander Pluntke - Berrie Waterink  - Bob Bailey - Cireful - DodgyNomad - Dominick March - dtgr")
            text _("                      Eden - Falidam - I am Jack's username - Fluffy - gabbledub - Guto Williams - I am Jack's username - Imtiaz Razak")
            text _("                         Justin Benjamin - KP472 - lewis j lorenz - Mark L - Markell Johnson - MIXTURE - Nicholas - Nicholas Gowen")
            text _("                                Niclas Plenter - NomadPG - Phillip Frabott - RestoWyntar - Robert Wolf - Ryan Schwegel - TYR")
            text _("                                                                 Valkyrie65 - Walle - William Dewall - Zyler Gamer")
            text _("                                                                                                                                  ")
            text _("                                                                 Special thanks to Bison and Peem for proofreading.")
            text _("                                                              Also a big thank you to all my patrons no matter the tier.")


init -1 style credits_text:
    size 25
    ypos 0
    font "Calibri.ttf"
init -1 style credits_label_text:
    size 40
    yoffset 5
    font "Old Press.ttf"


init -501 screen version_end():
    add qui.version_end_background

    frame padding (60,50) align (.01,.9):
        has vbox
        text "Sup guys,"
        text ""
        text "That's all the work I've done so far on this game."
        text "There's more coming of course so stay tuned."
        text "If you like my work and wanna see more, please consider supporting me."
        text "That'll be a huge motivator and let me know if anyone actually like the shit I write."
        text "Anyways, thanks a lot for playing what's available so far."
        text "Hope you enjoyed it, see you next time."
        text ""

        text ""
        text "Developer,"
        text "Az."
        text ""







init -501 screen version_end():
    variant "touch"
    add qui.version_end_background
    frame padding (60,50) align (.01,.9):
        has vbox
        text "Sup guys,"
        text ""
        text "That's all the work I've done so far on this game."
        text "There's more coming of course so stay tuned."
        text "If you like my work and wanna see more,"
        text "please consider supporting me."
        text "That'll be a huge motivator and let me know"
        text "if anyone actually like the shit I write."
        text "Thanks a lot for playing what's available so far."
        text "Hope you enjoyed it, see you next time."
        text ""


        text ""
        text "Developer,"
        text "Az."
        text ""








init -501 screen ep1_rel_report():
    add gui.main_menu_background
    frame padding (60,50) align (.05,.9):
        has vbox
        text "{color=#F38DBE}[EM]{/color} Affection   : [emLP]/10"
        text "{color=#F38DBE}[EM]{/color} Corruption  : [emCP]/5"
        text ""
        text "{color=#DAF28E}[SG]{/color} Corruption  : [sgCP]/10"
        text ""
        text "{color=#A403F1}[AS]{/color} Corruption  : [asCP]/10"
        text ""
        text "{color=#BD8751}[LU]{/color} Friendship  : [luFP]/5"
        text ""
        text "{color=#8cffff}[OM]{/color} Friendship  : [omFP]/10"
        text ""
        text "{color=#DB0000}Infraction Points{/color} : [omIP]/3"

init -501 screen ep2_rel_report():
    add gui.main_menu_background
    frame padding (60,50) align (.05,.9):
        has vbox
        text "{color=#F38DBE}[EM]{/color} Affection   : [emLP]/12"
        text "{color=#F38DBE}[EM]{/color} Corruption  : [emCP]/7"
        text ""
        text "{color=#DAF28E}[SG]{/color} Corruption  : [sgCP]/18"
        text ""
        text "{color=#A403F1}[AS]{/color} Corruption  : [asCP]/20"
        text ""
        text "{color=#BD8751}[LU]{/color} Friendship  : [luFP]/5"
        text ""
        text "{color=#8cffff}[OM]{/color} Friendship  : [omFP]/10"
        text ""
        text "{color=#DB0000}Infraction Points{/color} : [omIP]/3"

init -501 screen ep3_rel_report():
    add gui.main_menu_background
    frame padding (60,50) align (.05,.9):
        has vbox
        text "{color=#F38DBE}[EM]{/color} Affection   : [emLP]/16"
        text "{color=#F38DBE}[EM]{/color} Corruption  : [emCP]/9"
        text ""
        text "{color=#DAF28E}[SG]{/color} Corruption  : [sgCP]/22"
        text ""
        text "{color=#A403F1}[AS]{/color} Corruption  : [asCP]/22"
        text ""
        text "{color=#BD8751}[LU]{/color} Friendship  : [luFP]/5"
        text ""
        text "{color=#8cffff}[OM]{/color} Friendship  : [omFP]/10"
        text ""
        text "{color=#DB0000}Infraction Points{/color} : [omIP]/3"

init -501 screen ep4_rel_report():
    add gui.main_menu_background
    frame padding (60,50) align (.05,.9):
        has vbox
        text "{color=#F38DBE}[EM]{/color} Affection   : [emLP]/22"
        text "{color=#F38DBE}[EM]{/color} Corruption  : [emCP]/13"
        text ""
        text "{color=#DAF28E}[SG]{/color} Corruption  : [sgCP]/26"
        text ""
        text "{color=#A403F1}[AS]{/color} Corruption  : [asCP]/24"
        text ""
        text "{color=#BD8751}[LU]{/color} Friendship  : [luFP]/5"
        text ""
        text "{color=#8cffff}[OM]{/color} Friendship  : [omFP]/10"
        text ""
        text "{color=#DB0000}Infraction Points{/color} : [omIP]/3"

init -501 screen ep5_rel_report():
    add gui.main_menu_background
    frame padding (60,50) align (.05,.9):
        has vbox
        text "{color=#F38DBE}[EM]{/color} Affection   : [emLP]/22"
        text "{color=#F38DBE}[EM]{/color} Corruption  : [emCP]/15"
        text ""
        text "{color=#DAF28E}[SG]{/color} Corruption  : [sgCP]/30"
        text ""
        text "{color=#A403F1}[AS]{/color} Corruption  : [asCP]/30"
        text ""
        text "{color=#BD8751}[LU]{/color} Friendship  : [luFP]/11"
        text ""
        text "{color=#8cffff}[OM]{/color} Friendship  : [omFP]/10"
        text ""
        text "{color=#DB0000}Infraction Points{/color} : [omIP]/3"

init -501 screen ep6_rel_report():
    add gui.main_menu_background
    frame padding (60,50) align (.05,.9):
        has vbox
        text "{color=#F38DBE}[EM]{/color} Affection   : [emLP]/36"
        text "{color=#F38DBE}[EM]{/color} Corruption  : [emCP]/21"
        text ""
        text "{color=#DAF28E}[SG]{/color} Corruption  : [sgCP]/30"
        text ""
        text "{color=#A403F1}[AS]{/color} Corruption  : [asCP]/30"
        text ""
        text "{color=#BD8751}[LU]{/color} Friendship  : [luFP]/11"
        text ""
        text "{color=#8cffff}[OM]{/color} Friendship  : [omFP]/10"
        text ""
        text "{color=#DB0000}Infraction Points{/color} : [omIP]/3"

init -501 screen ep7_rel_report():
    add gui.main_menu_background
    frame padding (60,50) align (.05,.9):
        has vbox
        text "{color=#F38DBE}[EM]{/color} Affection   : [emLP]/38"
        text "{color=#F38DBE}[EM]{/color} Corruption  : [emCP]/23"
        text ""
        text "{color=#DAF28E}[SG]{/color} Corruption  : [sgCP]/35"
        text ""
        text "{color=#A403F1}[AS]{/color} Corruption  : [asCP]/37"
        text ""
        text "{color=#BD8751}[LU]{/color} Friendship  : [luFP]/11"
        text ""
        text "{color=#8cffff}[OM]{/color} Friendship  : [omFP]/10"
        text ""
        text "{color=#DB0000}Infraction Points{/color} : [omIP]/3"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
