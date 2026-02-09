// ================= CONFIG =================
const BACKEND_URL = "http://127.0.0.1:8000"; 
// For deployment, change to:
// const BACKEND_URL = "https://your-backend-name.onrender.com";

// ================= DOM ELEMENTS =================
const chatContainer = document.getElementById("chatContainer");
const status = document.getElementById("uploadStatus");
const fileInput = document.getElementById("pdfFile");
const fileNameDisplay = document.getElementById("fileNameDisplay");

// ================= STATE =================
let selectedFile = null;

// ================= ON LOAD =================
window.addEventListener("load", () => {
  const savedName = sessionStorage.getItem("uploadedFileName");
  if (savedName) {
    fileNameDisplay.innerText = savedName;
  }
});

// ================= FILE SELECTION =================
fileInput.addEventListener("change", () => {
  if (fileInput.files && fileInput.files.length > 0) {
    selectedFile = fileInput.files[0];
    fileNameDisplay.innerText = selectedFile.name;
    sessionStorage.setItem("uploadedFileName", selectedFile.name);
  } else {
    selectedFile = null;
    fileNameDisplay.innerText = "No file selected";
    sessionStorage.removeItem("uploadedFileName");
  }
});

// ================= CHAT UI =================
function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.classList.add("message", sender);
  msg.innerText = text;
  chatContainer.appendChild(msg);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

// ================= UPLOAD PDF =================
async function uploadPDF(event) {
  if (event) event.preventDefault();

  if (!selectedFile && fileInput.files.length > 0) {
    selectedFile = fileInput.files[0];
  }

  if (!selectedFile) {
    status.innerText = "⚠️ Please select a PDF file first.";
    status.style.color = "#ef4444";
    return;
  }

  if (selectedFile.type !== "application/pdf") {
    status.innerText = "❌ Only PDF files are allowed.";
    status.style.color = "#ef4444";
    return;
  }

  const formData = new FormData();
  formData.append("file", selectedFile);

  status.innerText = "⏳ Processing document...";
  status.style.color = "#6366f1";

  try {
    const response = await fetch(`${BACKEND_URL}/upload`, {
      method: "POST",
      body: formData
    });

    const text = await response.text();

    if (!response.ok) {
      console.error("Upload failed:", text);
      status.innerText = "❌ Upload failed. See console.";
      status.style.color = "#ef4444";
      return;
    }

    const data = JSON.parse(text);

    status.innerText = "✅ " + (data.message || "PDF processed successfully.");
    status.style.color = "#10b981";

    chatContainer.innerHTML = "";
    addMessage("The document is ready. Ask me anything about it.", "bot");

    const savedName = sessionStorage.getItem("uploadedFileName");
    fileNameDisplay.innerText = savedName || selectedFile.name;

  } catch (err) {
    console.error("Network error:", err);
    status.innerText = "❌ Could not connect to backend.";
    status.style.color = "#ef4444";
  }
}

// ================= ASK QUESTION (FIXED) =================
async function askQuestion() {
  const input = document.getElementById("questionInput");
  const question = input.value.trim();

  if (!question) return;

  addMessage(question, "user");
  input.value = "";

  const typing = document.createElement("div");
  typing.classList.add("message", "bot");
  typing.style.opacity = "0.6";
  typing.innerText = "Thinking...";
  chatContainer.appendChild(typing);
  chatContainer.scrollTop = chatContainer.scrollHeight;

  try {
    const response = await fetch(`${BACKEND_URL}/ask`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question: question
      })
    });

    const text = await response.text();

    if (typing.parentNode) {
      chatContainer.removeChild(typing);
    }

    if (!response.ok) {
      console.error("Ask failed:", text);
      addMessage("❌ Error getting answer.", "bot");
      return;
    }

    const data = JSON.parse(text);
    addMessage(
      data.answer || "I couldn't find an answer in the document.",
      "bot"
    );

  } catch (err) {
    console.error("Ask error:", err);
    if (typing.parentNode) {
      chatContainer.removeChild(typing);
    }
    addMessage("❌ Backend unreachable.", "bot");
  }
}