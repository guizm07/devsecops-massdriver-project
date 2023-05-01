import yaml
import git

class YamlTagUpdater:
    def __init__(self, git_repos, yaml_path, key, new_value):
        self.git_repos = git_repos
        self.yaml_path = yaml_path
        self.key = key
        self.new_value = new_value

    def update_yaml(self):
        for repo in self.git_repos:
            git.Repo.clone_from(repo, 'temp_repo')
            with open('temp_repo/' + self.yaml_path) as file:
                yaml_data = yaml.safe_load(file)
            yaml_data[self.key] = self.new_value
            with open('temp_repo/' + self.yaml_path, 'w') as file:
                yaml.dump(yaml_data, file)
            repo = git.Repo('temp_repo')
            repo.git.add(update=True)
            repo.git.commit(m="updated yaml tag")
            origin = repo.remote(name='origin')
            origin.push()
