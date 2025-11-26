export async function login(username,password){
    const response = await fetch('/api/login',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body: JSON.stringify({"username":username,"password":password})
    })
    console.log( response)
    return response.json()
}


export async function fetchUsers(){
    const response = await fetch('/api/users',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:'{}'
    })
    return response.json()
}

export async function fetchArticles(){
    const res = await fetch('/api/articles',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:'{}'
    })
    return res.json()
}
