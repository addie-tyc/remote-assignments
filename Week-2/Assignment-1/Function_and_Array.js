function max(numbers) {
  let max = numbers.pop();
  for (i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];    
    }
  }
  return max;
}

function findPosition(numbers, target) {
  let ans = -1
  for (i = 0; i < numbers.length; i++) {
    if (numbers[i] === target) {
      ans = i; 
      break;   
    }
  }
  return ans;
}