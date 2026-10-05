var checkValidString = function(s) {
    let minOpen = 0;
    let maxOpen = 0;

    for (let ch of s) {
        if (ch === '(') {
            minOpen++;
            maxOpen++;
        } 
        else if (ch === ')') {
            minOpen--;
            maxOpen--;
        } 
        else { // '*'
            minOpen--; // '*' as ')'
            maxOpen++; // '*' as '('
        }

        // Even in the best case, too many ')'
        if (maxOpen < 0) {
            return false;
        }

        // Minimum cannot be negative
        minOpen = Math.max(0, minOpen);
    }

    // If some possibility has 0 open brackets
    return minOpen === 0;
};