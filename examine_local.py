import dbelib

gd = dbelib.GetDocker()

for image in gd.local_tagged_images():
    packages = []
    good_packages = []
    bad_packages = []
    history = gd.image_history(image)
    for step in history:
        packages.extend(dbelib.Parser.package_names_from_history(step))
    for package in packages:
        if package is None:
            pass
        elif dbelib.Parser.package_is_pinned(package):
            good_packages.append(package)
        else:
            bad_packages.append(package)
    image_header = "------------------------\n%s\n" % image
    good = " ".join(good_packages)
    bad = " ".join(bad_packages)
    p_status = dbelib.OutFormatter.format_package_results(good, bad)
    print(image_header + p_status)
