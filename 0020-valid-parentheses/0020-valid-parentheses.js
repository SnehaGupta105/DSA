var isValid = function(s) {
    let stack = [];

    let pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let ch of s) {
        // Opening bracket
        if (ch === '(' || ch === '[' || ch === '{') {
            stack.push(ch);
        } 
        // Closing bracket
        else {
            if (stack.length === 0 || stack.pop() !== pairs[ch]) {
                return false;
            }
        }
    }

    return stack.length === 0;
};