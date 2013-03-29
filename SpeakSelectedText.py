import subprocess
import sublime, sublime_plugin

class SpeakSelectedTextCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selections = self.view.sel()
    selection = self.view.substr(selections[0])
    selection = selection.replace('"', '\\"')

    process = subprocess.Popen( "ps aux | grep say | wc -l", shell = True,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE
                              )
    processes, error = process.communicate()
    processes = processes.strip()

    if int(processes) > 2:
      subprocess.Popen( "killall say", shell = True,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE )
    else:
      subprocess.Popen( 'say "{0}"'.format(selection), shell = True,
                                                       stdout = subprocess.PIPE,
                                                       stderr = subprocess.PIPE )
