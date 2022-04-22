# WelcomeToMars

## Workflow for this repo
- create branch with commit
- update readme with commit
- complete task with commit
- update readme with commit
- pull request for branch with branch notes


## Useful links

- https://www.gurock.com/testrail/docs/api/getting-started/binding-python/
- https://docs.gitlab.com/ee/ci/test_cases/
- https://www.gurock.com/testrail/github-test-management
- https://blog.gurock.com/test-version-control/
- https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks


### Json, Yaml
- https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/
- https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/


## Improves:

### Git

- buy gitlab for qa or develop hooks for bitbacket(more pain!)
- configure gitlab for users groups
- trigger jenkins with bitbucket webhook > jenkins get diff from bitbacket after triggered


### Testrail

- research testrail version system https://blog.gurock.com/test-version-control/
- write docs for testrail lib
- sync comments for cases_methods with testrail api doc
- Support the ID of the parent section (to build section hierarchies)
- support adding attach files for cases


### Tech

- cache system improvements
- post cases with hook(firstly collect dirs for sections/suites, secondly cases) relative to last cases commit



### Test design

- Create test cases extension for code redactor(vs studio code)


## In progress

### Git

- migrate to gitlab
- implement gitlab server hooks
- create test-design branch with dev branch
- Git bot(client) for test rail
- link git branch to task in jira
- last branch label in case
- configure Gitlab runners
- write scripts for runners


### Testrail

- login with api key


## Done:

### Git

- research git hooks:
  - https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
  - https://developer.atlassian.com/server/framework/atlassian-sdk/set-up-the-atlassian-plugin-sdk-and-build-a-project/
  - https://docs.gitlab.com/ee/administration/server_hooks.html
- research gitlab runners:
  - https://docs.gitlab.com/runner/
  - https://docs.gitlab.com/runner/install/windows.html
- research and create gitlab self-management server:
  - https://about.gitlab.com/install/#ubuntu,
  - https://embeddedinventor.com/complete-guide-to-setting-up-gitlab-locally-on-windows-pc/#STEP5_Download_and_install_GitLab_server


### Testrail

- research testrail api
- first testrail api implements
- manipulations with cases


### Tech

- testcase file format(yml, json)
- download all case base and save it in a test-case format
- class TMSProject
- testcase system for test design
- log system or lib
- refactor create local case base
- cache system minimal
- create dir for empty sections/suites
