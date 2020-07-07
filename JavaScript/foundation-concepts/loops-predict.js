//Predict 1
for(var num = 0; num < 15; num++){
   console.log(num);
}
/* First Prediction was 0-15. But since 15 isn't less than 15 it doesn't console.log. It would console.log 15 if the code read num <= 15. */

//Output: 0,1,2,3,4,5,6,8,9,10,11,12,13,14


//Predict 2
for(var i = 1; i < 10; i+=2){
   if(i % 3 == 0){
       console.log(i);
   }
}
/* Integers that "i" becomes:
3,5,7,9
Since only 3 and 9 are divisable by 3 then those are the only 2 integers printed. 
I'm still getting used to how Modulo works so at times it gets a bit confusing*/

//Output: 3,9

//Predict 3
for(var j = 1; j <= 15; j++){
   if(j % 2 == 0){
       j+=2; // j=j+2
   }
   else if(j % 3 == 0){
       j++; //j=j+1
   }
   console.log(j);
}

//Output: 1,4,5,8,10,11,14,16