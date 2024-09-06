# Bull-Terrier - Workflow

## Table of Contents

* **[1. Definitions](#definitions)**
  * [1.1. Workflow](#workflow)
  * [1.2. Job](#job)
  * [1.3. Task](#task)

* **[2. Tasks](#tasks)**
  * [2.1. Bitbucket](#bitbucket)
  * [2.2. File System](#file-system)
  * [2.3. GitHub](#github)
  * [2.4. GitLab](#gitlab)
  * [2.5. HTTP](#http)

* **[2. Examples](#examples)**
  * [2.1. Simple Example](#simple-example)
  * [2.2. Adavanced Example](#advanced-example)

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

### Workflow

...

### Job

...

### Task

...

## Tasks

### Bitbucket

...

### File System

...

### GitHub

...

### GitLab

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

...

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
