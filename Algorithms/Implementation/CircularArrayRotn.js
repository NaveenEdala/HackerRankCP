'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the circularArrayRotation function below.
function circularArrayRotation(a, k, queries) {
    let lastEl;
    let foo = [];
    let i = queries.length;

    if (k < a.length) {
        const endValues = a.splice(-(k));
        a = [...endValues, ...a]
    }

    else if (k !== a.length) {
        while (k--) {
            lastEl = a.pop();
            a.unshift(lastEl);
        }
    }

    while (i--) { foo[i] = a[queries[i]] }
    return foo;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nkq = readLine().split(' ');

    const n = parseInt(nkq[0], 10);

    const k = parseInt(nkq[1], 10);

    const q = parseInt(nkq[2], 10);

    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));

    let queries = [];

    for (let i = 0; i < q; i++) {
        const queriesItem = parseInt(readLine(), 10);
        queries.push(queriesItem);
    }

    const result = circularArrayRotation(a, k, queries);

    ws.write(result.join('\n') + '\n');

    ws.end();
}
