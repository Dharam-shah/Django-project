// var name1 = "javascript";
// console.log(name1);

// var area = "circle";
// var PI = 3.14,
//   l = 5,
//   b = 5,
//   r = 2;
// if (area == "circle") {
//   console.log("Area of circle is: " + PI * r ** 2);
// } else if (area == "trinagle") {
//   console.log("Area of trinagle is: " + (l * b) / 2);
// } else if (area == "rectangle") {
//   console.log("Area of rectangle is: " + (l + b));
// } else {
//   console.log("please enter a valid data");
// }

var area = "triangle";
var pi = 3.14,
  l = 5,
  b = 5,
  r = 2;
switch (area) {
  case "circle":
    console.log("Area of circle is: " + pi * r ** 2);
    break;

  case "triangle":
    console.log("Area of trinagle is: " + (l * b) / 2);
    break;

  case "rectangle":
    console.log("Area of rectangle is: " + (l + b));
    break;

  default:
    console.log("Enter valid data");
}
