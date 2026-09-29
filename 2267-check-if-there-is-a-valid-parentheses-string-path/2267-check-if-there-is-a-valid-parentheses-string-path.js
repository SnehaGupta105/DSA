/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var hasValidPath = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    if ((m + n - 1) % 2 !== 0) {
        return false;
    }
    const dp = Array.from(
        { length: m },
        () => Array.from({ length: n }, () => new Set())
    );
    const startBalance = grid[0][0] === '(' ? 1 : -1;
    if (startBalance < 0) {
        return false;
    }

    dp[0][0].add(startBalance);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;

            const currentSet = dp[i][j];
            const change = grid[i][j] === '(' ? 1 : -1;
            if (i > 0) {
                for (const balance of dp[i - 1][j]) {
                    const newBalance = balance + change;

                    if (newBalance >= 0) {
                        currentSet.add(newBalance);
                    }
                }
            }
            if (j > 0) {
                for (const balance of dp[i][j - 1]) {
                    const newBalance = balance + change;
                    if (newBalance >= 0) {
                        currentSet.add(newBalance);
                    }
                }
            }
        }
    }
    return dp[m - 1][n - 1].has(0);
};