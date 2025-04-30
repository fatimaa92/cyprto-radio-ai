const aiComments = [
    { username: "CryptoGenius42", comment: "This market is wilder than a caffeinated alpaca! 🚀" },
    { username: "BlockchainWizard", comment: "If my investments had emotions, they’d be crying. 😭" },
    { username: "AI_Hodler", comment: "I asked ChatGPT if I should sell, it said ‘maybe.’ Thanks, AI. 🤖" },
    { username: "MoonBot9000", comment: "Alpaca Finance trending? My retirement plan just got fuzzier. 🦙" },
    { username: "RugPullDetective", comment: "Crypto influencers should come with warning labels. ⚠️" }
];

let currentIndex = 0;

function updateComments() {
    const commentBox = document.getElementById("ai-comments");

    const { username, comment } = aiComments[currentIndex];
    commentBox.innerHTML = `<p><strong>${username}</strong>: ${comment}</p>`;

    currentIndex = (currentIndex + 1) % aiComments.length; // Loop through array
}

// Update comment every 5 seconds
setInterval(updateComments, 5000);

// Initial call to display first comment
updateComments();
