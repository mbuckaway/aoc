using System;
using System.IO;
using System.Text;
using System.Linq;
using System.Collections.Generic;

namespace aic
{
    class GetPasswd
    {        
        static void Main(string[] args)
        {
            if (args.Length<1)
            {
                Console.WriteLine($"Usage: getpasswd input.txt");
                System.Environment.Exit(1);
            }
            var filename = args[0];
            Console.WriteLine($"Opening File: {filename}");
            if (!File.Exists(filename))
            {
                Console.WriteLine($"File {filename} does not exist");
                System.Environment.Exit(1);
            }
            var fileStream = new FileStream(args[0], FileMode.Open, FileAccess.Read);
            var result = 0;
            using (var streamReader = new StreamReader(fileStream, Encoding.UTF8))
            {
                string line;
                while ((line = streamReader.ReadLine()) != null) 
                {
                    // First item is rule, second is password
                    var items = line.Trim().Split(':');
                    var password = items[1].Trim();
                    var rules = items[0].Split(' ');
                    var letter = rules[1].Trim();
                    var count = rules[0].Split('-');
                    var min = Int16.Parse(count[0]);
                    var max = Int16.Parse(count[1]);
                    Console.WriteLine($"Password: {password} must be {min}-{max} {letter}'s in it");
                    // Now, count the number of "letters" found
                    var lettercount = 0;
                    for (var i=0; i<password.Length; i++)
                    {
                        if (password[i] == letter[0])
                        {
                            lettercount++;
                        }
                    }
                    Console.WriteLine($"Got {lettercount} items");
                    if (lettercount>=min && lettercount<=max)
                    {
                        Console.WriteLine("Got one!");
                        result++;
                    }
                }
            }
            Console.WriteLine($"There are {result} good passwords");
        }
    }
}
