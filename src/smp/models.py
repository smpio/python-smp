from __future__ import print_function, division, absolute_import, unicode_literals

import enum


@enum.unique
class Medium(enum.IntEnum):
    facebook = 1
    instagram = 2
    twitter = 3
    google = 4
    linkedin = 5
    pinterest = 6
    tumblr = 7
    pushbullet = 8
    telegram = 9
    viber = 10
    snapchat = 11
    periscope = 12
    whatsapp = 13
    slack = 14
    vk = 15
    ok = 16
    bitly = 17


@enum.unique
class PageType(enum.IntEnum):
    user = 1
    public = 2
    group = 3
    event = 4
    bot = 5
