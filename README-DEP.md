# 2TML: table-top-modelling-language

The idea behind this project is a system for defining the rules, mechanics, and data for a tabletop roll playing game such that instead of having a natural language
document describing the game you end up with what is essentially an indexed and searchable wiki/knowledge graph and a dynamic schema with a set of functions acting on it.

## Motivations and preface

Ever since I moved to playing dnd online I've been seriously underwhelmed by the ecosystem of digital tools available. After pouring over many, many projects and tools I've come
to the conclusion that ttrpg tools end up subpar because all the devs are independently implementing huge amounts of logic for even one aspect of gameplay, they're all reinventing
the wheel because there's no unified or digital representation of the game they can build off of.

## What I think a fully digitized ttrpg in a machine readable format could consist of.

If you break an entire ttrpg system out of a sourcebook and analyze the pieces I think you can classify any given element (rule or data) as what I've termed 'semantic' or 'computable'
content.

Computable: an element of the game that can be perfectly represented in and executed by code, this is the subset of a game system that can be fully modeled by a program and is in essence a schema + series of functions and procedures

Semantic: All elements that are "fuzzy" to a computer and not possible to directly represent with code. Primarily natural language descriptions.

## How I see this benefitting game devs

For any decently crunchy rpg system like dnd or pathfinder the game developers/designers have to keep track of a massive amount of information that makes up their entire RPG system.
While there are many ways to organize their system to help them keep track effectively with charts / diagrams etc without the system being understood by a computer the developers
are still the thing computing all of that information and turning it into a mental schema.

I figure if they're already developing an entire schema + operations for their game in natural language / spreadhseets give them a way to define the computable portion of their system
into and actual program. The benefits of this could be huge, imagine a DSL similar to lua + sql (with the 4 data language sub types), an interactive REPL/Terminal, and tools to visualize their schema into something like interactive UML diagrams. I see this as removing tons of mental overhead, a flat productivity boost, and the power to refine their system's rules for consistency, completeness, simplicity, and quality.

The semantic portion of the system could be described akin to a knowledge graph or semantic web similar to a wikia or RDL. The benefits of this would again be visualization/organization. Querying etc. If the semantic portion was well defined this could create some very interesting uses for natural language processing and understanding; I'm thinking things like natural language queries to instantly find the exact section of content you're looking for etc. Hypothetically if this project was realized then long term I picture
this section becoming very interesting indeed. 

## What this would do for software devs 

The idea is the output of the game dev system can create a batteries included off the shelf interface, API, library fully defining a game that could then be consumed by other programs. Saving ungodly amounts of time and preventing wheels from being reinvented. Devs would be able to jump almost straight into developing their actual application instead
of implementing rules.

## The potential end result for players

As a downstream effect player get more mechanically refined games supported by far more refined, polished, and powerful tools.

But what I think would be the true achievement of this project is some sort of very smart GUI psuedo-terminal with IDE like features, intellisense, and clickable keywords as buttons
that they use to interact with and play the game itself in person or on a VTT.

### Disclaimer: the goal of this project and even the computable portion is firmly not to over automate a table top game and turn it into a video gam. 


------------- SHORTEN THIS SECTION: JUST GET ACROSS POINT ABOUT THE IDEAL TOOLS AND GAMING SETUP DOESN'T AUTOMATE EVERYTHING FOR YOU IT LETS YOU PLAY THE GAME QUICKLY WITHOUT SLOWING YOU DOWN OR GETTING IN YOUR WAY; THE PERFECT TOOLSET OR SETUP SHOULD LET YOU PLAY AT NEARLY THE SPEED OF THOUGHT OR I/O ----------------

My idea for this terminal is to do for playing/running ttrpgs what Vim and Emacs do for typing and editing documents; that is when you master them you can type at the speed of thought. I think the ultimate ttrpg tool is not a VTT automating all the crunch and bookkeeping, I think it's something that lets you play at the speed you can make decisions, communicate, and take in relevant info. If you can query the exact rule or piece of content you need and get it instantly you don't need to go to google or start flipping through physical books. If you can near instantly manipulate the state of the game, have actors take actions etc, there is the potential to do this much faster than clicking through many buttons to do the same thing, which can also lead to opening up menus and googling howtos to do that thing on your VTT, if you can even do it at all. Instead just type out lighting
quick type safe autocompleted commands stating what you do or what should change in near plain english. 


















This repo is the current home for what I'm currently calling 'table top modeling language.' 

The idea for this project came from the realization that TTRPGs are still developed as natural language documents, and huge amounts of repeated work after the fact
goes into creating digital representations of game systems by hand. 

The basic idea is an application and/or system that lets game designers and developers define the rules and data of their game in a fully machine understandable format akin
to a schema, without having to know any programming.

I think such a thing has the potential to give a lot of power to game devs and remove a ton of mental overhead from the process.

The real boon in my mind though is the programmers making tools, platforms, and content for ttrpgs. Every VTT and big app is stuck having to rewrite huge, huge amounts of logic to handle game mechanics. This has not led to the best tools.

The idea is that the software developers are able to take part of the output from the game designers and instantly have a complete digital reresentation of a game's rules and mechanics to act as an interface or library in their own applications. Saving huge amounts of time/effort and leading to vastly better tools.
