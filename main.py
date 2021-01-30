import os
import subprocess


settings_dir = "~/.m2/"
settings_file = f'{settings_dir}/settings.xml'
settings_contents = f"""
<settings>
    <servers>
        <server>
            <id>github</id>
            <username>x-access-token</username>
            <password>{os.environ["GITHUB_PASSWORD"]}</password>
        </server>
    </servers>
</settings>
"""


def main():
    repo_name = os.environ["INPUT_REPO_NAME"]
    if '/' != repo_name[0]:
        repo_name = '/' + repo_name
    deploy_cmd = 'mvnw -e -B deploy -DaltDeploymentRepository=' \
        + f'github::default::https://maven.pkg.github.com{repo_name}'
    if not os.path.exists(settings_dir):
        os.makedirs(settings_dir)
    with open(settings_file, 'w') as inimage:
        inimage.write(settings_contents)
    subprocess.run(deploy_cmd.split())


if __name__ == "__main__":
    main()
