#!/bin/sh
# Fails when a tracked file carries the acceptance failure marker. The bracket keeps
# this script from matching itself.
set -eu
if git grep -n -e 'handler-acceptance: [f]ail' -- .; then
  echo "acceptance failure marker present" >&2
  exit 1
fi
echo "no acceptance failure marker"
