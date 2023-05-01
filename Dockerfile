FROM 077700697743.dkr.ecr.us-east-1.amazonaws.com/release-engineering/python-poetry:v1.1.0

# Development image, starting from python:3.8+poetry

# Workaround critical-level CVE in libexpat1 by upgrading the packages
# Which forces just security update (no feature-full updates)
# See https://fanduel.atlassian.net/browse/REE-1050
RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*


# "Workdir" folder is what's used by buildkite's docker plugin
COPY . /workdir
WORKDIR /workdir

RUN poetry install