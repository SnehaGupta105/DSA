var minOperations = function(nums, x) {
    const totalSum = nums.reduce((sum, num) => sum + num, 0);
    const target = totalSum - x;
    if (target < 0) return -1;
    if (target === 0) return nums.length;
    let left = 0;
    let windowSum = 0;
    let maxLength = -1;
    for (let right = 0; right < nums.length; right++) {
        windowSum += nums[right];    
        while (windowSum > target && left <= right) {
            windowSum -= nums[left];
            left++;
        }
        if (windowSum === target) {
            maxLength = Math.max(
                maxLength,
                right - left + 1
            );
        }
    }
    return maxLength === -1
        ? -1
        : nums.length - maxLength;
};