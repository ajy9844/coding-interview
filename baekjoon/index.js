function solution() {
    console.log("함수를 작성하세요.");
}

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
let input = fs.readFileSync(filePath).toString().split(' ').map((el) => +el);

console.log("답을 출력하세요.");