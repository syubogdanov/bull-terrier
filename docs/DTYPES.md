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

Values:

* `...`;
* `...`;
* `...`.

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

**Description**: Represents [MIME](https://en.wikipedia.org/wiki/MIME) types.

### `path`

**Type**: `string`

**Description**: Represents a file system path.

**Constraints**:

* Normalization is not required;
* Relative paths are allowed;
* Home directories are expanded.

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
