# Bull-Terrier - Data Types

## Table of Contents

* **[1. Data Types](#data-types)**
  * [1.1. http-url](#http-url)
  * [1.2. mime](#mime)
  * [1.3. path](#path)
  * [1.4. refname](#refname)
  * [1.5. sha1](#sha1)

## Data Types

### `http-url`

**Type**: `string`

**Description**: Represents a URL with an `HTTP` or `HTTPS` scheme.

**Constraints**:

* TLD is not required;
* Host is required;
* Maximum length: `2083`.

### `mime`

**Type**: `literal-string`

...

### `path`

**Type**: `string`

**Description**: Represents a file system path.

**Constraints**:

* Normalization is not required;
* Relative paths are allowed;
* Home directories are expanded.

### `refname`

**Type**: `string`

**Description**: Represents a `git` reference name.

**Constraints**:

* See the [documentation](https://git-scm.com/docs/git-check-ref-format).

### `sha1`

**Type**: `string`

...
