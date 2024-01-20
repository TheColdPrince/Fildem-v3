#!/usr/bin/python3

import dbus

def format_label(parts):
    separator = u'\u0020\u0020\u00BB\u0020\u0020'
    return separator.join(parts)

class DbusGtkMenuItem(object):
    def __init__(self, item, path=[], enabled=True):
        self.path = path
        self.separator = False
        self.action = str(item.get('action', ''))
        self.accel = str(item.get('accel', ''))
        self.shortcut = str(item.get('shortcut', ''))
        self.label = item.get('label', '')
        self.text = format_label(self.path + [self.label])
        self.enabled = enabled
        self.toggle_type = ''
        self.toggle_state = False
        self.section = None

    def set_toggle(self, toggle):
        if toggle:
            toggle = toggle[0]
            if isinstance(toggle, dbus.Boolean):
                self.toggle_type = 'checkmark'
                self.toggle_state = toggle
            elif isinstance(toggle, str):
                self.toggle_type = 'radio'
                self.toggle_state = bool(toggle)

class DbusOption(object):
    def __init__(self, path, object_path):
        print(dbus.SystemBus().get_object(path, object_path), False)

class DbusAppMenuItem(object):
    def __init__(self, item, path=[]):
        self.path = path
        self.action = int(item[0])
        self.accel = self.get_shortcut(item[1])
        self.separator = item[1].get('type', '') == 'separator'
        self.label = item[1].get('label', '')
        self.text = format_label(self.path + [self.label])
        self.enabled = item[1].get('enabled', True)
        self.visible = item[1].get('visible', True)
        self.toggle_state = item[1].get('toggle-state', 0) == 1
        self.toggle_type = item[1].get('toggle-type', '')  # 'radio' or 'checkmark'
        self.icon_data = item[1].get('icon_data', bytearray())
        self.section = None
        self.children = []

    def get_shortcut(self, item):
        shortcut = item.get('shortcut', '')
        if shortcut:
            return ''.join(['<' + v + '>' if i != len(shortcut) - 1 else v for i, v in enumerate(shortcut)])
        return shortcut
