//Biggie Size - Given an array, write a function that changes all positive numbers in the array to the string "big".  Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].
function bigSize(arr) {
   for(var i = 1; i < arr.length; i++) {
      if(arr[i] > 0) {
         arr[i] = "big";
      }
   }
   return arr;
}
// console.log(bigSize([-1,3,5,-5]));

// Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.
function lowHigh(arr) {
   var max = arr[0];
   var low = arr[0];
 
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] > max) {
       max = arr[i];
     }
     if(arr[i] < low) {
       low = arr[i];
     }
   }
   console.log("Lowest Value:",low)
   return max;
 }
// console.log(lowHigh([2,5,-1,13]));
// console.log(lowHigh([19,92,1,13]));

// Double Vision - Given an array (similar to saying 'takes in an array'), create a function that returns a new array where each value in the original array has been doubled.  Calling double([1,2,3]) should return [2,4,6] without changing the original array.
function doubleArr(arr) {
   var newArr = [];
 
   console.log("Original Array:",arr);
   for(var i = 0; i < arr.length; i++) {
     newArr.push(arr[i] * 2);
   }
   return newArr;
 }
//  console.log("Array Doubled:",doubleArr([1,2,3]));
//  console.log("Array Doubled:",doubleArr([2,4,6]));
 
// Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.  Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.
function countPos(arr) {
   var count = 0;
 
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] > 0) {
       count++;
       arr[arr.length - 1] = count;
     }
   }
   return arr
 }
// console.log(countPos([-1,1,1,1]));
// console.log(countPos([-3,3,7,5-2]));

// Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!".
function evenOdd(arr) {
   var oddCount = 0;
   var evenCount = 0;
 
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] % 2 === 1) {
       oddCount++;
       evenCount = 0;
     }
     if(arr[i] % 2 === 0) {
       evenCount++;
       oddCount = 0;
     }
 
     if(oddCount === 3) {
       console.log("That's odd!");
       oddCount = 0;
     }
     if(evenCount === 3) {
       console.log("Even more so!");
       evenCount = 0;
     }
   }
 }
// console.log(evenOdd([1,1,3,1,4,3,2,4,6]));

// Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.
function addToOdd(arr) {
   for(var i = 0; i < arr.length; i++) {
     if(i % 2 === 1) {
       arr[i]++;
     }
     console.log(arr[i]);
   }
   return arr;
 }
// console.log(addToOdd([7,2,9,1,5,3]));

// Previous Lengths - You are passed an array (similar to saying 'takes in an array' or 'given an array') containing strings.  Working within that same array, replace each string with a number - the length of the string at the previous array index - and return the array.  For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4]. Hint: Can for loops only go forward?
function preLength(arr) {
   var preArr = arr[i];
   var output = [];
 
   output.push(arr[0]);
   for(var i = 0; i+1 < arr.length; i++){
       arr[i] = arr[i].length;
       preArr = arr[i];
       output.push(preArr);
   }
   return output;
 }
//  console.log(preLength(["hello", "dojo", "awesome!"]));
//  console.log(preLength(["sean", "jessica", "parker", "awesome!"]));

// Add Seven - Build a function that accepts an array. Return a new array with all the values of the original, but add 7 to each. Do not alter the original array.  Example, addSeven([1,2,3]) should return [8,9,10] in a new array.
function addSeven(arr) {
   var output = [];
 
   for(var i = 0; i < arr.length; i++) {
     output.push(arr[i]+7)
   }
     console.log("Original:", arr);
     return output;
 }
 // console.log("Add 7:", addSeven([1,2,3]));
 // console.log("Add 7:", addSeven([5,7,9]));

 // Reverse Array - Given an array, write a function that reverses its values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array, but now contains values reversed like so... [2,4,6,1,3].  Do this without creating an empty temporary array.  (Hint: you'll need to swap values).
function reverseArr() {
   var arr = [3,1,6,4,2];
   console.log("Original:",arr);
   var newArr = arr.reverse();
   return newArr;
 }
 // console.log(reverseArr());
 
// Outlook: Negative - Given an array, create and return a new one containing all the values of the original array, but make them all negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].
function negArr(arr) {
   var newArr = [];
   for(var i = 0; i < arr.length; i++) {
     newArr.push(-Math.abs(arr[i]));
     //if you use "Math.abs" instead, then all negative values become positive
   }
   return newArr;
 }
 var x = [1,- 3, 5];
// console.log(negArr(x));

// Always Hungry - Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food".  If no array values are "food", then print "I'm hungry" once.
function nomNom(arr) {
   var count = 0;
   for(var i = 0; i < arr.length; i++) {
     if(arr[i] === "food") {
       console.log("Yummy");
     } else {
       count++;
     }
      if(count == arr.length) {
      return "I'm Hungry";
      }
   }
 }
// nomNom([1, 8, "food", "food", 9, "food"]);
// nomNom([1, 2, 3]);

// Swap Toward the Center - Given an array, swap the first and last values, third and third-to-last values, etc.  Example: swapTowardCenter([true,42,"Ada",2,"pizza"]) turns the array into ["pizza", 42, "Ada", 2, true].  swapTowardCenter([1,2,3,4,5,6]) turns the array into [6,2,4,3,5,1].  No need to return the array this time.
function swapCenter(arr) {
   var temp = arr[0];
   var temp2 = arr[2];
 
   for(var i = 0; i < arr.length; i++) {
     arr[0] = arr[arr.length - 1];
     arr[arr.length - 1] = temp;
     arr[2] = arr[arr.length - 3];
     arr[arr.length - 3] = temp2;
     return arr;
   }
 }
 // console.log(swapCenter([1,2,3,4,5,6]));
 // console.log(swapCenter([true, 42, "Ada", 2, "pizza"]));
 // console.log(swapCenter(["last", "second", "thirdLast", "middle", "third", "secondLast", "first"]))

 // Scale the Array - Given an array arr and a number num, multiply all values in the array arr by the number num, and return the changed array arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9].
function scaleArray(arr, num) {
   var newArr = [];
 
   for(var i = 0; i < arr.length; i++) {
     arr[i] *= num;
     newArr.push(arr[i]);
   }
   return newArr;
 }
//  console.log(scaleArray([1,2,3], 3));
//  console.log(scaleArray([2,4,6], 2));
 