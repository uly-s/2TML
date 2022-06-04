## The definition of a highly interconnected dynamic system satisfying many constraints
Reading through this list of all of sqlite's constraints
https://www.w3resource.com/sqlite/sqlite-constraint.php

1. Right away I can see that at least during the development phase of a game system there would have to be a lot more trigger actions than you would see in a normal schema
2. There needs to be a lot of default constraints on columns
3. No one size fits all approach will work for development; people have different needs and methods. Thus:
4. There should be high level configuration and template/macro system
	a. allow defaults to be set for various constructs, things like defining unsigned numbers as default
    b. allow a macro system to define resuable statements and expressions at a lower level than procedures/functions
    c. allow a system for named columns, compound data types, and enums for composability and reusability
    d. allow operations as a data type; be that from the macro system or with full blown procedures.
5. there is a need for a rich meta data tagging system, allowing semantic annotations of any element
6. Basic collections as data types or designated named collections like a key/val table as a dictionary
7. Aside from dictionaries both trees and graphs can be implemented as tables, this could be useful.
8. It is possible to store, query, parse, and manipulate arbitrary blobs of json or xml as columns
9. Some degree of prologue like functionality for very fine grained definition or verifiability
10. Ability to exclude sections of the schema from hard validation or constraint satisfaction
11. A versioning and branching system
12. A rich and powerful system of stored custom procedures (with event driven functions?)
13. Some system for solving limited constraint satisfaction problems
14. Transactions of course
15. Some system to show the consequences of a schema update or operation without actually executing it?
16. System for storing limited semantic data, enough to document/explain different elements and structures

For 4. to be possible and persistent a game schema needs not just the game definition but a series of tables to define and store components for the rest of the game

5 is just more tables, similar to auditing logs

6 is easy at least for dictionaries

7 is hard if you allow for defining totally arbitrary trees or graphs; must be limited

8. this is built in to sqlite 

9/10 & 11: Look up prologue, GDL, and Coq

12 just google how procedures/functions are stored

14 research how transactions are implemented

15 I dont even know really

16 easy

