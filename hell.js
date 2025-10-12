// let n = 10;
// function SumOfNumbers(n) {
//     if (n <= 1) return n;
//     return n + SumOfNumbers(n - 1);
// }
// // SumOfNumbers(n);
// console.log(SumOfNumbers(n))


// let arry = [1, 5, 4, 7, 8, 5, 2, 4, 7, 0];

// function SumOfArry(n) {
//     if (arry[i] == 0) return n;
//     return arry[n]+SumOfArry(n-1)
// }
// console.log(SumOfArry(arry.length-1))


// function Rec(n) {
//     if (n < 0) return;
//     console.log(n);
//     return Rec(--n);
// }
// // console.log(Rec(10))

// Rec(10)


// function Rect(n) {
//     if (n < 0) return;
//     console.log(n);
//     return Rect(n++);
// }
// Rect(5)


// function Hello(n) {
//     if (n < 1) return;
//     console.log(n);
//     Hello(--n);
// }
// Hello(10)

// let n=20
// function Hello(x) {
//     if (x == n) return;
//     console.log(x);
//     Hello(++x);
// }
// Hello(1)


let n = 15;
function Hello(x) {
    if (x > n) return;
    console.log(x);
    Hello(++x);
}
Hello(1)