async function sendMessage() {
    const msg = document.getElementById("msg").value;
    if (!msg) return;

    addMessage(msg, "user");
    document.getElementById("msg").value = "";

    const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    const data = await res.json();
    addMessage(data.response, "ai");
}

function addMessage(text, type) {
    const chat = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.className = "message " + type;
    div.innerText = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

