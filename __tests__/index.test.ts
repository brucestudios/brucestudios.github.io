import {
  capitalize,
  camelCase,
  snakeCase,
  truncate,
  chunkArray,
  removeDuplicates,
  shuffle,
  groupBy,
  deepMerge,
  pick,
  omit,
  hasNestedProp,
  formatDate,
  parseDate,
  isWeekend,
  addDays,
  isValidEmail,
  isValidUrl,
  isStrongPassword,
  isAlpha,
  isNumeric,
  clamp,
  lerp,
  randomInRange,
  degToRad,
  radToDeg,
  debounce,
  throttle
} from '../src/index';

describe('String Utilities', () => {
  test('capitalize', () => {
    expect(capitalize('hello')).toBe('Hello');
    expect(capitalize('')).toBe('');
    expect(capitalize('a')).toBe('A');
  });

  test('camelCase', () => {
    expect(camelCase('hello world')).toBe('helloWorld');
    expect(camelCase('hello-world')).toBe('helloWorld');
    expect(camelCase('hello_world')).toBe('helloWorld');
  });

  test('snakeCase', () => {
    expect(snakeCase('helloWorld')).toBe('hello_world');
    expect(snakeCase('hello world')).toBe('hello_world');
    expect(snakeCase('HelloWorld')).toBe('hello_world');
  });

  test('truncate', () => {
    expect(truncate('hello world', 5)).toBe('he...');
    expect(truncate('hi', 5)).toBe('hi');
    expect(truncate('hello world', 5, '')).toBe('hello');
  });
});

describe('Array Utilities', () => {
  test('chunkArray', () => {
    expect(chunkArray([1,2,3,4,5], 2)).toEqual([[1,2],[3,4],[5]]);
    expect(chunkArray([], 2)).toEqual([]);
    expect(chunkArray([1,2,3], 0)).toEqual([]);
  });

  test('removeDuplicates', () => {
    expect(removeDuplicates([1,2,2,3,1])).toEqual([1,2,3]);
    expect(removeDuplicates(['a','b','a'])).toEqual(['a','b']);
  });

  test('shuffle', () => {
    const arr = [1,2,3,4,5];
    const shuffled = shuffle(arr);
    expect(shuffled).toHaveLength(5);
    expect(shuffled).toEqual(expect.arrayContaining([1,2,3,4,5]));
  });

  test('groupBy', () => {
    const users = [
      { id: 1, group: 'A' },
      { id: 2, group: 'B' },
      { id: 3, group: 'A' }
    ];
    const grouped = groupBy(users, 'group');
    expect(grouped.A).toHaveLength(2);
    expect(grouped.B).toHaveLength(1);
    expect(grouped.C).toBeUndefined();
  });
});

describe('Object Utilities', () => {
  test('deepMerge', () => {
    const target = { a: 1, b: { c: 2 } };
    const source = { b: { d: 3 }, e: 4 };
    const result = deepMerge(target, source);
    expect(result).toEqual({ a: 1, b: { c: 2, d: 3 }, e: 4 });
  });

  test('pick', () => {
    const obj = { a: 1, b: 2, c: 3 };
    expect(pick(obj, ['a', 'c'])).toEqual({ a: 1, c: 3 });
  });

  test('omit', () => {
    const obj = { a: 1, b: 2, c: 3 };
    expect(omit(obj, ['b'])).toEqual({ a: 1, c: 3 });
  });

  test('hasNestedProp', () => {
    const obj = { a: { b: { c: 1 } } };
    expect(hasNestedProp(obj, 'a.b.c')).toBe(true);
    expect(hasNestedProp(obj, 'a.b.d')).toBe(false);
  });
});

describe('Date Utilities', () => {
  const date = new Date(2026, 3, 30, 12, 30, 45); // April 30, 2026 12:30:45

  test('formatDate', () => {
    expect(formatDate(date, 'yyyy-MM-dd')).toBe('2026-04-30');
    expect(formatDate(date, 'HH:mm:ss')).toBe('12:30:45');
    expect(formatDate(date, 'dd/MM/yyyy')).toBe('30/04/2026');
  });

  test('parseDate', () => {
    expect(parseDate('2026-04-30', 'yyyy-MM-dd')).toEqual(new Date(2026, 3, 30));
  });

  test('isWeekend', () => {
    // April 30, 2026 is Thursday
    expect(isWeekend(date)).toBe(false);
    const sunday = new Date(2026, 3, 28); // April 28, 2026 is Sunday
    expect(isWeekend(sunday)).toBe(true);
  });

  test('addDays', () => {
    const nextDay = addDays(date, 1);
    expect(nextDay.getDate()).toBe(1);
    expect(nextDay.getMonth()).toBe(3); // April (0-indexed) -> May? Wait April 30 + 1 day = May 1
    // Actually April has 30 days, so April 30 + 1 = May 1
    expect(nextDay.getMonth()).toBe(3); // April is index 3, May is index 4
    // Let's recalc: new Date(2026, 3, 30) => April 30, 2026 (month 3 is April)
    // add 1 day => May 1, 2026 (month 4)
    expect(nextDay.getMonth()).toBe(4);
    expect(nextDay.getDate()).toBe(1);
  });
});

describe('Validation Utilities', () => {
  test('isValidEmail', () => {
    expect(isValidEmail('test@example.com')).toBe(true);
    expect(isValidEmail('invalid-email')).toBe(false);
  });

  test('isValidUrl', () => {
    expect(isValidUrl('https://example.com')).toBe(true);
    expect(isValidUrl('not-a-url')).toBe(false);
  });

  test('isStrongPassword', () => {
    expect(isStrongPassword('Password123!')).toBe(true);
    expect(isStrongPassword('weak')).toBe(false);
    expect(isStrongPassword('password')).toBe(false);
    expect(isStrongPassword('PASSWORD123!')).toBe(false); // no lowercase
  });

  test('isAlpha', () => {
    expect(isAlpha('abc')).toBe(true);
    expect(isAlpha('abc123')).toBe(false);
  });

  test('isNumeric', () => {
    expect(isNumeric('123')).toBe(true);
    expect(isNumeric('12.3')).toBe(false);
  });
});

describe('Math Utilities', () => {
  test('clamp', () => {
    expect(clamp(5, 0, 10)).toBe(5);
    expect(clamp(-5, 0, 10)).toBe(0);
    expect(clamp(15, 0, 10)).toBe(10);
  });

  test('lerp', () => {
    expect(lerp(0, 10, 0.5)).toBe(5);
    expect(lerp(0, 10, 0)).toBe(0);
    expect(lerp(0, 10, 1)).toBe(10);
  });

  test('randomInRange', () => {
    const val = randomInRange(5, 10);
    expect(val).toBeGreaterThanOrEqual(5);
    expect(val).toBeLessThanOrEqual(10);
  });

  test('degToRad', () => {
    expect(degToRad(180)).toBeCloseTo(Math.PI);
    expect(degToRad(90)).toBeCloseTo(Math.PI / 2);
  });

  test('radToDeg', () => {
    expect(radToDeg(Math.PI)).toBeCloseTo(180);
    expect(radToDeg(Math.PI / 2)).toBeCloseTo(90);
  });
});

describe('Utility Functions', () => {
  test('debounce', () => {
    const mockFn = jest.fn();
    const debounced = debounce(mockFn, 100);
    debounced();
    debounced();
    expect(mockFn).not.toHaveBeenCalled();
    // advance time
    jest.advanceTimersByTime(100);
    expect(mockFn).toHaveBeenCalledTimes(1);
  });

  test('throttle', () => {
    const mockFn = jest.fn();
    const throttled = throttle(mockFn, 100);
    throttled();
    throttled();
    throttled();
    expect(mockFn).toHaveBeenCalledTimes(1);
    jest.advanceTimersByTime(100);
    throttled();
    expect(mockFn).toHaveBeenCalledTimes(2);
  });
});