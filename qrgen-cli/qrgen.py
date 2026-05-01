#!/usr/bin/env python3
"""
QRGen CLI - Generate QR codes from command line.

Supports outputting as PNG, SVG, or terminal ASCII art.
"""

import argparse
import sys
import os

def generate_ascii(qr):
    """Generate ASCII representation of QR code."""
    # Using qrcode's constants for dark and light modules
    dark = '██'
    light = '  '
    lines = []
    for r in qr.modules:
        line = ''.join(dark if c else light for c in r)
        lines.append(line)
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Generate QR codes from text or file input."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--text', help='Text to encode')
    group.add_argument('-f', '--file', help='Read input from file')
    parser.add_argument('-o', '--output', help='Output file path (if omitted, outputs ASCII to terminal)')
    parser.add_argument('-s', '--size', type=int, default=10, help='Size of each module in pixels (for image output, default 10)')
    parser.add_argument('-b', '--border', type=int, default=4, help='Border size (default 4)')
    parser.add_argument('-e', '--error', choices=['L', 'M', 'Q', 'H'], default='M', help='Error correction level (L, M, Q, H, default M)')

    args = parser.parse_args()

    # Determine input data
    if args.text:
        data = args.text
    else:
        if not os.path.isfile(args.file):
            sys.stderr.write(f"Error: File '{args.file}' not found.\n")
            sys.exit(1)
        with open(args.file, 'r', encoding='utf-8') as f:
            data = f.read()

    # Try to use segno for image output (supports PNG, SVG, terminal)
    try:
        import segno
        HAVE_SEGNO = True
    except ImportError:
        HAVE_SEGNO = False

    if args.output:
        # Image output
        if HAVE_SEGNO:
            qrcode = segno.make(data, error=args.error)
            # Save with scale (size) and border
            qrcode.save(args.output, scale=args.size, border=args.border)
            print(f"QR code saved to {args.output}")
        else:
            # Fallback to qrcode library
            try:
                import qrcode
                from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
                error_map = {
                    'L': ERROR_CORRECT_L,
                    'M': ERROR_CORRECT_M,
                    'Q': ERROR_CORRECT_Q,
                    'H': ERROR_CORRECT_H
                }
                qr = qrcode.QRCode(
                    version=None,
                    error_correction=error_map[args.error],
                    box_size=args.size,
                    border=args.border,
                )
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(args.output)
                print(f"QR code saved to {args.output}")
            except ImportError:
                sys.stderr.write("Error: No QR code library installed. Please install 'segno' or 'qrcode[pil]'.\n")
                sys.exit(1)
    else:
        # Terminal ASCII output
        if HAVE_SEGNO:
            # segno can output terminal directly
            qrcode = segno.make(data, error=args.error)
            # Use segno's terminal output
            sys.stdout.write(qrcode.terminal(compact=True))
        else:
            # Fallback to qrcode for terminal
            try:
                import qrcode
                from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
                error_map = {
                    'L': ERROR_CORRECT_L,
                    'M': ERROR_CORRECT_M,
                    'Q': ERROR_CORRECT_Q,
                    'H': ERROR_CORRECT_H
                }
                qr = qrcode.QRCode(
                    version=None,
                    error_correction=error_map[args.error],
                    box_size=args.size,
                    border=args.border,
                )
                qr.add_data(data)
                qr.make(fit=True)
                # Build ASCII
                lines = []
                for r in qr.modules:
                    line = ''.join('██' if c else '  ' for c in r)
                    lines.append(line)
                sys.stdout.write('\n'.join(lines) + '\n')
            except ImportError:
                sys.stderr.write("Error: No QR code library installed. Please install 'segno' or 'qrcode'.\n")
                sys.exit(1)

if __name__ == '__main__':
    main()