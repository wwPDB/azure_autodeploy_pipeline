# azure_autodeploy_pipeline
Pipeline used to trigger deployment to test environment

## Configuring forwarding request to remote server (AZURE pipeline)

To enable triggering of the remote deployment service, two variables must be
set in the pipeline (secrets)

*  `DEPLOY_HOST_URL` the URL to invoke deployment server

*  `DEPLOY_API_KEY` a secret API known to the configuration of the deployment server

## Configure AZURE pipeline to be triggered from github

A number of variables need to be declared and set to "mm".  These are:

* git_actor
* git_branch
* git_owner
* git_repo
* git_sha

To create, goto the pipeline, press `edit` -> `variables`.  In creating variables, set the "Let users override this value when running this pipeline" option. 

## Generate a personal access token for GitHub to trigger Azure with

There needs to be a secret for github to activate Azure pipeline with.

1. While looking at the project, click on `user settings` button to the left of user icon and select "Personal access token"

2. Create a token with full privledges with an expiration date that is known.

3. Copy the key.  You will not be able to access once created

## Configure GitHub

Under the organization github account, select `settings` -> `secrets` -> `Actions`

The token `AZURE_AUTODEPLOY_TOKEN` should be available to all repositories and kept secret.


