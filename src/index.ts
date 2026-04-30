// String Utilities
export function capitalize(str: string): string {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1);
}

export function camelCase(str: string): string {
  return str
    .toLowerCase()
    .replace(/[^a-zA-Z0-9]+(.)/g, (_, chr) => chr.toUpperCase());
}

export function snakeCase(str: string): string {
  return str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    ?.map((x) => x.toLowerCase())
    .join('_') ?? '';
}

export function truncate(str: string, length: number, suffix = '...'): string {
  if (str.length <= length) return str;
  return str.slice(0, length - suffix.length) + suffix;
}

// Array Utilities
export function chunkArray<T>(array: T[], size: number): T[][] {
  if (size <= 0) return [];
  const result: T[][] = [];
  for (let i = 0; i < array.length; i += size) {
    result.push(array.slice(i, i + size));
  }
  return result;
}

export function removeDuplicates<T>(array: T[]): T[] {
  return [...new Set(array)];
}

export function shuffle<T>(array: T[]): T[] {
  const shuffled = array.slice();
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

export function groupBy<T>(
  array: T[],
  key: keyof T | ((item: T) => any)
): Record<string, T[]> {
  const result: Record<string, T[]> = {};
  for (const item of array) {
    const k = typeof key === 'function' ? key(item) : item[key];
    const keyStr = String(k);
    if (!result[keyStr]) {
      result[keyStr] = [];
    }
    result[keyStr].push(item);
  }
  return result;
}

// Object Utilities
export function deepMerge<T extends object>(target: T, source: Partial<T>): T {
  const output = { ...target };
  if (isObject(target) && isObject(source)) {
    Object.keys(source).forEach((key) => {
      if (isObject(source[key as keyof T])) {
        if (!(key in target)) {
          Object.assign(output, { [key]: source[key] });
        } else {
          output[key] = deepMerge(target[key as keyof T], source[key as keyof T]);
        }
      } else {
        Object.assign(output, { [key]: source[key] });
      }
    });
  }
  return output;
}

function isObject(item: any): boolean {
  return item && typeof item === 'object' && !Array.isArray(item);
}

export function pick<T extends object>(
  obj: T,
  keys: (keyof T)[]
): Pick<T, typeof keys[number]> {
  const result: any = {};
  for (const key of keys) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      result[key] = obj[key];
    }
  }
  return result;
}

export function omit<T extends object>(
  obj: T,
  keys: (keyof T)[]
): Omit<T, typeof keys[number]> {
  const result = { ...obj };
  for (const key of keys) {
    delete result[key];
  }
  return result;
}

export function hasNestedProp<T extends object>(obj: T, path: string): boolean {
  const parts = path.split('.');
  let current = obj;
  for (const part of parts) {
    if (current == null || !(part in current)) {
      return false;
    }
    current = current[part as keyof typeof current];
  }
  return true;
}

// Date Utilities
export function formatDate(date: Date, format: string): string {
  const map: Record<string, string> = {
    yyyy: date.getFullYear().toString(),
    yy: date.getFullYear().toString().slice(-2),
    MM: String(date.getMonth() + 1).padStart(2, '0'),
    M: String(date.getMonth() + 1),
    dd: String(date.getDate()).padStart(2, '0'),
    d: String(date.getDate()),
    HH: String(date.getHours()).padStart(2, '0'),
    H: String(date.getHours()),
    mm: String(date.getMinutes()).padStart(2, '0'),
    m: String(date.getMinutes()),
    ss: String(date.getSeconds()).padStart(2, '0'),
    s: String(date.getSeconds()),
  };

  return format.replace(/(yyyy|yy|MM|M|dd|d|HH|H|mm|m|ss|s)/g, (matched) => map[matched]);
}

export function parseDate(dateString: string, format?: string): Date {
  // Simple implementation for common formats
  // In a real library, you might use a more robust parsing library or support more formats
  if (format === 'yyyy-MM-dd') {
    const [year, month, day] = dateString.split('-').map(Number);
    return new Date(year, month - 1, day);
  }
  // Fallback to ISO string parsing
  return new Date(dateString);
}

export function isWeekend(date: Date): boolean {
  const day = date.getDay();
  return day === 0 || day === 6;
}

export function addDays(date: Date, days: number): Date {
  const result = new Date(date);
  result.setDate(result.getDate() + days);
  return result;
}

// Validation Utilities
export function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

export function isValidUrl(url: string): boolean {
  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
}

export function isStrongPassword(password: string): boolean {
  // At least 8 characters, one uppercase, one lowercase, one number, one special char
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  return passwordRegex.test(password);
}

export function isAlpha(str: string): boolean {
  return /^[a-zA-Z]+$/.test(str);
}

export function isNumeric(str: string): boolean {
  return /^\d+$/.test(str);
}

// Math Utilities
export function clamp(num: number, min: number, max: number): number {
  return Math.min(Math.max(num, min), max);
}

export function lerp(start: number, end: number, t: number): number {
  return start + (end - start) * t;
}

export function randomInRange(min: number, max: number): number {
  return Math.random() * (max - min) + min;
}

export function degToRad(degrees: number): number {
  return (degrees * Math.PI) / 180;
}

export function radToDeg(radians: number): number {
  return (radians * 180) / Math.PI;
}

// File System Utilities (Node.js)
import { promises as fs } from 'fs';
import path from 'path';

export async function readFileAsync(
  filePath: string,
  encoding: BufferEncoding = 'utf8'
): Promise<string> {
  return fs.readFile(filePath, encoding);
}

export async function writeFileAsync(
  filePath: string,
  data: string | NodeJS.ArrayBufferView,
  options?: Object
): Promise<void> {
  await fs.writeFile(filePath, data, options);
}

export async function ensureDirAsync(dirPath: string): Promise<void> {
  await fs.mkdir(dirPath, { recursive: true });
}

export async function listFilesAsync(
  dirPath: string,
  options: { recursive?: boolean } = {}
): Promise<string[]> {
  const { recursive = false } = options;
  const files: string[] = [];

  const readDir = async (currentPath: string) => {
    const entries = await fs.readdir(currentPath, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(currentPath, entry.name);
      if (entry.isDirectory() && recursive) {
        await readDir(fullPath);
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
  };

  await readDir(dirPath);
  return files;
}

// Utility Functions
export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => ReturnType<T> {
  let timeout: NodeJS.Timeout;
  return function (...args: Parameters<T>) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  } as (...args: Parameters<T>) => ReturnType<T>;
}

export function throttle<T extends (...args: any[]) => any>(
  func: T,
  limit: number
): (...args: Parameters<T>) => ReturnType<T> {
  let inThrottle: boolean;
  return function (...args: Parameters<T>) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  } as (...args: Parameters<T>) => ReturnType<T>;
}