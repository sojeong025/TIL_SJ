// 1번
const nums = [1,2,3,4,5,6,7,8]

console.log('1번 출력 결과')
for (let i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}
console.log()
// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// const로 초기화한 변수는 재할당이 불가능해서 발생하는 문제다.


// 2번
console.log('2번 출력 결과')
for (num in nums) {
  console.log(num, typeof num)
  // 출력 결과
  // 0 string
  // 1 string
  // 2 string
  // 3 string
  // 4 string
  // 5 string
  // 6 string
  // 7 string
}
