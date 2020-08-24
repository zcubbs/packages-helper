# GitHub Shared Repo Upload Action



### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action

    - uses: geirem/packages-helper@master
      with:
        repo_name: ORGANIZATION/REPONAME
      env:
        GITHUB_PASSWORD: ${{ secrets.X_ACCESS_TOKEN }}
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `repo_name`  | Local path of the shared repo to use (organization / repo).   |
| `GITHUB_PASSWORD` _(env)_  | An access key with repo upload permissions. |

### Outputs
There are no outputs on successful execution.
