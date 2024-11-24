async function updateLeaderboard() {
    try {
        const response = await fetch('/waitlist/leaderboard/');
        if (!response.ok) throw new Error('Failed to fetch leaderboard data.');

        const leaderboard = await response.json();
        const leaderboardTable = document.getElementById('leaderboardTable');

        leaderboardTable.innerHTML = leaderboard
            .map(user => `<div>${user.name}: ${user.referrals_count}</div>`)
            .join('');
    } catch (error) {
        console.error('Error updating leaderboard:', error);
    }
}


setInterval(updateLeaderboard, 3600000);

updateLeaderboard();
