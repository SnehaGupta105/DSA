var uniformArray = function(nums1) {
    let min = Math.min(...nums1);

    // If minimum is odd, we can make everything odd
    if (min % 2 === 1) {
        return true;
    }

    // Minimum is even.
    // If there is any odd number, it cannot be made even.
    for (let x of nums1) {
        if (x % 2 === 1) {
            return false;
        }
    }

    return true;
};