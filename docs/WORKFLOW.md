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

* **[3. Examples](#examples)**
  * [3.1. Simple Example](#simple-example)
  * [3.2. Real-Life Example](#real-life-example)

* **[4. Attributes](#attributes)**
  * [4.1. branch](#branch)
  * [4.2. commit](#commit)
  * [4.3. host](#host)
  * [4.4. jobs](#jobs)
  * [4.5. mime](#mime)
  * [4.6. name](#name)
  * [4.7. path](#path)
  * [4.8. repo](#repo)
  * [4.9. tag](#tag)
  * [4.10. tasks](#tasks)
  * [4.11. url](#url)
  * [4.12. user](#user)

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

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        # -> -> -> -> -> -> -> ->
        - name: Bryan Cranston
          path: C:/Users/dev/breaking-bad/
        # -> -> -> -> -> -> -> ->

        - ...
```

### Job

**Job** is a collection of *tasks*. All *tasks* within a *job* must have unique names.

```yaml
---
jobs:
    - ...

    # -> -> -> -> -> -> -> ->
    - name: X-Men
      tasks:
        - ...
        - ...
        - ...
    # -> -> -> -> -> -> -> ->

    - ...
```

### Workflow

**Workflow** is a collection of independent *jobs*, within which a *pairwise comparison* of *tasks*
must be performed. Therefore, if any *job* contains less than two *tasks*, it will be ignored. All
*jobs* within a *workflow* must have unique names.

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

If [branch](#branch), [commit](#commit) or [tag](#tag) is not specified, then the repository's
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

...

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

If [branch](#branch), [commit](#commit) or [tag](#tag) is not specified, then the repository's
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

If [branch](#branch), [commit](#commit) or [tag](#tag) is not specified, then the project's
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

...

Structure:

* [`name`](#name) : *string* : *required*;
* [`url`](#url) : [*url*](DTYPES.md#url) : *required*;
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

## Examples

### Simple Example

The following example demonstrates how to define the *workflow* document so that Bull-Terrier
compares the contents of the `/home/linux/` directory with the contents of the
[`cpython`](https://github.com/python/cpython) repository.

```yaml
---
jobs:
    - name: Simple Example
      tasks:
        - name: Linus Torvalds
          path: /home/linux/

        - name: Guido van Rossum
          host: GitHub
          user: python
          repo: cpython
```

### Real-Life Example

The following example demonstrates how Bull-Terrier can be used in an academic environment. Imagine
that students were asked to solve two problems in their homework. For example, to implement
functions for calculating factorials and Fibonacci numbers.

```yaml
---
jobs:
    - name: A. Factorial
      tasks:
        - name: Captain Jack Sparrow
          host: GitHub
          user: johnny-depp
          repo: factorial

        - name: Hector Barbossa
          host: GitLab
          user: geoffrey-rush
          repo: factorial

        - name: Davy Jones
          host: Bitbucket
          user: bill-nighy
          repo: factorial

    - name: B. Fibonacci
      tasks:
        - name: Captain Jack Sparrow
          host: GitHub
          user: johnny-depp
          repo: fibonacci

        - name: Hector Barbossa
          host: GitLab
          user: geoffrey-rush
          repo: fibonacci

        - name: Davy Jones
          host: Bitbucket
          user: bill-nighy
          repo: fibonacci
```

## Attributes

### branch

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

### commit

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

### host

...

### jobs

...

### mime

...

### name

...

### path

...

### repo

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

### tag

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

### tasks

...

### url

...

### user

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
