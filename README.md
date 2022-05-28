# 2TML: Table-Top Modelling Language

## Preface 

This has been a zombie repo for some time because when I initially concevied the core idea it was something other's said sounded cool and they could imagine some uses for it, but my conception of it was very vague and abstract to the point where I had no idea what I was even making let alone a roadmap or the next step. However I have been mulling over this idea ever since opening this repo while playing a lot of D&D online, using, investigating, reading about digital tools and systems made for RPGs or just used for them. Something finally clicked and now I know exactly what problem I'm trying to solve and what to make to solve that problem. 

## Problem Statement: the state of tabletop gaming software

The state of software made to play TTRPGs directly in the form of VTTs and to a lesser extend software meant to assist some aspect of play is in a supremely sad state.
Ever since I started tabletop gaming I was befuddled at the quality and quantity of really good tools for playing by far the most popular tabletop game with a majority
market share, dnd5E. The shining exception to this and an example of a polished and near perfect service/application is D&D Beyond. Which until recently wasn't even the official toolset of 5E, just the universially agreed upon unofficial toolset.
Beyond has been a standout success compared to others because It stuck to digitizing 2 core components of playing D&D; 
2. It can manage all of your purchased content and makes all the content you have access to readily searchable and easy to quickly use in your game
1. While 2 is pretty good on an absolute and relative scale the true magic of Beyond is in the digital character sheet and builder. It is an example of truly polished and refined UI/UX design. The DCS fully interops with and can access any content you have on beyond such as spells, subclasses, items. 

While number 2 is mostly confined to major VTT platforms 1 is by a wide margin the most common sort of tool people make for 5E. There is an absolutely huge amount of
apps, websites, services, spreadsheets, and dead github repos implementing a digital character sheet in one form or another. Some were quite popular and pretty good but Beyond blew them all totally out of the water, no contest.

I came up with a test of sorts for tabletop software that I think explains Beyond's success when there were many, many free alternatives:

### To be successful or good a digital tool or piece of software seeking to implement some aspect of a ttrpg must be an outright superior experience to handling that same thing manually.

Be that with a dedicated gdrive for campaign info and a dice roller in discord or good old pen and paper, physical dice, and a dry erase board that is the standard it has to meet to be a success, because if it's not better than doing it the old fashioned way... people will just do it the old fashioned way. Your tool has to definitively enhance a player or DM's experience with a game to where there is no question they have more fun playing with it than without it.

While many tried and many partially succeded I believe Beyond was the first service to turn a digital character sheet into a solved problem. (TODO: explain how it did this). Everything before it was to some extent clunky, buggy, incomplete, or flawed in some way that made picking a DCS/CT a game of tradeoffs and pick your poison. They never fully encompased every use of a character sheet and everything it was supposed to keep track of, or it just didn't do a good enough job of it to standout like Beyond. A common theme I noticed in looking at many tools and services was to crank out a ton of different features but never refining or perfecting them to where you really want to use them and enjoy doing so.

Instead of adding on tons of features for different parts of D&D Beyond focused on refining those core aspects, it adds in new features slowly and carefully and is quick to disable or remove a work in progress that doesn't meet their standards. They add in a feature when it is done right.

That's roughly the state of isolated tools tracking only a subset of 5E / ttrpgs in general. Onto the big boys; virtual table tops. 

## Virtual Tabletops and Automation: a cursed problem



### 1. Queries
Simple lookup commands for quickly finding info without scrolling
  `list all monsters where type=undead and cr<2`
    
### 2. Entity tied macros
Currently in a platform like astral or even roll20 filling out macros for all your moves can be a pain
  `define 'attack' as (d20 + str + prof)`
then just enter `attack` to roll

### 3. Entity management
Entity importing is also a pain with lots of manual entry
  `from monsters import 'winter wolf'`
  
### 4. Rule factoring
Syntax for addition, modification of rules to help manage systems
  `on attack_roll=20 damage *= 2`
  `add skill 'sailing' with attribute 'wisdom'`
  
### 5. unified format for import / export of content
An XML / json like format to make importing items, monsters, subclasses, characters seemless



