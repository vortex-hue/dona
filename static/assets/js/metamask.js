// metamask.js
document.addEventListener("DOMContentLoaded", function () {
    const connectMetamaskButton = document.getElementById("connect-metamask-button");

    // Function to update the button text
    function updateButtonText(connected) {
        if (connected) {
            connectMetamaskButton.textContent = "Connected";
        } else {
            connectMetamaskButton.textContent = "Connect to MetaMask";
        }
    }

    // Initialize as not connected
    let isConnected = false;
    updateButtonText(isConnected);

    // Listen for button click
    connectMetamaskButton.addEventListener("click", async () => {
        // Check if MetaMask is available
        if (typeof window.ethereum !== "undefined") {
            const web3 = new Web3(window.ethereum);
       
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

                // Get the user's Ethereum address
                const userAddress = accounts[0];

                // You can now use 'userAddress' for further operations
                alert(`Connected to MetaMask. User's address: ${userAddress}`);

                // Set the connection status to connected
                isConnected = true;
                updateButtonText(isConnected);
            } catch (error) {
                alert("Error connecting to MetaMask:", error);
            }
        }else {
            alert("MetaMask is not available. Please install MetaMask.");
            };
        });
});
