import math
import gzip
import sublime, sublime_plugin

class FileSizeStats(sublime_plugin.EventListener):
	def update(self, view):
		r = sublime.Region(0, view.size())
		text = bytes(view.substr(r), 'utf-8')
		bytes_len = len(gzip.compress(text))
		kb_len = math.ceil( bytes_len / 1024)
		view.erase_status("gzippedSize")
		view.set_status("gzippedSize", "gzipped: ~%s KB" % kb_len)


	on_post_save_async = update
	on_modified_async = update
	on_activated_async = update