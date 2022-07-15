#!/bin/bash

image=${1:-django}
tag=${2:-latest}

# create production docker image
echo -e '\e[34m##############################\e[m'
echo -e build ${image}:${tag}
echo -e '\e[34m##############################\e[m'
docker build ./django --target=production -t ${image}:${tag}

if type dockle > /dev/null 2>&1; then
    # check security using dockle
    dockle -i CIS-DI-0005 -i CIS-DI-0006 -af settings.py ${image}:${tag}
fi