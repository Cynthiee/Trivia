// Load the leaderboard data from the API endpoint and update the leaderboard container
    async function updateLeaderboard() {
        const response = await fetch('/api/leaderboard'); // Ensure you have an API endpoint for fetching data
        const data = await response.json();
        const container = document.getElementById('leaderboard-container');
        container.innerHTML = ''; // Clear current leaderboard

        data.forEach((entry, index) => {
            const personDiv = document.createElement('div');
            personDiv.className = 'ref-person';
            personDiv.innerHTML = `
                <p>${index + 1}</p>
                <img src="${entry.image_url}" alt="">
                <p>${entry.name}</p>
                <i>⭐</i>
                <p>${entry.referrals}</p>
            `;
            container.appendChild(personDiv);
        });
    }

    // Call the function periodically or on certain events
    setInterval(updateLeaderboard, 30000); // Update every 30 seconds

