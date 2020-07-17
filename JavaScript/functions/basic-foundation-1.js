// Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function array(min, max) {
   var output = [];
   for(var i = min; i <= max; i++) {
     output.push(i);
   }
   return output;
 }
// console.log(array(1, 255))

// Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
function evenSum() {
   var sum = 0;
   for(var i=2; i <= 1000; i+=2) {
     if(i % 2 === 0) {
       sum = sum + i;
     }
   }
   return sum;
 }
// console.log(evenSum()); 

// Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999)
function oddSum() {
   var sum = 0;
   for(var i=1; i <= 5000; i+=2) {
     if(i % 2 !== 0) {
       sum = sum + i;
       console.log(i)
     }
   }
   return sum;
 }
// console.log(oddSum()); 

// Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
function sumArr(num) {
   var sum = 0;
     for(var i = 0; i < num.length; i++) {
       sum = sum + num[i];
     }
   return sum;
 }
// console.log(sumArr([1,2,5])); 
// console.log(sumArr([-5,2,5,12])); 

// Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
function findMax(num) {
   var max = num[0];
   for(var i = 0; i < num.length; i++) {
     if(num[i] > max) {
       max = num[i];
     }
   }
   return max;
 }
// console.log(findMax([-3,3,5,7])); 
// console.log(findMax([1,92,13,4])); 

// Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
function findAvg(num) {
   var avg = 0;
   var sum = 0;
   for(var i = 0; i < num.length; i++) {
     sum = sum + num[i];
   }
   avg = sum / num.length;
   return avg;
 }
// console.log(findAvg([1,3,5,7,20])); 
// console.log(findAvg([5,10,15]));

// Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
 function arrayOdd() {
   var newArray = [];
   for(var i = 1; i < 50; i+=2) {
     if(i % 2 !== 0) {
       newArray.push(i);
     }
   }
   return newArray;
 }
// console.log(arrayOdd()); 

// Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
function greaterThan(arr, y) {
   var high = 0;
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] > y) {
       high++;
     }
   }
   return high;
 }
// console.log(greaterThan([1,3,5,7], 3)); 
 
// Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
function squareArr(arr) {
   for(var i = 0; i < arr.length; i++) {
     arr[i] *= arr[i];
     }
   return arr;
 }
// console.log(squareArr([1,5,10,-2])); 

// Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
function negArr(arr) {
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] < 0) {
       arr[i] = 0;
     }
   }
   return arr;
 }
// console.log(negArr([1,5,10,-2])); 
// console.log(negArr([-1,13,19,-92]));

// Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
function maxMin(arr) {
   var avg = 0;
   var sum = 0;
   var max = arr[0];
   var min = arr[0];
   var newArr = []
 
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] > max) {
       max = arr[i];
     }
     if(arr[i] < min) {
       min = arr[i];
     }
     sum = sum + arr[i];
   }
     avg = sum / arr.length;
 
   newArr.push(max);
   newArr.push(min);
   newArr.push(avg);
   return newArr;
 }
// console.log(maxMin([1,5,10,-2]))
// console.log(maxMin([2,4,8,6]))
 
// Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
function swapVal(arr) {
   var num = 0;
 
   if(arr.length < 2) {
     return arr;
   }else{
     num = arr[0];
     arr[0] = arr[arr.length-1];
     arr[arr.length-1] = num;
   }
   return arr;
 }
// console.log(swapVal([1,5,10,-2]))
// console.log(swapVal([1,13,19,92]))

 // Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].
function numStr(arr) {
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] < 0) {
       arr[i] = "Dojo"
     }
   }
   return arr;
 }
// console.log(numStr([-1,-3,2]))
// console.log(numStr([-1,13,-19,92])) 