Nitro cog
This cog provides commands to send Discord Nitro links and manage the available links.

Commands
[p]nitro: Sends a Discord Nitro link in the channel. You can specify the link by providing a name for it after the command, for example: !nitro nerd.

[p]addnitro: Adds a new Nitro link to the list of available links. This command is only available to the bot owner. (adding for requests)

[p]listnitro: Lists all the available Nitro links and their names.


Installation
To install this cog, run the following command in Discord:

DISCLAIMER: These are fake nitros and can be used to troll your freinds.

Copy code
[p]repo add fidind3211 https://github.com/fidind3211/fidind321cogsred
[p]cog install fidind3211 nitro
Replace [p] with your bot's command prefix.

Configuration
This cog does not require any configuration.




Post Cog
The Post cog provides commands for posting messages and embeds to channels. It includes two commands:


post command:

The post command takes four arguments: title, description, color, and channel. It creates an embed with the provided title, description, and color, and then sends the embed to the specified channel. If the color argument is not a valid hexadecimal color code or a color name, an error message will be sent to the channel.

Usage: [pst <title> <description> <color> <channel>

Example: !post "Hello World" "This is a test message." red #genera


postmessage command:

The postmessage command takes two arguments: message and channel. It sends the provided message to the specified channel.

Usage: [p]postmessage <message> <channel>

Example: [p]message "This is a test message." #general

Color Support
The Post cog supports both hexadecimal color codes and color names. To use a hexadecimal color code, simply prefix the code with a # character. To use a color name, enter the name in lowercase without any spaces.

Example usage for hexadecimal color codes:

python
Copy code
[pst "My Title" "My Description" #FF0000 #general
Example usage for color names:

python
Copy code
[pst "My Title" "My Description" red #general

Support
If you encounter any issues with this cog, please contact the bot owner or developer for assistance. (Sparkow#4718, BenCos18#8565)



████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗██╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝██║
░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░██║
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗╚═╝
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚═╝

Thanks to BenCos18 for motivation!!!!!!!
