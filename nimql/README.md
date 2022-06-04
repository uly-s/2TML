
# NIMQL: A query language for maniacs

This subfolder is to house the "language" (could be a module, library, or even just a format/specification) that will be used to define games (the actual modeling language portion)

## As a disclaimer I'm writing this for myself to work out my thoughts on this as I go; like a scratchpad

I think this needs it's own language as how I imagine is working is in between a lot of things and borrows from many other things. It could be implemented without a specialized language but the complexity and engineering time would be 10x and the end result would just be another complicated ttrpg application and not what I'm aiming for.

- (First off the closest existing language/paradigm I could find to what I want was Rebol)

## What this needs to do and what a query language does 
https://www.techopedia.com/definition/1245/structured-query-language-sql
## Four Categories of SQL Commands

### Data Definition Language (DDL)
This includes CREATE (tables, views, objects, etc.), ALTER and DROP (delete).

### Data Manipulation Language (DML)
SELECT, INSERT, UPDATE, DELETE of records within tables.

### Data Control Language (DCL)
GRANT and/or REVOKE user privileges, etc.

### Database Indexing
CREATE INDEX and DROP INDEX statements are used to create and delete indexes in tables.

**SQL also allows users to build constraints** 
Some examples of SQL constraints include:

**NOT NULL**
Which prevents columns from having a null value.

**UNIQUE**
To ensure all values are different.

### BY FAR THE MOST IMPORTANT PARTS ARE DDL, DML, AND CONSTRAINTS
To define both the semantic and computable portions of a game we'll need more than sql's atomic value data management, but the computable portion can be mostly defined as a sql schema.

### To focus on the computable
Assuming the static rule set and mechanics can be implemented as a static chema with a great many constraints and foreign key relations; there also needs to be some element to describe the state of a game in play and how it changes over time. There also exists a series of relations between the rule schema, game state, and semantic graph of the game that could be useful to define. 

I would strongly assume that a static schema defining the rule set, not related to any instance of the game itself, would be chiefly the concern of game designers before the testing phase. As I want indie game designers as guinea pigs it makes sense to start here.




