// Setting and Swapping
    var myNumber = 42;
    var myName = "Sean";
    [myNumber , myName] = [myName , myNumber];
    console.log(myNumber, myName)

// Print -52 to 1066
for(var num = -52; num < 1067; num++) {
	console.log(num)
}

// Don't Worry, Be Happy
function beCheerful(){
	for(var i = 0; i < 98; i++){
  console.log("Good Morning!");
  }
}
beCheerful()

// Print and Count
function printCount(){
  var arr = [];

  for(var i = 512; i < 4096; i++){
    if(i % 5 === 0){
    arr.push(i)
    }
  }
return arr;
}

// Multiples of Six
var i = 6;
while (i >= 6 && i <= 60000) {
    if (i%6===0) {
        console.log(i);
    }
    i++;
}

// Counting, the Dojo Way
function Counting(){
  for(var i = 1; i <= 100; i++){
    if(i % 5 === 0){
      console.log('Coding');
    if(i % 10 === 0){
       console.log('Dojo');
       }  
    }
    else {
      console.log(i);
    }
  }
}
Counting();

// Multiples of Three - but Not All
function three(){
  for(var i = -300; i <= -9; i += 3){
    console.log(i)
  }
}
three();

// What Do You Know?
function parameter(incoming){
  console.log(incoming);
}
parameter(501)

// Printing Intergers with While
var i = 1999;

while(i < 5280) {
  i++
  console.log(i)
}

// Woah, That Sucker's Huge...
function woah(){
  var sum = 0;

  for(var i = 1; i < 300000; i+=2) {
    if(i % 2 === 1){
      sum += i;
    }
  }
  return(sum*2);
}

//Countdown by Fours
let i = 2016;

while(i > 0){
  console.log(i);
  i-=4;
}

// You Say It's Your Brithday
function bday(num1,num2){
  var month = 1;
  var date = 13;
  
  if(num1 === month || num2 === month){
    if(num2 === date || num1 === date){
      console.log('How did you know?');
    }
    else{
    console.log('Just another day...');
    }
  }
  else{
    if(month === date){
      if(num1 === num2){
        console.log('How did you know?');
      }
      else{
      console.log('Just another day...');
      }
    }
    else{
    console.log('Just another day...');
    }
  }
}

bday(1,4)
bday(13,1)
bday(3,24)
bday(3,27)
bday(13,1)

// Leap Year
function leap(year){
  
  if(year % 4 === 0){
    return 'Leap Year';
  }
  else if(year % 400 === 0){
    if(year % 100 === 0){
      return 'Not Leap Year';
    }
  return 'Leap Year'; 
  }
return 'Not Leap Year';
}

//2020 is leap year, next leap year should be 2024
console.log(leap(2020))
console.log(leap(2021))
console.log(leap(2022))
console.log(leap(2023))
console.log(leap(2024))

//Flexible Countdown
function flexCount(lowNum, highNum, mult){
  let num = highNum;
  
  while(num > lowNum){ 
    if(num % mult === 0){
      console.log(num);
      num -= mult;
    }
    else{ 
      num --;
    }
  }
}
flexCount(2,9,3)

//The Final Countdown

/*  Param1 = target
    Param2 = lowNum
    Param3 = highNum
    Param4 = Exception */

function finCount(param1,param2,param3,param4){
  let num = param2;
 
  while(num < param3){
    if(num % param1 === 0){
      if(num % param4 !== 0){
        console.log(num);
      }
    }
    num++;
  }
}

finCount(3,5,17,9);