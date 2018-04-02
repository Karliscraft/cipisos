#!/usr/bin/env python3
from subprocess import check_output as co, Popen as po, PIPE
from random import randint
import Xlib
import Xlib.X as X
from Xlib.display import Display

workspaces = {
        "terminals": [],
        "browser": [],
        "normal": []
        }

readable_names = {
        "terminals": "Terminals",
        "browser": "Browser",
        "normal": "Normal"
        }


display = Display()
padding = 20, 0, 0, 0 # Change as you like
coordappend = 0, 0
root = display.screen().root
screen_geometry = root.get_geometry()
screen_size = screen_geometry.width, screen_geometry.height
screen_size[1] -= padding[0] #
coordappend[1] += padding[0]
screen_size[0] -= padding[1]
screen_size[1] -= padding[2]
screen_size[0] -= padding[3]
coordappend[0] += padding[3]
rules = {
        'terminals': [
            {
                'class': 'xfce4-terminal',
                'objects': [
                    {
                        'x': 0,
                        'y': 0,
                        'width': screen_size[0] / 2,
                        'height': screen_size[1] / 2,
                        'state': 'normal'
                        },
                    {
                        'x': screen_size[0] / 2,
                        'y': 0,
                        'width': screen_size[0] / 2,
                        'height': screen_size[1] / 2,
                        'state': 'normal'
                        },
                    {
                        'x': 0,
                        'y': screen_size[1] / 2,
                        'width': screen_size[0] / 2,
                        'height': screen_size[1] / 2,
                        'state': 'normal'
                        },
                    {
                        'x': screen_size[0] / 2,
                        'y': screen_size[1] / 2,
                        'width': screen_size[0] / 2,
                        'height': screen_size[1] / 2,
                        'state': 'normal'
                        }
                    ]
                }
            ],
        'browser': [
            {
                'class': 'chromium',
                'objects': [
                    {
                        'x': 0,
                        'y': 0,
                        'width': screen_size[0],
                        'height': screen_size[1],
                        'state': 'normal'
                        }
                    ]
                }
            ]
        }

def lsw(mapped=True, unmapped=False, ignorable=False, not_ignorable=True):
    windows = []
    for x in root.query_tree().children:
        attr = x.get_attributes()
        if not ignorable and attr.override_redirect == 1 \
                or not not_ignorable and attr.override_redirect == 0 \
                or not mapped and attr.map_state == X.IsViewable \
                or not unmapped and (attr.map_state == X.IsUnviewable or attr.map_state == X.IsUnmapped):
            continue
        else:
            windows.append(x)

def switch_workspace(fromw, tow):
    for window in workspaces[fromw]:
        window.unmap()
    for window in workspaces[tow]:


c = lambda *args: co([*args], encoding='utf-8')
def position_window(window):
    classes = window.get_wm_class()
    for workspace in rules:
        for class_ in workspace:
            if "positioned" not in class_:
                class_["positioned"] = 0
            relevant_rule = class_[objects][class_["positioned"]]
            workspaces[workspace].append(
                    {
                        "x": relevant_rule["x"] + coordappend[0],
                        "y": relevant_rule["y"] + coordappend[1],
                        "width": relevant_rule["width"],
                        "height": relevant_rule["height"],
                        "window": window
                        }
                    )
            class_["positioned"] += 1

        
root = display.screen().root
mask = (X.SubstructureNotifyMask | X.SubstructureRedirectMask)
root.change_attributes(event_mask=mask)
current_workspace = 'normal'
po(['xfce4-terminal'])
po(['xfce4-terminal'])
po(['xfce4-terminal'])
po(['xfce4-terminal'])
po(['chromium'])
while True:
    event = display.next_event()
    if event.type == 16:
        if rules:
            position_window(window)
        elif 
