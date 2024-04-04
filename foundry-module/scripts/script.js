Hooks.on("init", function() {
  console.log("This code runs once the Foundry VTT software begins its initialization workflow.");
});

Hooks.on("ready", function() {
  console.log("This code runs once core initialization is ready and game data is available.");
});

Hooks.on("chatMessage", function(chatLog, message, chatData) {
    console.log("-- CHAT MESSAGE --");
    console.log(chatLog);
    console.log(message);
    console.log(chatData);
})

/*
    For next steps
    take a look at https://foundryvtt.com/article/macros/
    looking at https://foundryvtt.com/api/modules/hookEvents.html and the data in chatMessage
    and https://foundryvtt.com/api/classes/foundry.documents.BaseChatMessage.html for the chatMessage object
    and https://foundryvtt.com/api/classes/foundry.documents.BaseChatMessage.html#data for the chatData object
    Also, the chatData object has a "type" property that can be used to determine if the message is a chat message, a roll message, etc.
    The type property is a string and can be "message", "roll", "whisper", "blindroll", "selfroll", "gmroll", "system", "emote", "other"

    The next step I'm thinking of for the use case I envision '/cast magic missile at goblin' is to parse the message and determine if it's a spell cast and if so, what spell is being cast and who it's being cast at.
    I'm thinking of using the '/cast' as a trigger and then parsing the rest of the message to determine the spell and target.

    Doing this with an LLM is going to be almost hectic, as I need to parse the message and then determine if the spell is in the character's spell list and then if the target is a valid target for the spell.
    Whereas if I do this with a macro, I can just use the chatData object to determine the spell and target and then use the actor object to determine if the spell is in the character's spell list and if the target is a valid target for the spell.
    I think I'm going to go with the macro route for now and then maybe look into the LLM later.

    this keeps making me think of todoist NLU for dates and times and such
*/