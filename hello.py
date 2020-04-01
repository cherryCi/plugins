import sublime
import sublime_plugin
import time
import datetime

class FormatStampCommand(sublime_plugin.TextCommand):
	def format_timestamp(self, timeStamp):
		if timeStamp:
			timeStamp=float(timeStamp/1000) 
			timeArray = time.localtime(timeStamp)
			otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
			return otherStyleTime
		else:
			return time.strftime(format)


	def run(self, edit):
		window = self.view.window()
		view = window.active_view()
		for region in self.view.sel():
			if region.empty():
				selection = sublime.Region(0,self.view.size())
				selected_text = self.view.substr(selection)
				print(type(selected_text))
				timmeStyleTime = self.str_to_timestamp(str(selected_text))
				self.view.run_command("example",{"contents": " %s " % timmeStyleTime})
			else:
				self.view.insert(edit, 0, 'error\n')
