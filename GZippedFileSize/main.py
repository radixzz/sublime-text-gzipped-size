import math
import gzip
import sublime, sublime_plugin

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

class GZippedFileSize(sublime_plugin.EventListener):
	def update(self, view):
		r = sublime.Region(0, view.size())
		text = bytes(view.substr(r), 'utf-8')
		bytes_len = len(gzip.compress(text))
		fmt_len = sizeof_fmt(bytes_len)
		view.erase_status("gzippedSize")
		view.set_status("gzippedSize", "GZip %s" % fmt_len)

	on_post_save_async = update
	on_modified_async = update
	on_activated_async = update