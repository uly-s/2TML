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

By far the most mechanically intensive part of playing 5E is running combat encounters on a concrete map. Combat can be done without a physical map or tabletop in which case you can get great mileage out of Beyond and Discord with a bot for playing DND and interacting with beyond or a similar setup. A full on VTT can be used the same way but most people tend to prefer map based combat in general. 

Making a really good VTT is a genuinely hard problem, there's a massive amount of logic, rules, and data to implement for a game like 5E and thus tons of features and functionality to develop just to digitize the core essentials needed to play 5E similar to how you could in person. So a well done comprehensive VTT represents a huge amount of developer hours in an industry with a small overall market cap, of which you are only targeting the people that play online. 

The boon and promise of a VTT over meatspace is the specter or automation; playing 5E and especially combat involves a totally ridiculous amount of rules and moving pieces you have to keep track of one way or another. There are many digital combat trackers that act as a standalone application for overseeing and running combat, just tracking is not that hard to do well but automating combat is hard. Only certain parts of what goes into combat can even be automated.

### Segway: hard versus soft data in 5E/ttrpgs

From a software perspective DnD comes with two types of rules and data: which I've dubbed hard data/rules and soft data/rules. Hard refers to the portion of dnd that a computer can unambiguously understand and imeplement. Think numerical, categorical, boolean bits of data associated with various key words and a set well defined operations on the data/keywords that could all be represented in a schema or implemented with relatively basic programming constructs. Math, logic, and processes.

Soft refers to any part of the game described and handled by natural language. Dialogue, flavor, descriptions. Stuff that is just a meaningless string or image to a computer.

A VTT has a sort of implicit 'game state' tracking all the hard data and modifying it with hard rules.

## Back to VTTs

A VTT or software in general can obviously only directly implement and thus automate (to an extant) the hard aspects of a TTRPG. Ideally it facilitates or even improves the soft aspects in some way, or at least never gets in the way of them.

While this is not even remotely a hard and fast rule, I've found that too much automation or just poorly done automation of the hard rules, or worse: an attempt to implement soft data parts of the game in some way directly can totally stifle creativity and at least representing the results of free form play; it then becomes essentially a subpar video game.

So the ideal VTT automates all the boring parts of whatever you're doing while also allowing you to maniuplate the state of the game totally arbitrarily according to the soft aspects of play, such as the DM modifying the map mid combat with lots of flames to account for a PC starting a fire in a way their character sheet has no button for.

(NEED TO CLEAN THIS UP LATER AND MOVE STUFF TO SUB SECTIONS)

The problem is what exactly you want to automate and what parts of the game state you want to change manually are context dependant and change over time. You may have been quite happy with the VTT resolving and applying all your attack rolls the past however many turns, but now you want to do something non standard and creative but you're struggling to figure out how to get the VTT to let you do this. At worst forcing mental overhead on people remembering the result of your roleplay but at least pausing the entire game while you struggle with options, menus, and buttons.

Thus I consider ttrpg automation a cursed problem (one with a contradictory solution): You want a VTT to automate exactly what you want it to at that moment while also allowing you to make any arbitrary change at any time, easily and without it getting in your way.


## But why is it like this?

I think the overall space of ttrpg software is a hugely unexplored and underdeveloped with tons of potential. I think it is this way because ttrpgs are fundamentally developed just like they've always been: for meatspace to be consumed by thinking humans.

Thus any digital tool or VTT has to take a natural language book and implement in code the parts of the game they need for an application. For a big app like a full VTT this means creating a massive model of the entire game. From scratch or bits and pieces.

The wheel has been reinvented on this many, many times. In many different formats and languages. But none is really complete or extensible and reused between applications. Instead we have dozens, hundreds, maybe thousands of implementations of the 5E system scattered across the internet. None complete, comprehensive, or official and thus able to serve as a basis for a tool or VTT, most of which end up not great because there's huge amounts of interconnected logic to implement for even simple UI features witch then need to be heavily refined and polished for people to actually like and use what you're making.


## My solution: digital first development with specialized tools for non developer game designers

So when a game developer develops a game with a serious amount of crunch, data, mechanics defined by the rules. For the hard data/rules they are essentially defining a potentially quite intricate and complex schema, graph, algorithm that make up the rules for the game... in natural language. They're then responsible for making this NL defined schema complete and consistent across every possible act of game play. The rules can't ambiguously contradict each other and they can create very complex interactions between each other in ways they could not see coming. They may have to crunch a great deal of numbers to balance player ability, they have to plan around any way a player could develop their character to prevent things that could tottally break the game.

## So people are defining a huge schema with algorithms acting on it in natural language, and then other people are tasked with trying to decipher from documents what that schema and algorithm look like in code.

So why not just define the game digitally in the first place? With the hard/data rules defined by game devs stored in a machine readable format. So when a game dev creates a book, document, website etc to distribute their game the the digital version of the rules is already implemented and ready to go.

## How?

## 1. game design stage

An application or system for game devs to help them define and develop the rules system for their game such that the system is stored internally in a robust machine readable format. The front end I imagine as a custom RPG editor suite that provides various tools to develop a model, such as a visual UML or ER diagram editor, a prologue like interface for defining and tracking rules, an SQL like DSL with a graphical builder as well as psueodo-terminal and script editor. 
The ability to embed, reference, link various entities into NL documents, assign keywords to parts of the system for searching.
Let them visualize their rule system, experiment and run simulations of gameplay. Run queries against parts of their system. Check for balance and consistency. 

The idea is to build something for the game devs they want to use because it's taking huge amounts of mental overhead off of them, letting them develop a better game faster. If you just give them another chore they won't use it

## 2. tool and platform development

A game made and released with the application from 1. can export a ready made model of the game for consumption by other programs. It would probably be best if the model output by 1. was in some intermediate format easily translatible for use as an API/ABI/Interface in various languages configured to various needs. Has to strike a balance between power and compatibility. End goal is just to save software devs a huge amount of time and let them focus on developing their actual application without getting bogged down in business logic. This would also allow for total interoperability of content between platforms. 

## 3. consumption by players

I posit that tools and and platforms built on this system could be a lot more powerful and more polished as a baseline, but my dream for this is not to interact with the game through buttons and menus, but to provide a kind of smart GUI psuedo-terminal to players and especially GMs

The power of learning vim/emacs and even just knowing all the keyboard shortcuts for your operating system is the ability to interact with a computer or type at the speed of thought instead of the speed of your mouse. I imagine a similar possibility for ttrpgs, a vim/emacs for gaming + ide intellisense features + basic nlp technology that let's you play at the speed of thought (or really the speed at which you make decisions, communicate, and can read relevant info). A terminal for VTTs giving you full expressive power over the game.

((MORE ON THIS LATER))



----------- blah blah------------
A combination of internal/external DSLs and SQL like data definition/manipulation language + scripting, serving as the core of the backend for a series of frontend UI applications.



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



