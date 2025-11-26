
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

export async function updateArticle(id,title,content,username){
    const res = await fetch('/api/update_article',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({'id':id,'title':title,'content':content,'username':username})
    })
}

export async function deleteArticle(id){
    const res = await fetch('/api/delete_article',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({'id':id})
    })
    return res.json()
}

export async function fetchComments(article_id){
    const res = await fetch('/api/comments',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'article_id':article_id})
    })
    return res.json()
}

export async function createComment(article_id,content,username){
    const res = await fetch('/api/create_comment',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'article_id':article_id,'username':username,'content':content})
    })
    return res.json()
}