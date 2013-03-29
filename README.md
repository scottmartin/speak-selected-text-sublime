# Speak Selected Text for Sublime Text 2

I threw together this plugin so I could use the Mac's text to speech system in Sublime Text 2. I use the "Speak selected text when key is pressed" [feature](http://support.apple.com/kb/PH11255) all the time. When Apple released Lion they changed the way this feature worked, breaking the functionality in a lot of applications. It use to just copy the selected text and read it from the clipboard, making it work in any application that allowed you to copy text. After Lion it uses an API that developers have to add into their application before the feature will work. Just from my day to day use, it seems like the old way worked better.

This plugin was designed for use with Mac OS X and is only needed with OS X 10.7 and higher.

## Installing

Once you have Git installed just go into Sublime's Packages folder and clone the repo.

```bash
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
$ git clone https://github.com/scottmartin/speak-selected-text-sublime.git "Speak Selected Text"
```

## Usage

From within Sublime Text 2 you can use the plugin on of 3 ways.

1. Right click your selection and choose "Speak Selected Text" from the context menu.
2. Use the command palette and search for "Speak Selected Text".
3. Set a keyboard shortcut to the "speak_selected_text" command.

**Note:** You can run the command again to stop the speech at any time.
