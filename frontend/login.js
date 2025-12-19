const API_BASE = "http://127.0.0.1:8000";
let mode = "login";

// already logged in → dashboard
if (localStorage.getItem("access_token")) {
  window.location.href = "dashboard.html";
}

function switchMode() {
  const title = document.getElementById("title");
  const btn = document.getElementById("actionBtn");
  const switchText = document.getElementById("switchText");
  const error = document.getElementById("error");
  const success = document.getElementById("success");

  error.textContent = "";
  success.textContent = "";

  if (mode === "login") {
    mode = "signup";
    title.textContent = "Sign Up";
    btn.textContent = "Create Account";
    btn.onclick = signup;
    switchText.textContent = "Already have an account? Login";
  } else {
    mode = "login";
    title.textContent = "Login";
    btn.textContent = "Log In";
    btn.onclick = login;
    switchText.textContent = "Create new account";
  }
}

async function signup() {
  const email = emailInput().value.trim();
  const password = passwordInput().value.trim();
  const error = document.getElementById("error");
  const success = document.getElementById("success");

  error.textContent = "";
  success.textContent = "";

  const res = await fetch(`${API_BASE}/auth/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();
  if (!res.ok) return error.textContent = data.detail;

  success.textContent = "Signup successful! Please login.";
  switchMode();
}

async function login() {
  const email = emailInput().value.trim();
  const password = passwordInput().value.trim();
  const error = document.getElementById("error");

  error.textContent = "";

  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();
  if (!res.ok) return error.textContent = data.detail;

  localStorage.setItem("access_token", data.access_token);
  window.location.href = "dashboard.html";
}

function emailInput() {
  return document.getElementById("email");
}

function passwordInput() {
  return document.getElementById("password");
}
