# Speak Selected Text for Sublime Text 2

I threw together this plugin so I could use the Mac's text-to-speech function in Sublime Text 2. I use the "Speak selected text when key is pressed" [feature](http://support.apple.com/kb/PH11255) all the time. When Apple released Lion, they changed the way this feature worked, breaking the functionality in many applications. Prior to Lion, the feature simply copied the selected text and read it from the clipboard, making it work in any application that allowed you to copy text. After Lion's release, it now uses an API that developers must add to their applications before the feature will work. From my day-to-day use, it seems like the old way worked better.

This plugin was designed for use with Mac OS X, and it is only needed for OS X 10.7 and higher.

## Installing

Once you have Git installed, just go into Sublime's Packages folder and clone the repo.

```bash
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
$ git clone https://github.com/scottmartin/speak-selected-text-sublime.git "Speak Selected Text"
```

## Usage

From within Sublime Text 2, you can use the plugin one of three ways.

1. Right-click your selection and choose "Speak Selected Text" from the context menu.
2. Use Sublime's command palette and search for "Speak Selected Text".
3. Create a Sublime Text key-binding mapped to the "speak_selected_text" command (note that the key-binding cannot be the same as the OS shortcut, or the OS shortcut will override it).

**Note:** You can run the command again to stop the speech at any time.
