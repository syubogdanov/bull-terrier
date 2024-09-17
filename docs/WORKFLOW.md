# Bull-Terrier - Workflow

## Table of Contents

* **[1. Definitions](#definitions)**
  * [1.1. Task](#task)
  * [1.2. Job](#job)
  * [1.3. Workflow](#workflow)

* **[2. Tasks](#tasks)**
  * [2.1. Bitbucket](#bitbucket)
  * [2.2. File System](#file-system)
  * [2.3. GitHub](#github)
  * [2.4. GitLab](#gitlab)
  * [2.5. HTTP](#http)

* **[3. Attributes](#attributes)**
  * [3.1. branch](#branch)
  * [3.2. commit](#commit)
  * [3.3. host](#host)
  * [3.4. jobs](#jobs)
  * [3.5. mime](#mime)
  * [3.6. name](#name)
  * [3.7. path](#path)
  * [3.8. repo](#repo)
  * [3.9. tag](#tag)
  * [3.10. tasks](#tasks)
  * [3.11. url](#url)
  * [3.12. user](#user)

## Definitions

### Task

**Task** is an abstract definition of a file (in terms of `UNIX`). This can be a regular file, a
directory, or, for example, some web resource.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Sergei Bogdanov
          host: GitHub
          user: syubogdanov
          repo: bull-terrier
        # -> -> -> -> -> -> -> ->

        - ...
```

### Job

**Job** is a collection of uniquely named *tasks*.

```yaml
---
jobs:
    - ...

    # -> -> -> -> -> -> -> ->
    - name: Fight Club
      tasks:
        - ...
        - ...
        - ...
    # -> -> -> -> -> -> -> ->

    - ...
```

### Workflow

**Workflow** is a collection of uniquely named *jobs*.

```yaml
---
# -> -> -> -> -> -> -> ->
jobs:
    - ...
    - ...
    - ...
# -> -> -> -> -> -> -> ->
```

## Tasks

### Bitbucket

To use a repository hosted on [Bitbucket](https://bitbucket.org/), use the following rule.

If [`branch`](#branch), [`commit`](#commit) or [`tag`](#tag) is not specified, then the repository's
default branch is used.

Structure:

* [`name`](#name) : *string* : *required*;
* [`host`](#host) : *literal-string {`Bitbucket`}* : *required*;
* [`user`](#user) : *string* : *required*;
* [`repo`](#repo) : *string* : *required*;
* [`branch`](#branch) : [*refname*](DTYPES.md#refname) : *optional*;
* [`commit`](#commit) : [*sha1*](DTYPES.md#sha1) : *optional*;
* [`tag`](#tag) : [*refname*](DTYPES.md#refname) : *optional*.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Kirk Hammett
          host: Bitbucket
          user: metallica
          repo: master-of-puppets
        # -> -> -> -> -> -> -> ->

        - ...
```

### File System

To use a regular file or a directory, use the following rule.

Note that:

* If [`path`](#path) is a symlink, then it is followed;

* If [`path`](#path) is a directory, then its junctions, mounts and symlinks will be ignored. The
  rule is also true for symlinks pointing to directories.

Structure:

* [`name`](#name) : *string* : *required*;
* [`path`](#path) : [*path*](DTYPES.md#path) : *required*.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Taylor Swift
          path: C:/Users/TS/Midnights/Anti-Hero.txt
        # -> -> -> -> -> -> -> ->

        - ...
```

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Lana Del Rey
          path: ~/Desktop/Honeymoon/
        # -> -> -> -> -> -> -> ->

        - ...
```

### GitHub

To use a repository hosted on [GitHub](https://github.com/), use the following rule.

If [`branch`](#branch), [`commit`](#commit) or [`tag`](#tag) is not specified, then the repository's
default branch is used.

Structure:

* [`name`](#name) : *string* : *required*;
* [`host`](#host) : *literal-string {`GitHub`}* : *required*;
* [`user`](#user) : *string* : *required*;
* [`repo`](#repo) : *string* : *required*;
* [`branch`](#branch) : [*refname*](DTYPES.md#refname) : *optional*;
* [`commit`](#commit) : [*sha1*](DTYPES.md#sha1) : *optional*;
* [`tag`](#tag) : [*refname*](DTYPES.md#refname) : *optional*.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Eminem
          host: GitHub
          user: shady-records
          repo: slim-shady
        # -> -> -> -> -> -> -> ->

        - ...
```

### GitLab

To use a repository hosted on [GitLab](https://gitlab.com/), use the following rule.

If [`branch`](#branch), [`commit`](#commit) or [`tag`](#tag) is not specified, then the project's
default branch is used.

Structure:

* [`name`](#name) : *string* : *required*;
* [`host`](#host) : *literal-string {`GitLab`}* : *required*;
* [`user`](#user) : *string* : *required*;
* [`repo`](#repo) : *string* : *required*;
* [`branch`](#branch) : [*refname*](DTYPES.md#refname) : *optional*;
* [`commit`](#commit) : [*sha1*](DTYPES.md#sha1) : *optional*;
* [`tag`](#tag) : [*refname*](DTYPES.md#refname) : *optional*.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Donatello
          host: GitLab
          user: ninja-turtles
          repo: purple-mask
        # -> -> -> -> -> -> -> ->

        - ...
```

### HTTP

To use a web resource that is accessible over `HTTP` or `HTTPS`, use the following rule.

If [`mime`](#mime) is not specified, then the downloaded file is interpreted first as an archive,
and if it cannot be decompressed in any known way, then as text. It is strongly recommended to
specify [`mime`](#mime).

Structure:

* [`name`](#name) : *string* : *required*;
* [`url`](#url) : [*http-url*](DTYPES.md#http-url) : *required*;
* [`mime`](#mime) : [*mime*](DTYPES.md#mime) : *optional*.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Wovlerine
          url: https://x-men.marvel/logan.rar
          mime: application/x-rar-compressed
        # -> -> -> -> -> -> -> ->

        - ...
```

## Attributes

### `branch`

Specifies the [branch](https://git-scm.com/docs/git-branch) to be used.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: James Hetfield
          host: GitHub
          user: metallica
          repo: enter-sandman
          # -> -> -> -> -> -> -> ->
          branch: remastered-2021
          # -> -> -> -> -> -> -> ->

        - ...
```

### `commit`

Specifies the [commit](https://git-scm.com/docs/git-commit) to be used.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Ryan Gosling
          host: GitLab
          user: ryan-gosling
          repo: la-la-land
          # -> -> -> -> -> -> -> ->
          commit: dea4ea046a6778c845edc4b6a916bc9f7699b82c
          # -> -> -> -> -> -> -> ->

        - ...
```

### `host`

Specifies the name of the source-code-hosting platform to be used.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Hugh Jackman
          # -> -> -> -> -> -> -> ->
          host: Bitbucket
          # -> -> -> -> -> -> -> ->
          user: marvel
          repo: wolverine

        - ...
```

### `jobs`

Specifies the list of [*jobs*](#job).

```yaml
---
# -> -> -> -> -> -> -> ->
jobs:
    - ...
    - ...
    - ...
# -> -> -> -> -> -> -> ->
```

### `mime`

Specifies the [MIME](https://en.wikipedia.org/wiki/MIME).

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Laura Kinney
          url: https://x-men.marvel/x-23.tar.gz
          # -> -> -> -> -> -> -> ->
          mime: application/x-tar
          # -> -> -> -> -> -> -> ->

        - ...
```

### `name`

Specifies the name of a [job](#job) or a [task](#task).

```yaml
---
jobs:
      # -> -> -> -> -> -> -> ->
    - name: F-R-I-E-N-D-S
      # -> -> -> -> -> -> -> ->
      tasks:
        - ...
```

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

          # -> -> -> -> -> -> -> ->
        - name: Sheldon Lee Cooper
          # -> -> -> -> -> -> -> ->
          path: /home/big-bang-theory/

        - ...
```

### `path`

Specifies the path in the file system.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Wade Wilson
          # -> -> -> -> -> -> -> ->
          path: ~/hello/deadpool/
          # -> -> -> -> -> -> -> ->

        - ...
```

### `repo`

Specifies the repository ([Bitbucket](https://bitbucket.org/), [GitHub](https://github.com/)) or
project ([GitLab](https://gitlab.com/)).

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Bill Gates
          host: GitHub
          user: microsoft
          # -> -> -> -> -> -> -> ->
          repo: vscode
          # -> -> -> -> -> -> -> ->

        - ...
```

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Bugs Bunny
          host: GitLab
          user: looney-tunes
          # -> -> -> -> -> -> -> ->
          repo: merrie-melodies
          # -> -> -> -> -> -> -> ->

        - ...
```

### `tag`

Specifies the [tag](https://git-scm.com/docs/git-tag) to be used.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Albert Einstein
          host: Bitbucket
          user: genius
          repo: physics
          # -> -> -> -> -> -> -> ->
          tag: theory-of-relativity
          # -> -> -> -> -> -> -> ->

        - ...
```

### `tasks`

Specifies the list of [*tasks*](#task).

```yaml
---
jobs:
    - ...

    - name: How I Met Your Mother
      # -> -> -> -> -> -> -> ->
      tasks:
      # -> -> -> -> -> -> -> ->
        - ...
        - ...
        - ...

    - ...
```

### `url`

Specifies the URL to be used.

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Andy Dufrain
          # -> -> -> -> -> -> -> ->
          url: https://shawshank.gov/
          # -> -> -> -> -> -> -> ->

        - ...
```

### `user`

Specifies the username ([GitLab](https://gitlab.com/), [GitHub](https://github.com/)) or
workspace ([Bitbucket](https://bitbucket.org/)).

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Darth Vader
          host: GitHub
          # -> -> -> -> -> -> -> ->
          user: anakin-skywalker
          # -> -> -> -> -> -> -> ->
          repo: sith

        - ...
```

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: Indiana Jones
          host: Bitbucket
          # -> -> -> -> -> -> -> ->
          user: henry-jones
          # -> -> -> -> -> -> -> ->
          repo: crystal-skull

        - ...
```
