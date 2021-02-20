# fantasy-name-generator

This is a fantasy name generator that works as a Discord bot. 
Simply set the environment `OAUTH_TOKEN` to your bot token for it to work.

## Changing the Bot
To edit the bot, go to the `bot` file. There you will mostly find a whole 
lot of functions.

### Changing commands
You will find functions that look something like this

```
@client.command() 
async def male(ctx): 
    await ctx.send(main.generate(main.reset(), "m"))
```
The "male" part on line two is what the user will have to input. The `ctx.send` is
what the bot will say. These can be changed at your leisure.

### Changing command prefix
`client = commands.Bot(command_prefix='g!')`

The above code is where the prefix is dictated. So someone using the bot will have
to type "g!__". At the end of this line of code is the "g!". If you change this to
something else, you will have to input that string before the command to call the
bot.

## Changing names

Simply go the tuples in `main` (`malenames`, `femalenames` and `familynames`) and
change to the names to something that you want. It will automatically adjust.

## Using the bot
At the moment, when you hop into Discord you will have to first add the bot, or clone
it with your own code document. Then you type in "g1", followed by either male
or female. It will print the respective gender name followed by a second name, all
randomly determined.
