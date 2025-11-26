export async function fetchUsers() {
  const r = await fetch('/api/users')
  if (!r.ok) throw new Error('Failed to fetch users')
  return r.json()
}

export async function createUser(name) {
  const r = await fetch('/api/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name })
  })
  if (r.status === 409) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Conflict'
    const err = new Error(msg)
    err.code = 409
    throw err
  }
  if (!r.ok) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Request failed'
    throw new Error(msg)
  }
  return r.json()
}

export async function login(username, password) {
  const r = await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  })
  if (!r.ok) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Login failed'
    throw new Error(msg)
  }
  return r.json()
}

export async function fetchArticles() {
  const r = await fetch('/api/articles')
  if (!r.ok) throw new Error('Failed to fetch articles')
  return r.json()
}

export async function createArticle(title, content, username) {
  const r = await fetch('/api/articles', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, content, username })
  })
  if (!r.ok) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Create article failed'
    throw new Error(msg)
  }
  return r.json()
}

export async function updateArticle(id, title, content) {
  const r = await fetch(`/api/articles/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, content })
  })
  if (!r.ok) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Update article failed'
    throw new Error(msg)
  }
  return r.json()
}

export async function deleteArticle(id) {
  const r = await fetch(`/api/articles/${id}`, { method: 'DELETE' })
  if (!r.ok) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Delete article failed'
    throw new Error(msg)
  }
  return r.json()
}

export async function fetchArticleComments(articleId) {
  const r = await fetch(`/api/articles/${articleId}/comments`)
  if (!r.ok) throw new Error('Failed to fetch comments')
  return r.json()
}

export async function addComment(articleId, content, username) {
  const r = await fetch(`/api/articles/${articleId}/comments`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ content, username })
  })
  if (!r.ok) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Add comment failed'
    throw new Error(msg)
  }
  return r.json()
}

export async function deleteComment(commentId) {
  const r = await fetch(`/api/comments/${commentId}`, { method: 'DELETE' })
  if (!r.ok) {
    const e = await r.json().catch(() => ({}))
    const msg = e && e.error ? e.error : 'Delete comment failed'
    throw new Error(msg)
  }
  return r.json()
}
