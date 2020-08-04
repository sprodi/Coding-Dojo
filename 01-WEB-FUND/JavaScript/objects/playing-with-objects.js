var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

function nameAge() {
  for(var i = 0; i < users.length; i++) {
    console.log(users[i].name, "-", users[i].age);
  }
}

console.log("John's Age -", users[1].age);
console.log("Name of first object -", users[0].name);
console.log(" "); // Linebreak
nameAge(users);