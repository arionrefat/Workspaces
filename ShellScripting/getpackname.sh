#!/bin/bash

git diff-tree --no-commit-id --name-only -r "$(git rev-parse HEAD)" | awk -F "/" '{print $2}'
