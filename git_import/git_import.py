from typing import Dict
from git import Repo
import subprocess
import os


class GitArgsNotAcceptableException(Exception):
    pass


class FromGitImport(object):

    def __init__(self, ssh_repo_path: str, **kwargs: Dict[str, str]) -> None:

        # Initiate Properties.
        repo_name: str = os.path.basename(ssh_repo_path).split(".")[0]
        full_dir_path: str = os.path.join(kwargs.get("save_path"), repo_name)
        git_hash = kwargs.get("use_commit") if kwargs.get("use_commit") else None
        branch: str = "master" if kwargs.get("use_branch") is None else kwargs.get("use_branch")

        # Select clone method.
        if not os.path.isdir(full_dir_path):
            if kwargs.get("ssh_key_path"):
                ssh_key_path = {"GIT_SSH_COMMAND": "ssh -i " + kwargs.get("ssh_key_path")}
                Repo.clone_from(ssh_repo_path, full_dir_path, env=ssh_key_path)
            else:
                Repo.clone_from(ssh_repo_path, full_dir_path)

        # Apply rules.
        if "use_branch" in kwargs:
            subprocess.run("""
                            cd {save_path}; git checkout -b {branch}; git pull origin {branch}
                           """.format(save_path=kwargs.get("save_path"),
                                      branch=branch),
                           shell=True)

        if "always_sync" in kwargs and "use_commit" in kwargs:
            raise GitArgsNotAcceptableException("`always_sync` & `use_commit` Cannot be assigned "
                                                "together.")

        if "use_commit" in kwargs:
            subprocess.run("cd " + full_dir_path + "; git checkout " + git_hash, shell=True)

        if "always_sync" in kwargs:
            subprocess.run("cd " + kwargs.get("save_path") + "; git pull origin {}".format(branch))

