# RollDice CLI

A flexible command-line tool for rolling dice in various formats, perfect for tabletop RPGs, board games, or any situation needing random number generation.

## Features

- Support for standard dice notation (e.g., `2d6`, `1d20+4`)
- Verbose mode to see individual rolls
- Simple and intuitive interface
- Zero dependencies beyond commander and chalk

## Installation

```bash
npm install -g rolldice-cli
```

Or clone and link locally:

```bash
git clone https://github.com/yourusername/rolldice-cli.git
cd rolldice-cli
npm link
```

## Usage

### Basic Rolls

```bash
rolldice roll 2d6      # Roll two six-sided dice
rolldice roll d20      # Roll one twenty-sided dice (d20 = 1d20)
rolldice roll 3d8      # Roll three eight-sided dice
```

### With Modifiers

```bash
rolldice roll 1d20+5   # Roll d20 and add 5
rolldice roll 4d10-3   # Roll four d10 and subtract 3
rolldice roll 2d4+8    # Roll two d4 and add 8
```

### Verbose Output

Use `-v` or `--verbose` to see individual rolls:

```bash
rolldice roll 3d6 -v
# Output:
# Rolling 3d6:
# Result: 12
# Details: 3, 4, 5
```

### Help

```bash
rolldice help
# Shows detailed notation guide
```

## Examples

```bash
# Roll for damage: 2d6+3
rolldice roll 2d6+3

# Roll for initiative: 1d20+dex modifier
rolldice roll 1d20+4

# Roll multiple attacks: 3d8
rolldice roll 3d8

# Roll with subtraction: 2d10-2
rolldice roll 2d10-2
```

## Notation Guide

- `NdM`: Roll N dice with M sides each. If N is omitted, it defaults to 1.
- `NdM+X`: Add X to the total.
- `NdM-X`: Subtract X from the total.

Examples:
- `d6` or `1d6`: One six-sided die
- `2d8`: Two eight-sided dice
- `3d10+15`: Three ten-sided dice plus 15
- `4d6-2`: Four six-sided dice minus 2

## License

MIT

## Contributing

Feel free to submit issues or pull requests!
