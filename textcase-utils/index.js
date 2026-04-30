/**
 * Text Case Utilities
 * A lightweight utility for converting text between different cases
 */

const CASE_TYPES = {
  CAMEL: 'camel',
  PASCAL: 'pascal',
  SNAKE: 'snake',
  KEBAB: 'kebab',
  CONSTANT: 'constant',
  TRAIN: 'train',
  SENTENCE: 'sentence',
  TITLE: 'title'
};

/**
 * Convert string to camelCase
 * @param {string} str - Input string
 * @returns {string} camelCase string
 */
function toCamelCase(str) {
  return str
    .toLowerCase()
    .replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
}

/**
 * Convert string to PascalCase
 * @param {string} str - Input string
 * @returns {string} PascalCase string
 */
function toPascalCase(str) {
  return str
    .match(/[a-zA-Z0-9]+/g)
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join('');
}

/**
 * Convert string to snake_case
 * @param {string} str - Input string
 * @returns {string} snake_case string
 */
function toSnakeCase(str) {
  return str
    .match(/[a-zA-Z0-9]+/g)
    .map(word => word.toLowerCase())
    .join('_');
}

/**
 * Convert string to kebab-case
 * @param {string} str - Input string
 * @returns {string} kebab-case string
 */
function toKebabCase(str) {
  return str
    .match(/[a-zA-Z0-9]+/g)
    .map(word => word.toLowerCase())
    .join('-');
}

/**
 * Convert string to CONSTANT_CASE
 * @param {string} str - Input string
 * @returns {string} CONSTANT_CASE string
 */
function toConstantCase(str) {
  return str
    .match(/[a-zA-Z0-9]+/g)
    .map(word => word.toUpperCase())
    .join('_');
}

/**
 * Convert string to Train-Case
 * @param {string} str - Input string
 * @returns {string} Train-Case string
 */
function toTrainCase(str) {
  return str
    .match(/[a-zA-Z0-9]+/g)
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join('-');
}

/**
 * Convert string to sentence case
 * @param {string} str - Input string
 * @returns {string} Sentence case string
 */
function toSentenceCase(str) {
  return str
    .toLowerCase()
    .replace(/^[a-z]/, c => c.toUpperCase());
}

/**
 * Convert string to Title Case
 * @param {string} str - Input string
 * @returns {string} Title Case string
 */
function toTitleCase(str) {
  return str
    .match(/[a-zA-Z0-9]+/g)
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(' ');
}

/**
 * Convert text from one case to another
 * @param {string} text - Input text
 * @param {string} fromCase - Source case type
 * @param {string} toCase - Target case type
 * @returns {string} Converted text
 */
function convertCase(text, fromCase, toCase) {
  if (!text) return '';
  
  // Normalize input by splitting into words based on common separators
  let words;
  
  switch (fromCase) {
    case CASE_TYPES.CAMEL:
      words = text
        .replace(/[A-Z]/g, ' $&')
        .trim()
        .split(/\s+/)
        .filter(Boolean);
      break;
    case CASE_TYPES.PASCAL:
      words = text
        .replace(/[A-Z]/g, ' $&')
        .trim()
        .split(/\s+/)
        .filter(Boolean);
      break;
    case CASE_TYPES.SNAKE:
      words = text.split('_').filter(Boolean);
      break;
    case CASE_TYPES.KEBAB:
      words = text.split('-').filter(Boolean);
      break;
    case CASE_TYPES.CONSTANT:
      words = text.split('_').filter(Boolean);
      break;
    case CASE_TYPES.TRAIN:
      words = text.split('-').filter(Boolean);
      break;
    case CASE_TYPES.SENTENCE:
    case CASE_TYPES.TITLE:
      // For sentence and title case, split by spaces and punctuation
      words = text
        .split(/[\s\-_]+/)
        .filter(Boolean);
      break;
    default:
      // Fallback: split by non-alphanumeric characters
      words = text
        .match(/[a-zA-Z0-9]+/g) || [];
  }
  
  // Convert to lowercase for processing
  words = words.map(word => word.toLowerCase());
  
  // Convert to target case
  switch (toCase) {
    case CASE_TYPES.CAMEL:
      return words
        .map((word, index) => index === 0 ? word : word.charAt(0).toUpperCase() + word.slice(1))
        .join('');
    case CASE_TYPES.PASCAL:
      return words
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join('');
    case CASE_TYPES.SNAKE:
      return words.join('_');
    case CASE_TYPES.KEBAB:
      return words.join('-');
    case CASE_TYPES.CONSTANT:
      return words.map(word => word.toUpperCase()).join('_');
    case CASE_TYPES.TRAIN:
      return words
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join('-');
    case CASE_TYPES.SENTENCE:
      if (words.length === 0) return '';
      return words[0].charAt(0).toUpperCase() + words.slice(1).join(' ').toLowerCase();
    case CASE_TYPES.TITLE:
      return words
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(' ');
    default:
      return text;
  }
}

/**
 * Detect the case of a string
 * @param {string} str - Input string
 * @returns {string} Detected case type
 */
function detectCase(str) {
  if (!str) return '';
  
  if (/^[a-z]+([A-Z][a-z]*)*$/.test(str)) {
    return CASE_TYPES.CAMEL;
  }
  
  if (/^[A-Z][a-z]+([A-Z][a-z]*)*$/.test(str)) {
    return CASE_TYPES.PASCAL;
  }
  
  if (/^[a-z]+(_[a-z]+)*$/.test(str)) {
    return CASE_TYPES.SNAKE;
  }
  
  if (/^[a-z]+(-[a-z]+)*$/.test(str)) {
    return CASE_TYPES.KEBAB;
  }
  
  if (/^[A-Z]+(_[A-Z]+)*$/.test(str)) {
    return CASE_TYPES.CONSTANT;
  }
  
  if (/^[A-Z][a-z]+(-[A-Z][a-z]+)*$/.test(str)) {
    return CASE_TYPES.TRAIN;
  }
  
  if (/^[A-Z][a-z]*( [a-z]+)*$/.test(str)) {
    return CASE_TYPES.SENTENCE;
  }
  
  if (/^([A-Z][a-z]*)+( [A-Z][a-z]*)*$/.test(str)) {
    return CASE_TYPES.TITLE;
  }
  
  return 'unknown';
}

// Export functions for Node.js
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
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
  };
}

// For browser usage
if (typeof window !== 'undefined') {
  window.textCaseUtils = {
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
  };
}