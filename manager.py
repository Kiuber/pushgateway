from echobox.tool import file
from echobox.tool import functocli
from echobox.app.devops import DevOpsApp

APP_NAME = 'prom-pushgateway-ttl'


class App(DevOpsApp):

    def __init__(self):
        DevOpsApp.__init__(self, APP_NAME)

    def merge_upstream_code(self, tag):
        remote_name = 'upstream'
        self.shell_run(f'git remote add {remote_name} git@github.com:prometheus/pushgateway.git', exit_on_error=False)
        self.shell_run(f'git fetch {remote_name}')
        self.shell_run(f'git merge {tag}')

    def build_image(self, version=None, platform='linux/amd64', push=False):
        version = file.file_get_contents(f'{self.root_dir}/VERSION').strip() if not version else version

        image_tag = f'{version}-ttl'
        image_name = f'kiuber/{self.app_name}'
        image = f'{image_name}:{image_tag}'
        self.shell_run(f'PREFIX=./.build/{platform.replace("/", "-")} make build')

        env = f'DOCKER_ARCHS=amd64 DOCKER_IMAGE_NAME={image_name} SANITIZED_DOCKER_IMAGE_TAG="" DOCKER_IMAGE_TAG={image_tag}'
        self.shell_run(f'{env} make common-docker')

        if push:
            self.shell_run(f'{env} make common-docker-publish')


if __name__ == '__main__':
    functocli.run_app(App)
