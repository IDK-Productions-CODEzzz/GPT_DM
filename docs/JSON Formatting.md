# JSON File Standards Framework

Use this document as a starting point for defining JSON file standards for the project. Add or modify sections as needed.

## Structure and Formatting

- Indentation: 2 spaces for each nested item.

## Field Conventions

- Element Name: The name of any element should not contain spaces. Underscores should be used instead. Spaces are only allowed in the lowest level value fields.
  - Example: `"Critical_Success": "Nat 10 = hit + extra effect."`

- Non-Alphanumerics: All non-alphanumeric characters must use UTC encoding. The exceptions are the underscore "_" and the hyphen "-".
  - Example: `"Zai\u2019kir":`
