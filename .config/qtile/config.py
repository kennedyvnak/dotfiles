from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"

keys = [
    # Window Control
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left",),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right",),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Actions
    Key([mod], "q", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "s", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget",),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc="powermenu"),
    Key([mod], "w", lazy.spawn("sh -c ~/.config/rofi/wallpaper.rasi"), desc="wallpaper"),
    Key([mod], "e", lazy.spawn("nemo"), desc="file manager"),
    Key([mod], "o", lazy.spawn("flameshot gui"), desc="Screenshot"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Multimedia
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
]

groups = [Group(f"{i+1}", label="󰏃") for i in range(8)]
for i in groups:
    keys.extend([
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        margin=[5, 5, 5, 5],
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        border_width=0,
    ),
    layout.Max(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        margin=5,
        border_width=0,
    ),
    layout.Floating(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        margin=5,
        border_width=0,
    ),
    layout.Stack(num_stacks=2),
    layout.Bsp(),
    layout.Matrix(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        margin=5,
        border_width=0,
    ),
    layout.MonadTall(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        margin=5,
        border_width=0,
    ),
    layout.MonadWide(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        margin=5,
        border_width=0,
    ),
    layout.Tile(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
    ),
    layout.VerticalTile(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [widget_defaults.copy()]

def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")

screens = [
    Screen(
        wallpaper="~/.config/qtile/current_wallpaper.jpg",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.Spacer(
                    length=15,
                    background="#282828",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/launch_Icon.png",
                    margin=2,
                    background="#282828",
                    mouse_callbacks={"Button1": power},
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/6.png",
                ),
                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method="block",
                    active="#928374",
                    block_highlight_text_color="#D3C6AA",
                    highlight_color="#4B427E",
                    inactive="#282828",
                    foreground="#4B427E",
                    background="#3C3836",
                    this_current_screen_border="#3C3836",
                    this_screen_border="#3C3836",
                    other_current_screen_border="#3C3836",
                    other_screen_border="#3C3836",
                    urgent_border="#3C3836",
                    rounded=True,
                    disable_drag=True,
                ),
                widget.Spacer(
                    length=8,
                    background="#3C3836",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/1.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/layout.png", background="#3C3836"
                ),
                widget.CurrentLayout(
                    background="#3C3836",
                    foreground="#928374",
                    fmt="{}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/search.png",
                    margin=2,
                    background="#282828",
                    mouse_callbacks={"Button1": search},
                ),
                widget.TextBox(
                    fmt="Search",
                    background="#282828",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground="#928374",
                    mouse_callbacks={"Button1": search},
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/4.png",
                ),
                widget.WindowName(
                    background="#3C3836",
                    format="{name}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground="#928374",
                    empty_group_string="Desktop",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/3.png",
                ),
                widget.Systray(
                    background="#282828",
                    fontsize=2,
                ),
                widget.Spacer(
                    length=-7,
                    background="#3C3836",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/6.png",
                    background="#3C3836",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/ram.png",
                    background="#3C3836",
                ),
                widget.Spacer(
                    length=-7,
                    background="#3C3836",
                ),
                widget.Memory(
                    background="#3C3836",
                    format="{MemUsed: .0f}{mm}",
                    foreground="#928374",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/7.png",
                    background="#3C3836",
                ), 
                widget.Spacer(
                    length=8,
                    background="#3C3836",
                ),
                widget.NvidiaSensors(
                    background="#3C3836",
                    foreground="#928374",
                    font="JetBrains Mono Bold",
                ),
                widget.Spacer(
                    length=-4,
                    background="#3C3836",
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/7.png',
                    background='#282828',
                ),
                widget.Spacer(
                    length=4,
                    background="#3C3836",
                ),
                widget.HDDBusyGraph(
                    background="#3C3836",
                    border_color="#282828",
                    graph_color="#928374",
                    fill_color="#3C3836",
                    samples=50,
                    type="line"
                ),
                widget.Spacer(
                    length=-4,
                    background="#3C3836",
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#282828',
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/clock.png",
                    background="#282828",
                    margin_y=6,
                    margin_x=5,
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background="#282828",
                    foreground="#928374",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),
                widget.Spacer(
                    length=18,
                    background="#282828",
                ),
            ],
            30,
            border_color="#282828",
            border_width=[0, 0, 0, 0],
            margin=[5, 5, 5, 5],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position(),),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#1F1D2E",
    border_normal="#1F1D2E",
    border_width=0,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser("~/.config/qtile/autostart_once.sh")])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
