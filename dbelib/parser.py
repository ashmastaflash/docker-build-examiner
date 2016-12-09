import re


class Parser(object):
    pkg_add = re.compile(r'^.*?(apt-get\sinstall|apk\sadd|yum\sinstall)')
    pkg_extract = re.compile(r'(\s[A-Za-z0-9]{3}[A-Za-z0-9_\-=\.${}"]+)')
    pkg_reject = ["&", "apt-get", "yum", "update", "install", "apk", "add"]

    @classmethod
    def package_names_from_history(cls, history_step):
        packages = []
        created_by = history_step["CreatedBy"]
        if Parser.pkg_add.match(created_by):
            for package in Parser.pkg_extract.findall(created_by):
                if Parser.is_a_package(package):
                    packages.append(package.lstrip())
        return packages

    @classmethod
    def is_a_package(cls, pkg_name):
        for reject in Parser.pkg_reject:
            if reject in pkg_name:
                return False
        return True

    @classmethod
    def package_is_pinned(cls, package):
        if re.search(r'[^=]+[=]+[^=]+', package):
            return True
        else:
            return False
