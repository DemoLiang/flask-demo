
export async function login(username,password){
    const res = await fetch('/api/login',{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({'username':username,'password':password})
    })

    return res.json()
}

export async function fetchUsers(){
    const res = await fetch('/api/users',{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:'{}'
    })
    return res.json()
}

export async function createUser(username,password){
    const res = await fetch('/api/add_user',{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({"username":username,"password":password})
    })
    return res.json()
}