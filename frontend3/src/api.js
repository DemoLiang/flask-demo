
export async function login(username,password){
    const res = await fetch('/api/login',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({'username':username,'password':password})
    })
    return res.json()
}

export async function fetchUsers(){
    const res = await fetch('/api/users',{
        method:'POST',
        hedaers:{
            'Content-Type':'application/json'
        },
        body:'{}'
    })
    return res.json()
}

export async function fetchArticles(){
    const res= await fetch('/api/articles',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:'{}'
    })
    return res.json()
}

export async function createArticle(title,content,username){
    const res = await fetch('/api/create_article',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({'title':title,'content':content,'username':username})
    })
    return res.json()
}
