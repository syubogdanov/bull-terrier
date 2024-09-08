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
  * [3.2. Adavanced Example](#advanced-example)
  * [3.3. Real-Life Example](#real-life-example)

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

**Job** is a collection of *tasks*.

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

**Workflow** is a document that declares a list of independent *jobs*, within which a *pairwise
comparison* of *tasks* must be performed. Therefore, if any *job* contains less than two *tasks*, it
will be ignored.

```yaml
# -> -> -> -> -> -> -> ->
---
jobs:
    - ...
    - ...
    - ...
# -> -> -> -> -> -> -> ->
```

## Tasks

### Bitbucket

To use a repository hosted on [Bitbucket](https://bitbucket.org/), use the following rule.

...

### File System

...

### GitHub

To use a repository hosted on [GitHub](https://github.com/), use the following rule.

...

### GitLab

To use a repository hosted on [GitLab](https://gitlab.com/), use the following rule.

...

### HTTP

...

## Examples

### Simple Example

The following example demonstrates how to define the *workflow* document so that Bull-Terrier
compares the contents of the `/home/linux/` directory with the contents of the `cpython` repository.

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

### Advanced Example

The following example demonstrates how to define the *workflow* document so that Bull-Terrier
performs two independent checks - separately `DC` and separately `Marvel`.

```yaml
---
jobs:
    - name: DC
      tasks:
        - name: Batman
          host: Bitbucket
          user: bruce-wayne
          repo: arkham
          branch: dark-knight

        - name: Joker
          url: https://joker.dc/earth-23
          mime: application/gzip

        - name: Two-Face
          host: GitLab
          user: harvey-dent
          repo: coin
          tag: tail

    - name: Marvel
      tasks:
        - name: Spider-Man
          url: https://spider.man/no-way-home
          mime: text/plain

        - name: Green Goblin
          path: ~/films/../games/lego
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

...

### commit

...

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

...

### tag

...

### tasks

...

### url

...

### user

...
