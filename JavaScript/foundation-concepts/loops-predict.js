//Predict 1
for(var num = 0; num < 15; num++){
   console.log(num);
}
//Output: 0,1,2,3,4,5,6,8,9,10,11,12,13,14


//Predict 2
for(var i = 1; i < 10; i+=2){
   if(i % 3 == 0){
       console.log(i);
   }
}
/* Integers that "i" becomes:
3,5,7,9
Since only 3 and 9 are divisable by 3 then those are the only 2 integers printed. */

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