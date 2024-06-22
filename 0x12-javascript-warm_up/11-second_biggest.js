// Retrieve arguments from the command line, excluding the first two default ones (node and script path)
let args = process.argv.slice(2);

// Convert all arguments to integers
let integers = args.map(arg => parseInt(arg, 10));

// Check if there are less than 2 integers
if (integers.length < 2) {
    console.log(0);
} else {
    // Find the second largest integer
    let max = -Infinity;
    let secondMax = -Infinity;

    for (let num of integers) {
        if (num > max) {
            secondMax = max;
            max = num;
        } else if (num > secondMax && num < max) {
            secondMax = num;
        }
    }

    console.log(secondMax);
}

