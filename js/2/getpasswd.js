//
// Adventure in Code task 2
//

const fs = require('fs');
const yargs = require('yargs');
const format = require('string-format')

var myArgs = process.argv.slice(2);

const argv = yargs
    .option('filename', {
        alias: 'f',
        description: 'Filename to load',
        type: 'string',
        demandOption: true
    })
    .help()
    .alias('help', 'h')
    .argv;

if (argv.filename)
{
    console.log("Using filename: " + argv.filename);
}

var array = fs.readFileSync(argv.filename).toString().split("\n");
var count = 0;
for(i in array)
{
    if (array[i] == '')
    {
        continue;
    }
    var tokens = array[i].split(" ");
    // First item is the min/max
    var minmax = tokens[0].split("-");
    var min = parseInt(minmax[0], 10);
    var max = parseInt(minmax[1], 10);
    // Second item is the letter
    var letter = tokens[1].substr(0, 1);
    var passwd = tokens[2];
    var lettercount = 0;
    for (i in passwd)
    {
        if (passwd[i] == letter)
        {
            lettercount++;
        }
    }
    if ((lettercount>=min) && (lettercount<=max))
    {
        count++;
    }
}
console.log(format('Found {} valid passwords', count));
