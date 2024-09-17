# Bull-Terrier - Data Types

## Table of Contents

* **[1. Data Types](#data-types)**
  * [1.1. http-url](#http-url)
  * [1.2. mime](#mime)
  * [1.3. path](#path)
  * [1.4. refname](#refname)
  * [1.5. sha-1](#sha-1)

## Data Types

### `http-url`

**Type**: `string`

**Description**: Represents a URL with an `HTTP` or `HTTPS` scheme.

**Constraints**:

* TLD is not required;
* Host is required;
* Maximum length: `2083`.

**Example**:

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: ...
          # -> -> -> -> -> -> -> ->
          url: https://example.com
          # -> -> -> -> -> -> -> ->
          mime: ...

        - ...
```

### `mime`

**Type**: `literal-string`

**Description**: Represents [MIME](https://en.wikipedia.org/wiki/MIME) types.

**Values**:

* `application/gzip`;
* `application/vnd.rar`;
* `application/x-7z-compressed`;
* `application/x-bzip`;
* `application/x-bzip2`;
* `application/x-rar-compressed`;
* `application/x-tar`;
* `application/x-zip-compressed`;
* `application/zip`;
* `text/css`;
* `text/csv`;
* `text/html`;
* `text/javascript`;
* `text/markdown`;
* `text/php`;
* `text/plain`;
* `text/rtf`;
* `text/x-asm`;
* `text/x-c`;
* `text/x-c++`;
* `text/x-csharp`;
* `text/x-go`;
* `text/x-java-source`;
* `text/x-lua`;
* `text/x-markdown`;
* `text/x-perl`;
* `text/x-python`;
* `text/x-r`;
* `text/x-rustsrc`;
* `text/x-shellscript`;
* `text/x-sql`;
* `text/x-yaml`;
* `text/xml`.

**Example**:

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: ...
          url: ...
          # -> -> -> -> -> -> -> ->
          mime: application/gzip
          # -> -> -> -> -> -> -> ->

        - ...
```

### `path`

**Type**: `string`

**Description**: Represents a file system path.

**Constraints**:

* Normalization is not required;
* Relative paths are allowed;
* Home directories are expanded.

**Example**:

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: ...
          # -> -> -> -> -> -> -> ->
          path: ~/bull/../terrier/
          # -> -> -> -> -> -> -> ->

        - ...
```

### `refname`

**Type**: `string`

**Description**: Represents a `git` reference name.

**Constraints**:

* See the [documentation](https://git-scm.com/docs/git-check-ref-format).

**Example**:

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: ...
          host: ...
          user: ...
          repo: ...
          # -> -> -> -> -> -> -> ->
          branch: python-dev
          # -> -> -> -> -> -> -> ->

        - ...
```

### `sha-1`

**Type**: `string`

**Description**: Represents a [`SHA-1`](https://en.wikipedia.org/wiki/SHA-1) hash.

**Example**:

```yaml
---
jobs:
    - name: ...
      tasks:
        - ...

        - name: ...
          host: ...
          user: ...
          repo: ...
          # -> -> -> -> -> -> -> ->
          commit: dea4ea046a6778c845edc4b6a916bc9f7699b82c
          # -> -> -> -> -> -> -> ->

        - ...
```
