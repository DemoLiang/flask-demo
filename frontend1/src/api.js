export async function fetchUsers(){
    const r = await fetch('/api/users')
    return r.json()
}


export async function createUser(name) {
    const r = await fetch('/api/users',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:Json.stringify({name})
    })
    return r.json()
}

export async function login(username ,password){
    console.log('login',username,password)
    const r = await fetch('/api/login',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify({"username":username,"password":password})
    })
    if (r.status!==200){
        throw new Error('Invalid username or password')
    }
    return r.json()
}
