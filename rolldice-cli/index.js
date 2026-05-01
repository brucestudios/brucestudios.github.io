#!/usr/bin/env node

const { Command } = require('commander');
const chalk = require('chalk');

const program = new Command();

program
  .name('rolldice')
  .description('CLI tool for rolling dice in various formats')
  .version('1.0.0');

// Define the roll command
program
  .command('roll <notation>')
  .description('Roll dice using standard notation (e.g., 2d6, 1d20+4)')
  .option('-v, --verbose', 'Show individual dice rolls')
  .action((notation, options) => {
    const result = parseAndRoll(notation, options.verbose);
    if (options.verbose) {
      console.log(chalk.blue(`Rolling ${notation}:`));
      console.log(chalk.green(`Result: ${result.total}`));
      console.log(chalk.yellow(`Details: ${result.details.join(', ')}`));
    } else {
      console.log(chalk.green(result.total));
    }
  });

// Define the help command for specific notations
program
  .command('help')
  .description('Show help for dice notation')
  .action(() => {
    console.log(chalk.blue(`
Dice Notation Guide:
  NdM   Roll N dice with M sides each (e.g., 2d6)
  NdM+X Roll N dice with M sides each and add X (e.g., 3d8+2)
  NdM-X Roll N dice with M sides each and subtract X (e.g., 4d10-3)
  NdM   (without N) is assumed to be 1dM (e.g., d20 is 1d20)

Examples:
  rolldice roll 2d6      # Roll two six-sided dice
  rolldice roll 1d20+5   # Roll one twenty-sided dice and add 5
  rolldice roll d8       # Roll one eight-sided dice
  rolldice roll 3d10-2   # Roll three ten-sided dice and subtract 2
    `));
  });

program.parse();

// Function to parse the notation and roll the dice
function parseAndRoll(notation, verbose) {
  // Remove whitespace
  notation = notation.trim().toLowerCase();

  // Default values
  let diceCount = 1;
  let diceSides = 0;
  let modifier = 0;

  // Regular expression to parse notation like 2d6+4 or d20-3
  const pattern = /^(\d*)d(\d+)([+-]\d+)?$/;
  const match = notation.match(pattern);

  if (!match) {
    console.error(chalk.red(`Invalid dice notation: ${notation}`));
    process.exit(1);
  }

  // Parse the matched groups
  if (match[1]) {
    diceCount = parseInt(match[1], 10);
  }
  diceSides = parseInt(match[2], 10);
  if (match[3]) {
    modifier = parseInt(match[3], 10);
  }

  // Validate
  if (diceCount <= 0 || diceSides <= 0) {
    console.error(chalk.red(`Dice count and sides must be positive numbers.`));
    process.exit(1);
  }

  // Roll the dice
  const rolls = [];
  let total = 0;
  for (let i = 0; i < diceCount; i++) {
    const roll = Math.floor(Math.random() * diceSides) + 1;
    rolls.push(roll);
    total += roll;
  }
  total += modifier;

  // Prepare details for verbose output
  const details = [...rolls];
  if (modifier !== 0) {
    details.push(modifier >= 0 ? `+${modifier}` : `${modifier}`);
  }

  return {
    total,
    details,
    notation: `${diceCount}d${diceSides}${modifier >= 0 ? '+' + modifier : modifier}`
  };
}