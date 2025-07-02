export async function crawlAPI(keyword) {
    const res = await fetch('http://localhost:5000/crawl', {
      method: 'POST',
      body: JSON.stringify({ keyword }),
      headers: { 'Content-Type': 'application/json' }
    })
  
    if (!res.ok) throw new Error('请求失败')
    return await res.json()
  }
  