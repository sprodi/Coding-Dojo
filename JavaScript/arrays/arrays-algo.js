//Print Values and Sum
var testArr = [6,3,5,1,2,4]
var sum = 0;

for(var i = 0; i < testArr.length; i++) {
  sum += testArr[i];
    console.log('Num '+''+testArr[i]);
    console.log('Sum '+''+sum);
}
//Output: 
// "Num 6"
// "Sum 6"
// "Num 3"
// "Sum 9"
// "Num 5"
// "Sum 14"
// "Num 1"
// "Sum 15"
// "Num 2"
// "Sum 17"
// "Num 4"
// "Sum 21"

//Value * Position
var testArr = [6,3,5,1,2,4]

for(i = 0; i < testArr.length; i++){
   console.log(testArr[i] * [i]);
}

//output: [0,3,10,3,8,20]