const API_BASE = "http://127.0.0.1:8000";
const token = localStorage.getItem("access_token");


if (!token) {
  window.location.href = "index.html";
}



window.onload = loadFiles;

async function loadFiles() {
  const res = await fetch(`${API_BASE}/files`, {
    headers: { Authorization: `Bearer ${token}` }
  });

  const files = await res.json();
  fileList.innerHTML = "";

  files.forEach(f => {
    const div = document.createElement("div");
    div.className = "file-card";
    div.innerHTML = `
      <span>${f.filename}</span>
      <span>
        <a href="${API_BASE}${f.url}" target="_blank">View</a>
        <button onclick="deleteFile(${f.id})">Delete</button>
      </span>
    `;
    fileList.appendChild(div);
  });
}

async function uploadFile() {
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  await fetch(`${API_BASE}/files/upload`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
    body: formData
  });

  loadFiles();
}

async function deleteFile(id) {
  await fetch(`${API_BASE}/files/${id}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` }
  });

  loadFiles();
}



function logout() {
  localStorage.removeItem("access_token");
  window.location.replace("./index.html");
}
