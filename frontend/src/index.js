document.addEventListener('DOMContentLoaded', function(){

    console.log('hello')

    // helper methods 
    function qs(identifier){
        return document.querySelector(identifier) 
    }
    function ce(element){
        return document.createElement(element) 
    }

    const mainbox = qs('div#mainbox')  
    function ClearMainBox(){ 
        mainbox.innerHTML = " "
    }

    if (sessionStorage.getItem('userkey') == null && sessionStorage.getItem('username') == null){
        console.log('not logged in')
        ClearMainBox() 
        LoginPage() 
    } 

    function LoginPage(){  
        const loginBox = ce('div') 
        loginBox.id = "loginbox" 

        const loginP = ce('p') 
        loginP.innerText = "LOG IN"
        loginBox.append(loginP) 

        const loginMessageSlot = ce('p') 
        loginMessageSlot.id = "login-message-slot"
        loginBox.append(loginMessageSlot)

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

        const signInButton = ce('button')
        signInButton.innerText = "Or Sign In Instead"
        signInButton.addEventListener('click', function(){
            ClearMainBox() 
            SignUpPage()
        })
        loginBox.append(signInButton)

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
                if (json.status == "Success"){
                    sessionStorage.setItem('userkey', json.username) 
                    sessionStorage.setItem('hash', json.hash) 
                    console.log(sessionStorage.getItem('userkey')) 
                } 
                else { 
                    loginMessageSlot = qs('p#login-message-slot')
                    loginMessageSlot.innerText = "Details Invalid, Please Try Again"
                    setTimeout(function(){
                        loginMessageSlot.innerText = ""
                    }, 2000) 
                } 
                event.target.querySelector('#login-username').value = ''
                event.target.querySelector('#login-password').value = ''
            })  

    }

    function SignUpPage(){
        const signUpBox = ce('div') 
        signUpBox.id = "loginbox" 
        mainbox.append(signUpBox)

        const signInP = ce('p') 
        signInP.innerText = "SIGN UP"
        signUpBox.append(signInP) 

        const signUpForm = ce('form') 
        signUpForm.id = "signup-form" 
        signUpBox.append(signUpForm)
        
        const inputUsername = ce('input') 
        inputUsername.id = "login-username"
        signUpForm.append(inputUsername)
        inputUsername.placeholder = "create a username"

        const inputLineBreak1 = ce('br') 
        signUpForm.append(inputLineBreak1)

        const inputPassword = ce('input')
        inputPassword.id = "login-password"
        signUpForm.append(inputPassword)
        inputPassword.placeholder = "create a password"
 
        const inputLineBreak2 = ce('br')
        signUpForm.append(inputLineBreak2)

        const inputPasswordCheck = ce('input')
        inputPasswordCheck.id = "login-password-check"
        signUpForm.append(inputPasswordCheck)
        inputPasswordCheck.placeholder = "type password again"
   
        const inputLineBreak3 = ce('br')
        signUpForm.append(inputLineBreak3)

        const signUpSubmit = ce('button')
        signUpSubmit.innerText = "Sign Up" 
        signUpForm.append(signUpSubmit) 

        const backToLogin = ce('button')
        backToLogin.innerText = "Back To Login"
        signUpBox.append(backToLogin)
        backToLogin.addEventListener('click', function(){
            ClearMainBox() 
            LoginPage()
        })

        signUpForm.addEventListener('submit', function(event){
            event.preventDefault() 
            console.log(event)
        })

    }




}) 