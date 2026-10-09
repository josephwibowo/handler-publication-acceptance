# handler-publication-acceptance

Disposable acceptance target for Handler's GitHub publication profile
([JOS-38](https://linear.app/middesk/issue/JOS-38)). Handler's publisher App opens
chained pull requests here; the operator reviews them. Nothing here is a product.

- `main` is the integration branch. `handler/**` holds Handler-owned feature branches.
- One repository ruleset covers both: code-owner review by `@josephwibowo`, stale-approval
  dismissal, last-push approval, the `check` status from GitHub Actions, and no bypass.
- `ci/check.sh` fails when any tracked file contains the acceptance failure marker, so a
  candidate can be made to fail its required check on purpose.

Contains no secrets. Close or delete acceptance pull requests and branches freely.
