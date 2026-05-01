const {
  toCamelCase,
  toPascalCase,
  toSnakeCase,
  toKebabCase,
  toConstantCase,
  toTrainCase,
  toSentenceCase,
  toTitleCase,
  convertCase,
  detectCase,
  CASE_TYPES
} = require('../index');

describe('toCamelCase', () => {
  test('converts simple string', () => {
    expect(toCamelCase('hello world')).toBe('helloWorld');
  });

  test('converts string with multiple spaces', () => {
    expect(toCamelCase('hello  world')).toBe('helloWorld');
  });

  test('converts string with punctuation', () => {
    expect(toCamelCase('hello, world!')).toBe('helloWorld');
  });

  test('handles empty string', () => {
    expect(toCamelCase('')).toBe('');
  });
});

describe('toPascalCase', () => {
  test('converts simple string', () => {
    expect(toPascalCase('hello world')).toBe('HelloWorld');
  });

  test('converts string with multiple spaces', () => {
    expect(toPascalCase('hello  world')).toBe('HelloWorld');
  });

  test('handles empty string', () => {
    expect(toPascalCase('')).toBe('');
  });
});

describe('toSnakeCase', () => {
  test('converts simple string', () => {
    expect(toSnakeCase('hello world')).toBe('hello_world');
  });

  test('converts string with multiple spaces', () => {
    expect(toSnakeCase('hello  world')).toBe('hello_world');
  });

  test('converts string with punctuation', () => {
    expect(toSnakeCase('hello, world!')).toBe('hello_world');
  });

  test('handles empty string', () => {
    expect(toSnakeCase('')).toBe('');
  });
});

describe('toKebabCase', () => {
  test('converts simple string', () => {
    expect(toKebabCase('hello world')).toBe('hello-world');
  });

  test('converts string with multiple spaces', () => {
    expect(toKebabCase('hello  world')).toBe('hello-world');
  });

  test('converts string with punctuation', () => {
    expect(toKebabCase('hello, world!')).toBe('hello-world');
  });

  test('handles empty string', () => {
    expect(toKebabCase('')).toBe('');
  });
});

describe('toConstantCase', () => {
  test('converts simple string', () => {
    expect(toConstantCase('hello world')).toBe('HELLO_WORLD');
  });

  test('converts string with multiple spaces', () => {
    expect(toConstantCase('hello  world')).toBe('HELLO_WORLD');
  });

  test('converts string with punctuation', () => {
    expect(toConstantCase('hello, world!')).toBe('HELLO_WORLD');
  });

  test('handles empty string', () => {
    expect(toConstantCase('')).toBe('');
  });
});

describe('toTrainCase', () => {
  test('converts simple string', () => {
    expect(toTrainCase('hello world')).toBe('Hello-World');
  });

  test('converts string with multiple spaces', () => {
    expect(toTrainCase('hello  world')).toBe('Hello-World');
  });

  test('converts string with punctuation', () => {
    expect(toTrainCase('hello, world!')).toBe('Hello-World');
  });

  test('handles empty string', () => {
    expect(toTrainCase('')).toBe('');
  });
});

describe('toSentenceCase', () => {
  test('converts simple string', () => {
    expect(toSentenceCase('hello world')).toBe('Hello world');
  });

  test('converts string with multiple spaces', () => {
    expect(toSentenceCase('hello  world')).toBe('Hello world');
  });

  test('converts string with punctuation', () => {
    expect(toSentenceCase('hello, world!')).toBe('Hello, world!');
  });

  test('handles empty string', () => {
    expect(toSentenceCase('')).toBe('');
  });
});

describe('toTitleCase', () => {
  test('converts simple string', () => {
    expect(toTitleCase('hello world')).toBe('Hello World');
  });

  test('converts string with multiple spaces', () => {
    expect(toTitleCase('hello  world')).toBe('Hello World');
  });

  test('converts string with punctuation', () => {
    expect(toTitleCase('hello, world!')).toBe('Hello, World!');
  });

  test('handles empty string', () => {
    expect(toTitleCase('')).toBe('');
  });
});

describe('convertCase', () => {
  test('converts from camel to snake', () => {
    expect(convertCase('helloWorld', CASE_TYPES.CAMEL, CASE_TYPES.SNAKE)).toBe('hello_world');
  });

  test('converts from snake to camel', () => {
    expect(convertCase('hello_world', CASE_TYPES.SNAKE, CASE_TYPES.CAMEL)).toBe('helloWorld');
  });

  test('converts from kebab to pascal', () => {
    expect(convertCase('hello-world', CASE_TYPES.KEBAB, CASE_TYPES.PASCAL)).toBe('HelloWorld');
  });

  test('converts from constant to train', () => {
    expect(convertCase('HELLO_WORLD', CASE_TYPES.CONSTANT, CASE_TYPES.TRAIN)).toBe('Hello-World');
  });

  test('returns same string if from and to are same', () => {
    expect(convertCase('helloWorld', CASE_TYPES.CAMEL, CASE_TYPES.CAMEL)).toBe('helloWorld');
  });

  test('handles empty string', () => {
    expect(convertCase('', CASE_TYPES.CAMEL, CASE_TYPES.SNAKE)).toBe('');
  });
});

describe('detectCase', () => {
  test('detects camelCase', () => {
    expect(detectCase('helloWorld')).toBe(CASE_TYPES.CAMEL);
  });

  test('detects PascalCase', () => {
    expect(detectCase('HelloWorld')).toBe(CASE_TYPES.PASCAL);
  });

  test('detects snake_case', () => {
    expect(detectCase('hello_world')).toBe(CASE_TYPES.SNAKE);
  });

  test('detects kebab-case', () => {
    expect(detectCase('hello-world')).toBe(CASE_TYPES.KEBAB);
  });

  test('detects CONSTANT_CASE', () => {
    expect(detectCase('HELLO_WORLD')).toBe(CASE_TYPES.CONSTANT);
  });

  test('detects Train-Case', () => {
    expect(detectCase('Hello-World')).toBe(CASE_TYPES.TRAIN);
  });

  test('detects sentence case', () => {
    expect(detectCase('Hello world')).toBe(CASE_TYPES.SENTENCE);
  });

  test('detects Title Case', () => {
    expect(detectCase('Hello World')).toBe(CASE_TYPES.TITLE);
  });

  test('returns unknown for random string', () => {
    expect(detectCase('hello!@#$world')).toBe('unknown');
  });

  test('handles empty string', () => {
    expect(detectCase('')).toBe('');
  });
});