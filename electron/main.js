
// src/main.js

const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });
  win.loadURL('http://localhost:5173');
}

function startPython() {
  const py = spawn('python', ['backend/app.py']);
  py.stdout.on('data', (data) => console.log(`[PY]: ${data}`));
  py.stderr.on('data', (data) => console.error(`[PY ERROR]: ${data}`));
}

app.whenReady().then(() => {
  startPython();
  createWindow();
});