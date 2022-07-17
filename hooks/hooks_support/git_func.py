import git

def get_remote_head(local_repo, remote_name='origin', ref_name='origin/HEAD') -> str:
    print(local_repo.remotes)
    for remote in local_repo.remotes:
        if remote.name == remote_name:
            print(remote.refs)
            for ref in remote.refs:
                if ref.name == ref_name:
                    print(ref.name, ref.commit)
                    return ref.commit


def get_diff(a_index=None, b_index=None, local_git_path='.git', mask=None, remote_name='origin', ref_name='origin/HEAD') -> dict:
    repo = git.Repo(local_git_path)
    commits_list = list(repo.iter_commits())
    local_head = repo.head.commit
    remote_head = get_remote_head(repo, remote_name, ref_name)
    print(f"remote head hash: {remote_head}")
    print(f"local head hash: {local_head}")
    # h_commit.diff()  # diff tree against index
    # h_commit.diff('HEAD~1')  # diff tree against previous tree
    # h_commit.diff(None)  # diff tree against working tree
    if a_index:
        a_commit = commits_list[a_index]
    else:
        a_commit = local_head
    if b_index:
        b_commit = commits_list[b_index]
    else:
        b_commit = remote_head
    diffs = a_commit.diff(b_commit)

    diffs_paths = {}
    for i in diffs:
        if mask and mask not in i.a_path:
            continue
        diffs_paths[i.a_path] = (i.a_path)
    return diffs_paths

# git ls-remote | grep HEAD
# git diff-tree --no-commit-id --name-only -r aeefe08caad7eb25ac3a9e2b01f165b0763b1731
# git diff --name-only
