// 모듈러 연산 이용 (ref. https://st-lab.tistory.com/162)
// [성질 1] (a + b) mod m = ((a mod m) + (b mod m)) mod m
// [성질 2] (a x b) mod m = ((a mod m) x (b mod m)) mod m
// [거듭제곱법] A^B mod C = ((A mod C)^B) mod C
// 모듈러 연산에서 나눗셈 연산은 없다
// 즉, 이항계수에 적용하려면 역원을 구해야 한다 => (r!(n-r)!)의 역원

// 페르마의 소정리 이용
// 소수인 p, p의 배수가 아닌 A에 대해 A^(p-1) === 1 (mod p)
// 즉, (A^(p-2)) % p = (A^(-1)) % p
// 이를 이용해서 이항계수의 분모로 인한 나눗셈을 곱셈으로 변환!

// 이항계수 식을 변형시켜 보면, 다음과 같다!
// (n! / k!(n-k)!) mod p
// = (n! x (k!(n-k)!)^(-1)) mod p
// = ((n! mod p) x ((k!(n-k)!)^(-1) mod p))  mod p
// = ((n! mod p) x ((k!(n-k)!)^(p-2) mod p)) mod p

// TLE를 막기 위해 분할정복 이용
function pow(x, y) {
    if (y === 0n) {
        return 1n;
    } else if (y === 1n) {
        return x % p;
    }
    
    var k = pow(x, BigInt(parseInt(y / 2n)));
    if (y % 2n === 1n) {
        return (k * k * x) % p;
    } else {
        return (k * k) % p;
    }
}

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
let input = fs.readFileSync(filePath).toString().split(' ').map((el) => +el);

const [n, k] = input;
const p = 1000000007n;
const fac = Array(n + 1).fill(1n);

for (let i = 2n; i <= n; i++) {
    fac[i] = (i * fac[i - 1n]) % p;
}

const num = fac[n] // 분자 N!
const den = fac[k] * fac[n - k] % p; // 분모 K!(N-K)!

const ans = num * pow(den, p - 2n) % p;
console.log(parseInt(ans));
