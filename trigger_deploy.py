#!/usr/bin/env python

"""Simple program to forward requests to an autodeploy"""


import os
import sys

import requests


def main():
    """Triggers update request"""

    api = os.environ.get("DEPLOY_API_KEY")
    deploy_url = os.environ.get("DEPLOY_HOST_URL")
    repository = os.environ.get("GIT_REPO")
    branch = os.environ.get("GIT_BRANCH")
    sha1 = os.environ.get("GIT_SHA")        
    actor = os.environ.get("GIT_ACTOR")
    owner = os.environ.get("GIT_OWNER")    

    if api is None or deploy_url is None or repository is None:
        print("X", api)
        print("X", deploy_url)
        print("X", repository)
        print("Environment not set - no request")
        return

    tdata = {
        "api_key": api,
        "repository": repository,
        "branch": branch,
        "actor": actor,
        "sha1": sha1
    }
    ret = requests.post(deploy_url + "/update", json=tdata)
    print(ret.text)


if __name__ == "__main__":
    main()

