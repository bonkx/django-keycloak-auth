# django-keycloak-auth
Django Keycloak Auth with OpenID Connect

### Using mozilla-django-oidc
```
pip install mozilla-django-oidc
```

### Using django-login-required-middleware for all web routes
```
pip install django-login-required-middleware
```

### [Github Action as a service](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/configuring-the-self-hosted-runner-application-as-a-service)


### Github Runners

Download

```sh
# Create a folder
$ mkdir actions-runner && cd actions-runner   
# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
# Optional: Validate the hash
$ echo "29fc8cf2dab4c195bb147384e7e2c94cfd4d4022c793b346a6175435265aa278  actions-runner-linux-x64-2.311.0.tar.gz" | shasum -a 256 -c
# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz
```

Configure

```sh
# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/nawastra/django-keycloak-auth --token AF4RTIPFXI5E4BD4DHIMDXDFQ2UZG
# Last step, run it!
$ ./run.sh
```

Using your self-hosted runner

```sh
# Use this YAML in your workflow file for each job
runs-on: self-hosted
```
