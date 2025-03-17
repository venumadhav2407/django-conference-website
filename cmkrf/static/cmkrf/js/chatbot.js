const chatbotToggle = document.getElementById("chatbotToggle");
const chatbotWindow = document.getElementById("chatbotWindow");
const closeChatbot = document.getElementById("closeChatbot");
const chatInput = document.getElementById("chatInput");
const sendMessage = document.getElementById("sendMessage");
const chatBox = document.getElementById("chatBox");

chatbotToggle.addEventListener("click", () => {
    chatbotWindow.classList.toggle("hidden");
});

closeChatbot.addEventListener("click", () => {
    chatbotWindow.classList.add("hidden");
});

const responses = {
    "hi": "Hello! How can I assist you?",
    "hello": "Hi there! Need help with the Surgeon Summit?",
    "schedule": "The summit schedule will be available soon. Stay tuned!",
    "venue": "The summit will be held at AIIMS, New Delhi.",
    "register": "You can register on our official website.",
    "thanks": "You're welcome! 😊",
    "default": "Sorry, I didn't understand. Can you please rephrase?"
};



function addMessage(message, sender = "user") {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("p-2", "rounded-lg", sender === "user" ? "bg-blue-500 text-white" : "bg-gray-100", "w-fit", "max-w-xs");
    msgDiv.textContent = message;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
}

sendMessage.addEventListener("click", () => {
    const userMessage = chatInput.value.trim().toLowerCase();
    if (userMessage === "") return;

    addMessage(userMessage, "user");
    chatInput.value = "";

    setTimeout(() => {
        const botReply = responses[userMessage] || responses["default"];
        addMessage(botReply, "bot");
    }, 1000); // Simulating typing delay
});

chatInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") sendMessage.click();
});