# JSON File Standards Framework

Use this guide whenever you create or modify JSON files for the project. Apply these rules unless a specific JSON schema explicitly overrides them.

## Structure and Formatting

- Indent nested structures with exactly two spaces; do not use tabs or four-space indentation.
- Example:

  Non-compliant:

  ```json
  {
      "object": {
          "sub-object": "This is a description for the sub-object."
      }
  }
  ```

  Compliant:

  ```json
  {
    "object": {
      "sub-object": "This is a description for the sub-object."
    }
  }
  ```

## Field Naming and Character Rules

- The term *field* refers to a JSON property name (object key).
- Keys for objects or arrays must be lowercase `snake_case`. Replace spaces with underscores.
- Keys for primitive values (strings, numbers, booleans) may contain spaces or uppercase letters only when that formatting is part of the canonical label and no further nesting occurs. Prefer `snake_case` when possible.
- Allowed characters for keys are `a`–`z`, `0`–`9`, `_`, and `-`. Apostrophes and other punctuation are not permitted directly in keys. When a canonical label requires them, encode the character using a Unicode escape (for example, use `\u0027` for an apostrophe).
- String values should use characters that are easy to type on a standard US keyboard. Replace typographic punctuation with its ASCII equivalent (for example, prefer `'` instead of `’`). Use Unicode escapes only when a required character cannot be typed directly.
- Example:

  ```json
  {
    "locations": {
      "Michigan City": {
        "state": "Indiana, US"
      }
    }
  }
  ```

  Should be rewritten as:

  ```json
  {
    "locations": {
      "michigan_city": {
        "state": "Indiana, US"
      }
    }
  }
  ```

- Example of handling apostrophes in keys:

  ```json
  {
    "characters": {
      "Zai'kir": {
        "title": "Blade of the Dawn"
      }
    }
  }
  ```

  Should be rewritten as:

  ```json
  {
    "characters": {
      "Zai\u0027kir": {
        "title": "Blade of the Dawn"
      }
    }
  }
  ```

- Example of replacing smart punctuation in values:

  ```json
  {
    "flavor_text": "The blade’s edge gleams."
  }
  ```

  Should be rewritten as:

  ```json
  {
    "flavor_text": "The blade's edge gleams."
  }
  ```
