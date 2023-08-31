#
#Tema
#Autor:Eliú Moreno Ramírez
#Fecha: 30-08-23
#
import os
import subprocess
from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from libqtile import qtile

#Para decoración de barra widgets
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

color_barra="#353446"
fuente_barra="JetBrains Mono SemiBold"

mod = "mod4"
terminal = guess_terminal()
color="#BF6Da4"
color_light="#00E597"
color_light2="#85ffff"
back="#222222"
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn('kitty'), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Open Menu"),
    Key([mod], "g", lazy.spawn("google-chrome-stable"), desc="Open Chrome"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Control volumen
    Key([],"XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5% ")),
    Key([],"XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5% ")),
    Key([],"XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle ")),
    #captura de pantalla
    Key([mod],"s",lazy.spawn("scrot")),

]

groups = [Group(f"{i+1}", label="◉") for i in range(5)]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod],i.name,lazy.group[i.name].toscreen(),desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=True),desc="Switch to & move focused window to group {}".format(i.name),),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

#Tema actual de cada layout
def init_layout_theme():
    return {"margin":7,
	    "border_width":5,
	    "border_focus":"#a74978",
	    "border_normal":"#4c566a"}

layout_theme=init_layout_theme()

layouts = [
    layout.Columns(**layout_theme),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #layout.Floating(**layout_theme),
    #layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Max(**layout_theme),
    #layout.MonadTall(margin=5, border_width=5, border_focus="#ff0000",border_normal="#4c566a"),
    #layout.MonadWide(margin=5, border_width=5, border_focus="#ff0000",border_normal="#4c566a"),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def search():
	qtile.cmd_spawn("rofi -show drun")

powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash",size=8)
    ]
}

powerline2 = {
    "decorations": [
        PowerLineDecoration(path="back_slash",size=8)
    ]
}


screens = [
    Screen(
        top=bar.Bar(
            [
		        widget.Spacer(length=15,background=color_barra,),#Espacio
                #Escritorio nombre
		        widget.GroupBox(fontsize=24,borderwidth=3,highlight_method='block',active='#CAA9E0',block_highlight_text_color="#91B1F0",highlight_color='#4B427E',inactive='#282738',foreground='#000000',background=color_barra,this_current_screen_border='#353446',this_screen_border='#353446',other_current_screen_border='#353446',other_screen_border='#353446',urgent_border='#353446',rounded=True,disable_drag=True,),         

                #widget.Prompt(),
		        
                #Busqueda en rofi
		        #widget.TextBox(fmt='Search', background='#282738',font="JetBrains Mono Bold",fontsize=13,foreground='#CAA9E0',mouse_callbacks={"Button1": search},),

		        #Ventana actual
                widget.WindowName(background = color_barra,format = "{name}",font=fuente_barra,foreground='#ffffff',empty_group_string = 'Desktop',fontsize=13,),
                #widget.Checkupdates(
                #    custom_command="checkupdates",
                #    backgound="555555",
                #    update_interval=1800,
                #    colour_have_updates="00ff00",
                #    colour_no_updates="ff5500",
                #    display_format="Actualizacions:{updates}",
                #    padding=10,
                #    ),
               # widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff"),},name_transform=lambda name: name.upper(),),
                
                #Widget sistema
                widget.Systray(background=color_barra,fontsize=2,),
                widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline2), #Separacion
                #Info CPU
		        widget.Sep(linewidth=0,padding=3,foreground="#e9d0de",background=color_barra,**powerline2), #Separacion
		        widget.CPU(format="CPU:{load_percent}%",foreground="#000000",background="#BC92C1",font=fuente_barra),
		        widget.TextBox(text="T=",foreground="#000000",background="#BC92C1",font=fuente_barra,padding_y=3),
                widget.ThermalSensor(foreground="#000000",background="#BC92C1",font=fuente_barra,threshold=50,**powerline),
                
        		widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline), #Separacion
                #Info GPU
                widget.NvidiaSensors(format='GPU: T={temp}°C',foreground="#000000" ,font=fuente_barra, background="#7DACC0",**powerline2),
        		widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline2), #Separacion
		        
                #Info Memoria ram
                widget.Memory(format='RAM: {MemUsed: .0f}{mm}',foreground='#000000',background="#a3cde0",font=fuente_barra,fontsize=13,update_interval=5,**powerline ), 		
		        widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline), 
                
                #Hora y fecha
		        widget.Clock(format="%d-%m %I:%M %p",foreground="#000000",background="#abc193",font=fuente_barra,**powerline2),		
		        widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline2),
    
                #volumen
                widget.TextBox(text="Vol:",foreground="#000000",background="#eed290",font=fuente_barra),
                widget.PulseVolume(foreground="#000000",background="#eed290",limit_max_volume=False,font=fuente_barra,**powerline),
                widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline), 
		
                #Red
                widget.Net(format='{down}↓↑',font=fuente_barra,foreground="#000000", background="#d88c74",**powerline2),
		        widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline2),

                #Layout
		        widget.CurrentLayout(foreground="#000000",background="#b76a77",font=fuente_barra,**powerline),
		        widget.Sep(linewidth=0,padding=1,foreground="#e9d0de",background=color_barra,**powerline), 
                
                #Bateria




                #Log out
                widget.QuickExit(default_text="Exit",foreground="#ffffff",background=color_barra,font="JetBrains Mono Bold",countdown_format="[{}]"),widget.Sep(linewidth=0,padding=10,foreground="#e9d0de",background=color_barra), 
            ],
            32,
            #background="#282738",
            opacity=0.8, #opacidad barra 
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            margin = [10,20,6,20], #Margen barra
	  # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
