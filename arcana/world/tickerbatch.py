# -*- coding: utf-8 -*-
 
#HEADER
from evennia import TICKER_HANDLER as tickerhandler 
from evennia.objects.models import ObjectDB
 
#CODE
 
#for each in ObjectDB.objects.all():
#    if each.is_typeclass('typeclasses.objects.Object'):
#        each.db.invis = 0

for each in ObjectDB.objects.all():
    if each.is_typeclass('typeclasses.characters.Character'):
        each.attributes.add("ban", "None")
        each.attributes.add("finalban", 0)
        each.attributes.add("kinetic", 0)
        each.attributes.add("push",0)
        each.attributes.add("rush", 0)
