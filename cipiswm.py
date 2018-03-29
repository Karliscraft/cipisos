#!/usr/bin/env python3
from subprocess import check_output as co, Popen as po, PIPE

windows = []
padding = 20, 0, 0, 0 # Change as you like
coordappend = 0, 0
screen_size = tuple(c('wattr', 'wh', c('lsw', '-r')).split())
screen_size[1] -= padding[0] #
coordappend[1] += padding[0]
screen_size[0] -= padding[1]
screen_size[1] -= padding[2]
screen_size[0] -= padding[3]
coordappend[0] += padding[3]
c = lambda *args: co([*args], encoding='utf-8')
po(['xfce4-terminal'])
po(['xfce4-terminal'])
po(['xfce4-terminal'])
po(['xfce4-terminal'])
po(['chromium'])
while len(c('lsw').split()) < 4:
    pass

for positioned, i in enumerate(c('lsw').split('\n')):
    classes = [x.replace(',' '') for x in c('xprop', '-id', i, 'NET_WM_CLASS').split()[2:]]
    if positioned == 0 and 'xfce4-terminal' in classes:
        x, y = 0, 0
        width, height = screen_size[0] / 2, screen_size[1] / 2
    elif positioned == 1 and 'xfce4-terminal' in classes:
        x, y = screen_size[0] / 2, 0
        width, height = screen_size[0] / 2. screen_size[1] / 2
    elif positioned == 2 and 'xfce4-terminal' in classes:
        x, y = 0, screen_size[1] / 2
        width, height = screen_size[0] / 2, screen_size[1] /  2
    elif positioned == 3 and 'xfce4-terminal' in classes:
        x, y = screen_size[0] / 2, screen_size[1] / 2
        width, height = screen_size[0] / 2, screen_size[1] / 2
    else:
        for window in c('lsw'):
            wi
            windows.append({
                'id': window,
                'x': c('wattr x')}))


process = po(['wew'], encoding = 'utf-8', stdout = PIPE)
while True:
    if process.stdout.readline().split(':')[0] == 16:
        new_windowsf = co('lsw')
        new_windows = [x for x in new_windowsf if x not in windows]
        for window in new_windows:

