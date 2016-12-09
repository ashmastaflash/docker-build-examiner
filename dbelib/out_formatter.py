from string import Template


class OutFormatter(object):
    @classmethod
    def format_package_results(cls, good, bad):
        tmpl = Template("\tPinned: $good\n\tUnpinned: $bad")
        return tmpl.safe_substitute({"good": good, "bad": bad})
