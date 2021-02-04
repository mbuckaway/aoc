using System;
using System.IO;
using System.Text;
using System.Linq;
using System.Collections.Generic;

namespace aic
{
    class Get20203
    {        
        static void Main(string[] args)
        {
            if (args.Length<1)
            {
                Console.WriteLine($"Usage: get2020 input.txt");
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
            var numbers = new List<int>();

            using (var streamReader = new StreamReader(fileStream, Encoding.UTF8)) {
                string line;

                while ((line = streamReader.ReadLine()) != null) 
                {
                    var value = Int32.Parse(line.Trim());
                    numbers.Add(value);
                }
                numbers.Sort();
            }
            Console.WriteLine($"{numbers.Count} numbers found");
            // Two loops, one starts from the top, and one starts from the bottom. We are looking for two items that add up to 2020
            var result = 0;
            foreach(var start in numbers)
            {
                foreach(var middle in numbers)
                {
                    foreach(var end in Enumerable.Reverse(numbers))
                    {
                        if (start+middle+end==2020)
                        {
                            result = start*middle*end;
                            Console.WriteLine($"Numbers are {start}, {middle}, and {end}");
                            Console.WriteLine($"And the answer is: {result}");
                            break;
                        }
                    }
                    if (result!=0)
                    {
                        break;
                    }
                }
                if (result!=0)
                {
                    break;
                }
            }
        }
    }
}
