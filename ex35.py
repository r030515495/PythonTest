# -*- coding: utf-8 -*-
#!/usr/bin/env python


from sys import exit

def gold_room():
    print "This room is full of gold "
    
    next = raw_input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man,")
        
    if how_much < 50 :
        print "Nice"
        exit(0)
    else :
        dead("yout greedy bastarf")
        
        
def bear_room():
    print "dd"