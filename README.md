<!--
Avoid using this README file for information that is maintained or published elsewhere, e.g.:

* metadata.yaml > published on Charmhub
* documentation > published on (or linked to from) Charmhub
* detailed contribution guide > documentation or CONTRIBUTING.md

Use links instead.
-->

# tor-obfs4-bridge-k8s

Charmhub package name: tor-obfs4-bridge-k8s
More information: https://charmhub.io/tor-obfs4-bridge-k8s

This charm is an experiment, in which I am aiming at created a better UX than
the [terraform approach](https://github.com/sed-i/tf-gcp/tree/main/tor-obfs4-bridge).


## Workload lifecycle
- Startup
- Evaluation
- Receiving traffic ('production')

## Resource revisions

| Resource revision | OCI image                         |
|-------------------|-----------------------------------|
| bridge:1          | `thetorproject/obfs4-bridge:0.14` |
