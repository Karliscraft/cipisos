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
    if positioned == 0:

process = po(['wew'], encoding = 'utf-8', stdout = PIPE)
while True:
    if process.stdout.readline().split(':')[0] == 16:
        new_windowsf = co('lsw')
        new_windows = [x for x in new_windowsf if x not in windows]
        for window in new_windows:

