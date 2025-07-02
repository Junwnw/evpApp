export async function loginAPI(username, password) {
  const res = await fetch('http://localhost:5000/login', {
    method: 'POST',
    body: JSON.stringify({ username, password }),
    headers: { 'Content-Type': 'application/json' }
  })
  return res.json()
}