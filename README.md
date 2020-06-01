# 2TML: Table-Top Modelling Language

## Possible use cases (most assuming a command line interface, ex roll20 chat window)

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



