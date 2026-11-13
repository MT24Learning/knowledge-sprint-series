# Phase 1 · Runnable code

The commands printed on the sprint images of Phase 1, Engineering Foundations (Essential Commands in Sprint 1, Try It in Sprints 2 and 3), as shell scripts you can run. The images print no output, so there is nothing to compare; a few marked lines are added so that the commands run in an empty folder.

| Sprint | File | Run with |
|---|---|---|
| 1 · Environment + Git Foundations | [`sprint01_environment_git_foundations.sh`](sprint01_environment_git_foundations.sh) | `sh sprint01_environment_git_foundations.sh` |
| 2 · Hashing + GitHub over SSH | [`sprint02_hashing_github_ssh.sh`](sprint02_hashing_github_ssh.sh) | `sh sprint02_hashing_github_ssh.sh` |
| 3 · Project Structure & Quality Gates | [`sprint03_project_structure_quality_gates.sh`](sprint03_project_structure_quality_gates.sh) | `sh sprint03_project_structure_quality_gates.sh` |

## Run it

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
. .venv/bin/activate
sh sprint01_environment_git_foundations.sh
```


## Versions

`requirements.txt` pins the tools of Sprint 3 at the versions checked.

Checked on 13 November 2026, in a fresh environment built from `requirements.txt`: each script runs to the end in an empty folder (Git 2.43, ruff 0.17.5, mypy 2.4.1, pytest 9.2.0). Sprint 2's first digest equals the SHA-256 of "abc" in NIST FIPS 180-4's examples.

## Notes

- Each script creates a new folder (`sprint01-run/` and so on) and works inside it; it stops if that folder already exists.
- Lines marked `not on the image` only create what the image's commands need (a folder, a file to commit, a Git identity, the small project of Sprint 3) or show one extra result.
- `echo -n` needs a shell whose `echo` accepts `-n` (dash, bash); elsewhere use `printf '%s' abc`.

## Licence

The code in this folder is licensed under the [MIT License](../../../LICENSE-CODE). The images and texts of the series stay under CC BY-NC-SA 4.0 ([LICENSE](../../../LICENSE)).

[← Phase 1](../README.md)
