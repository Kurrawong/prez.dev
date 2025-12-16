---
title: Deployment
#description: The API for Prez
---

## Running

This section is for developing Prez locally. See the [Running](#running) options below for running Prez in production.

To run the development server (with auto-reload on code changes):

```bash
poetry run python main.py
```

### Running in a Container

Prez container images are built using a GitHub Action and are available [here](https://github.com/RDFLib/prez/pkgs/container/prez).

The Dockerfile in the repository can also be used to build a Docker image.

#### Image variants

The image name is `ghcr.io/rdflib/prez`.

The `latest` tag points to the latest stable release of Prez. All latest stable releases have a `major`, `major.minor`, and `major.minor.patch` tag pointing to it.

For example, for a release with a git tag of 3.2.4, the following tags will be on the container image:

- `3`
- `3.2`
- `3.2.4`
- `latest`

The full version is automatically created/incremented using the [Semantic Release GitHub Action](https://github.com/cycjimmy/semantic-release-action), which automatically increments the version based on commits to the `main`
branch.