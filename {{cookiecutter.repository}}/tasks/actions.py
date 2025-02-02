"""Code to execute github actions from whichever branch you are in.
This comes in handy for developing actions yaml files.
See: https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#create-a-workflow-dispatch-event
"""

# %% IMPORTS

import json

from invoke.context import Context
from invoke.runners import Result
from invoke.tasks import task

# %% TASKS
GH_REQUEST_PREFIX = 'gh api --method POST -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28"'
WORKFLOW_PREFIX = "/repos/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/"


def get_current_branch(ctx: Context) -> str:
    branch_result: Result | None = ctx.run("git branch --show-current")
    assert branch_result, "Could not get the current branch!"
    branch: str = branch_result.stdout.strip()
    if not branch:
        raise ValueError("Could not get the current branch!")
    return branch


def get_payload_str(ctx: Context, inputs: dict[str, str]) -> str:
    branch = get_current_branch(ctx)
    out_str = f' -f "ref={branch}"'
    for k, v in inputs.items():
        out_str += f'-f "inputs[{k}]={v}"'
    return out_str


def get_workflows(ctx: Context) -> dict[str, int]:
    """Return a dict of github workflow {name: id} pairs."""
    actions_result: Result | None = ctx.run("gh workflow list --json name,id")
    assert actions_result, "Could not get workflows list!"
    actions_json = json.loads(actions_result.stdout)
    return {action["name"]: action["id"] for action in actions_json}


def run_action(ctx: Context, workflow_id: int, inputs: dict[str, str]) -> None:
    print(f"Running workflow ID: {workflow_id} w/ inputs {inputs}")
    gh_request = (
        GH_REQUEST_PREFIX
        + f" {WORKFLOW_PREFIX}{workflow_id}/dispatches"
        + get_payload_str(ctx, inputs)
    )
    ctx.run(gh_request)


@task
def run_check_action(ctx: Context, workflows_dict: dict[str, int]) -> None:
    if "check" not in workflows_dict:
        raise ValueError("Check workflow not found!")
    workflow_id = workflows_dict["check"]
    run_action(ctx, workflow_id, {})


@task
def run_test_action(ctx: Context, workflows_dict: dict[str, int]) -> None:
    if "test" not in workflows_dict:
        raise ValueError("Test workflow not found!")
    workflow_id = workflows_dict["test"]
    run_action(ctx, workflow_id, {})
