# JSON File Standards Framework

Use this document as a starting point for defining JSON file standards for the project. Add or modify sections as needed.

## Structure and Formatting

- Indentation: 2 spaces for each nested item.
  - Examples:
    - The following JSON snippit currently indents using 4 spaces:
      ```JSON
      {
          "object": {
              "sub-object": "This is a description for the sub-object."
          }
      }
      ```
      It should be changed to the following:
      ```JSON
      {
        "object": {
          "sub-object": "This is a description for the sub-object."
        }
      }
      ```

## Field Conventions

- Allowed Characters: Refers to characters allowed in fields. All alphanumeric characters are allowed. The only non-alphanumeric characters allowed are the underscore `_`, the hyphen `-`, and the escape character `\` where the underscore is a replacement for the space in higher level fields, and the escape character is used exclusively for unicode referencing. Characters referenced by `\u` codes must be easy to type on a standard US keyboard. Spaces and capital letters are only allowed in the lowest level fields.
  - Examples:
    - `’` cannot be easily typed on a US keyboard. However, the similar character `'` can. So `'` should be used instead of `’`.
    - `Zai'kir` uses the character `'` which is not allowed. So `Zai'kir` becomes `Zai\u0027kir`.
    - The following JSON snippit uses a space and capital letters above the lowest level to define a location object:
      ```JSON
      {
        "locations": {
          "Michigan City": {
            "state": "Indiana, US"
          }
        }
      }
      ```
      For compliance, the snippit should be changed to the following:
      ```JSON
      {
        "locations": {
          "michigan_city": {
            "state": "Indiana, US"
          }
        }
      }
      ```
