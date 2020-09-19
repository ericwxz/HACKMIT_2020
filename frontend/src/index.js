document.addEventListener('DOMContentLoaded', function(){

    console.log('hello')

    // helper methods 
    function qs(identifier){
        return document.querySelector(identifier) 
    }
    function ce(element){
        return document.createElement(element) 
    }



    if (sessionStorage.getItem('userkey') == null && sessionStorage.getItem('username') == null){
        console.log('not logged in')
        LoginPage()
    } 


    function LoginPage(){  
        const mainbox = qs('div#mainbox')        
        const loginBox = ce('div') 
        loginBox.id = "loginbox" 

        const loginP = ce('p') 
        loginP.innerText = "LOG IN"
        loginBox.append(loginP) 

        const loginForm = ce('form') 
        loginForm.id = "login-form" 
        
        const inputUsername = ce('input') 
        inputUsername.id = "login-username"
        loginForm.append(inputUsername)
        inputUsername.placeholder = "username"

        const inputLineBreak1 = ce('br')
        loginForm.append(inputLineBreak1)

        const inputPassword = ce('input')
        inputPassword.id = "login-password"
        loginForm.append(inputPassword)
        inputPassword.placeholder = "password"
 
        const inputLineBreak2 = ce('br')
        loginForm.append(inputLineBreak2)

        const loginSubmit = ce('button')
        loginSubmit.innerText = "Log In" 
        loginForm.append(loginSubmit)

        loginBox.append(loginForm) 
        loginForm.addEventListener('submit', function(event){
            console.log(event) 
            event.preventDefault()
            LogIn(event) 
        }) 

        mainbox.append(loginBox)
    } 

    function LogIn(event){
        console.log(event.target)
        console.log(event.target.querySelector('#login-username').value) 
        console.log(event.target.querySelector('#login-password').value) 

        const configObj = { 
            method: 'POST', 
            headers: { 
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }, 
            body: JSON.stringify({
                username: event.target.querySelector('#login-username').value, 
                password: event.target.querySelector('#login-password').value
            })
        }

        fetch('http://localhost:3000/users/login', configObj)
            .then(res => res.json())
            .then(json => {
                if (json.message == "Success"){
                    sessionStorage.setItem('userkey', json.message.split(" ")[1]) 
                    sessionStorage.setItem('username', json.message.split(" ")[2])
                    console.log(sessionStorage.getItem('userkey')) 

                    coverUpLogin(json.message) 
                    textPage("1.1") 
                } 
                else {
                    user_message_slot.innerText = json.message
                    setTimeout(function(){
                        user_message_slot.innerText = ""
                    }, 2000) 
                } 
                event.target.querySelector('#login-username').value = ''
                event.target.querySelector('#login-password').value = ''
            })  

    }





}) 