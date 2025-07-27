const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const chatId = "frontend_user";  // Unique ID for the chat session
const typingIndicator = document.getElementById("typing-indicator");
const modelBadge = document.getElementById("status-badge");

async function loadChatHistory() {
  try {
    const response = await fetch(`http://localhost:8003/history/${chatId}`);
    const data = await response.json();
    data.messages.forEach(msg => {
      appendMessage(msg.role === "user" ? "You" : "AI", msg.message, msg.role);
    });
  } catch (error) {
    console.error("Failed to load history:", error);
  }
}

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage("You", message, "user");
  await saveHistory(chatId, message, "user");
  userInput.value = "";

  const llmChoice = document.getElementById("llm-choice").value;
  updateModelBadge(llmChoice);

  typingIndicator.classList.remove("hidden");  // Show typing...

  try {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ chat_id: chatId, message: message, model: llmChoice })
    });

    const data = await response.json();
    appendMessage("AI", data.response, "ai");
    await saveHistory(chatId, data.response, "assistant");

  } catch (error) {
    appendMessage("System", "Error connecting to server.", "system");
    console.error(error);
  } finally {
    typingIndicator.classList.add("hidden");  // Hide typing...
  }
}

function appendMessage(sender, text, role) {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message");
  msgDiv.classList.add(role === "user" ? "user" : "ai");

  const content = document.createElement("div");
  content.classList.add("message-content");

  content.innerHTML = `<div class="message-text">${text.replace(/\n/g, "<br/>")}</div>`;
  msgDiv.appendChild(content);
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function saveHistory(chatId, message, role, timestamp = Date.now()) {
  try {
    const payload = { chat_id: chatId, role: role, message: message, timestamp: timestamp };
    const res = await fetch("http://localhost:8003/history", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      const errText = await res.text();
      console.error("Backend error:", errText);
      return;
    }

    const data = await res.json();
    console.log("History saved:", data);

  } catch (error) {
    console.error("Failed to save history:", error);
  }
}

let historyVisible = false;

function toggleHistory() {
  historyVisible = !historyVisible;
  chatBox.innerHTML = "";  // Clear chat box

  if (historyVisible) {
    loadChatHistory();
    document.getElementById("toggle-history").innerText = "Hide History";
  } else {
    appendMessage("System", "Chat history hidden.", "system");
    document.getElementById("toggle-history").innerText = "Show History";
  }
}

// Update status badge when model changes
function updateModelBadge(model) {
  const name = model.charAt(0).toUpperCase() + model.slice(1);
  modelBadge.textContent = `Model: ${name}`;
}

// Initialize: load default model badge
updateModelBadge(document.getElementById("llm-choice").value);

// Optional: allow Enter key to send message
userInput.addEventListener("keydown", function(e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});
