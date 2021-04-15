//
// Adventure in Code task 1
//

var fs = require('fs');
const yargs = require('yargs');

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

if (argv.filename) {
    console.log("Using filename: " + argv.filename);
}

var array = fs.readFileSync(argv.filename).toString().split("\n");
var array2 = array.slice();
const desc = array.sort((a, b) => {  
     return a - b
   })
 const accend = array2.sort((a, b) => {  
     return b - a
 })

var number = 0;
for(i in array)
{
    for (j in array2)
    {
        var val1 = parseInt(array[i], 10)
        var val2 = parseInt(array2[j], 10)
        sum = val1 + val2
        console.log(val1 + " + " + val2 + " = " + sum);
        if (sum == 2020)
        {
            number = val1 * val2;
            console.log("The numbers are " + val1 + " and " + val2 + " and the product is " + number);
            break;
        }
    }
    if (number != 0)
    {
        break;
    }
}
