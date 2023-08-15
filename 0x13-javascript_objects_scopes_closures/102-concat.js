#!/usr/bin/node

const fs = require('fs').promises;

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

async function concat () {
  const dataA = await fs.readFile('./' + fileA, 'utf8');
  const dataB = await fs.readFile('./' + fileB, 'utf8');
  await fs.writeFile(fileC, dataA + '\n' + dataB);
}

concat();
