import docker


class GetDocker(object):
    def __init__(self):
        self.client = docker.from_env()

    def local_tagged_images(self):
        """Returns a list of all tagged local images"""
        retval = []
        for image in self.client.images():
            if image["RepoTags"] is None:
                continue
            elif "<none>:<none>" in image["RepoTags"]:
                continue
            else:
                for repo_tag in image["RepoTags"]:
                    retval.append(repo_tag)
        return retval

    def image_history(self, image_tag):
        """Returns a list of steps comprising repo history"""
        return self.client.history(image_tag)
