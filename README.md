# ChatGPT Hangman Plugin

I've been messing around in another project adding memory to ChatGPT, but it's really hard to get it to keep track of complex state.

You can see this if you try to play Hangman against it. It often starts off well, but eventually, it will put your guessed letters in the wrong place, or just add random letters instead of underscores.

So I thought, why not make a plugin to do this instead!

You can see it in action in this video. At about 4 minutes in you can see the issues with ChatGPT, and then at 5 minutes we build and test the plugin.

The video has a bunch of other interesting things - I've been experimenting with adding emotion and personality to my bot...

[![Demo Video](https://img.youtube.com/vi/4oQUsiPsbOQ/0.jpg)](https://www.youtube.com/watch?v=4oQUsiPsbOQ)

# Installation

To run this locally, set up a virtual environment and then install the requirements:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Then you can run the plugin with:

    python main.py

# Issues

I had problems installing the plugin using localhost so I ended up using ngrok and then using its URL - if you do this then make sure you update the URLs in ai-plugin.json.

The code is VERY simple - DO NOT use this in production! It's just a proof of concept.

The game state is global so it's not possible to play multiple games at once.