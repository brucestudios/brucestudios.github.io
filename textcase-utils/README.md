# TextCase Utils

A lightweight, zero-dependency JavaScript utility for converting text between different cases (camelCase, snake_case, kebab-case, PascalCase, etc.).

## Features

- Convert between 8 common case formats:
  - camelCase
  - PascalCase
  - snake_case
  - kebab-case
  - CONSTANT_CASE
  - Train-Case
  - Sentence case
  - Title Case
- Detect the case of a given string
- Zero dependencies
- Works in both Node.js and browser environments
- Fully tested with Jest
- Linted with ESLint

## Installation

```bash
npm install textcase-utils
```

## Usage

### Node.js

```javascript
const {
  toCamelCase,
  toSnakeCase,
  convertCase,
  detectCase
} = require('textcase-utils');

toCamelCase('hello world'); // 'helloWorld'
toSnakeCase('helloWorld'); // 'hello_world'
convertCase('hello-world', 'kebab', 'camel'); // 'helloWorld'
detectCase('helloWorld'); // 'camel'
```

### Browser

```html
<script src="path/to/textcase-utils.js"></script>
<script>
  console.log(textCaseUtils.toCamelCase('hello world')); // 'helloWorld'
</script>
```

Or if using a module bundler:

```javascript
import { toCamelCase } from 'textcase-utils';
```

## API

### Conversion Functions

All conversion functions take a string and return a string.

- `toCamelCase(str)`
- `toPascalCase(str)`
- `toSnakeCase(str)`
- `toKebabCase(str)`
- `toConstantCase(str)`
- `toTrainCase(str)`
- `toSentenceCase(str)`
- `toTitleCase(str)`

### General Conversion

```javascript
convertCase(text, fromCase, toCase)
```

Where `fromCase` and `toCase` are one of:
- 'camel'
- 'pascal'
- 'snake'
- 'kebab'
- 'constant'
- 'train'
- 'sentence'
- 'title'

### Case Detection

```javascript
detectCase(str)
```

Returns one of the case types above or 'unknown'.

## License

MIT

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Running Tests

```bash
npm test
```

## Linting

```bash
npm run lint
```