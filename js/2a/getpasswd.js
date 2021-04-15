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
    var pos12 = tokens[0].split("-");
    var pos1 = parseInt(pos12[0], 10)-1;
    var pos2 = parseInt(pos12[1], 10)-1;
    // Second item is the letter
    var letter = tokens[1].substr(0, 1);
    var passwd = tokens[2];
    var lettercount = 0;
    if (passwd[pos1] == letter) lettercount++;
    if (passwd[pos2] == letter) lettercount++;
    if (lettercount==1) count++;
}
console.log(format('Found {} valid passwords', count));
