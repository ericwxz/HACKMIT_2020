document.addEventListener('DOMContentLoaded', function(){

    console.log('Hello World')
    const mainbox = qs('div#mainbox')  

    // DEFINITIONS 
    const dashboardTab = qs('span#page-dashboard')
    const requestsTab = qs('span#page-requests')
    const analyticsTab = qs('span#page-analytics')
    const storiesTab = qs('span#page-stories')

    // EXPERIMENT 
    sessionStorage.setItem('userkey', 123) 
    sessionStorage.setItem('username', 'alexis') 

    // sessionStorage.removeItem('userkey')
    // sessionStorage.removeItem('userkey')

    // INITIAL CHECK IF LOGGED IN ON PAGE LOAD 
    if (sessionStorage.getItem('userkey') == null && sessionStorage.getItem('username') == null){
        console.log('not logged in')
        ClearMainBox() 
        LoginPage() 
    } 
    else {
        console.log(sessionStorage.getItem('userkey'))
        Dashboard() 
    }

    dashboardTab.addEventListener('click', function(){
        if (sessionStorage.getItem('userkey') != null && sessionStorage.getItem('username') != null) {
            Dashboard() 
        } else{
            LoginPage() 
        }
    })

    requestsTab.addEventListener('click', function(){
        if (sessionStorage.getItem('userkey') != null && sessionStorage.getItem('username') != null) {
            Requests() 
        } else{
            LoginPage() 
        }
    })

    analyticsTab.addEventListener('click', function(){
        Analytics() 
    })

    storiesTab.addEventListener('click', function(){
        Stories() 
    }) 

}) 


// HELPER METHODS 
function qs(identifier){
    return document.querySelector(identifier) 
}
function ce(element){
    return document.createElement(element) 
}
function ClearMainBox(){ 
    mainbox.innerHTML = " "
}





// LOGGING IN 

function LoginPage(){  
    ClearMainBox() 
    const loginBox = ce('div') 
    loginBox.id = "loginbox" 

    const loginP = ce('p') 
    loginP.id = "login-p"
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
    inputUsername.placeholder = "Username"

    const inputLineBreak1 = ce('br') 
    loginForm.append(inputLineBreak1)

    const inputPassword = ce('input')
    inputPassword.type = 'password'
    inputPassword.id = "login-password"
    loginForm.append(inputPassword)
    inputPassword.placeholder = "Password"

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
                Dashboard() 
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




// SIGNING UP 

function SignUpPage(){
    ClearMainBox() 
    const signUpBox = ce('div') 
    signUpBox.id = "loginbox" 
    mainbox.append(signUpBox)

    const signInP = ce('p') 
    signInP.innerText = "SIGN UP"
    signUpBox.append(signInP) 

    const signUpMessageSlot = ce('p')
    signUpBox.append(signUpMessageSlot)

    const signUpForm = ce('form') 
    signUpForm.id = "signup-form" 
    signUpBox.append(signUpForm)
    
    const inputUsername = ce('input') 
    inputUsername.id = "signup-username"
    signUpForm.append(inputUsername)
    inputUsername.placeholder = "Username"

    const inputLineBreak1 = ce('br') 
    signUpForm.append(inputLineBreak1)

    const inputPassword = ce('input')
    inputPassword.type = 'password'
    inputPassword.id = "signup-password"
    signUpForm.append(inputPassword)
    inputPassword.placeholder = "Password"

    const inputLineBreak2 = ce('br')
    signUpForm.append(inputLineBreak2)

    const inputPasswordCheck = ce('input')
    inputPasswordCheck.type = 'password' 
    inputPasswordCheck.id = "signup-passwordcheck"
    signUpForm.append(inputPasswordCheck)
    inputPasswordCheck.placeholder = "Repeat Password"

    const inputLineBreak3 = ce('br')
    signUpForm.append(inputLineBreak3)

    const inputLineBreak7 = ce('br')
    signUpForm.append(inputLineBreak7)

    const inputState = ce('input')
    inputState.id = 'signup-loc-state' 
    inputState.placeholder = "State" 
    signUpForm.append(inputState)

    const inputLineBreak4 = ce('br')
    signUpForm.append(inputLineBreak4)

    const inputCity = ce('input')
    inputCity.id = 'signup-loc-city' 
    inputCity.placeholder = "City" 
    signUpForm.append(inputCity)

    const inputLineBreak5 = ce('br')
    signUpForm.append(inputLineBreak5)

    const inputZipCode = ce('input')
    inputZipCode.type = 'number' 
    inputZipCode.id = "signup-loc-zipcode"
    inputZipCode.placeholder = "Zip Code"
    signUpForm.append(inputZipCode)

    const inputLineBreak6 = ce('br')
    signUpForm.append(inputLineBreak6)

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
        SignUp(event) 
    })

}

function SignUp(event){
    console.log(event.target)
    console.log(event.target.querySelector('#signup-username').value) 
    console.log(event.target.querySelector('#signup-password').value) 
    console.log(event.target.querySelector('#signup-passwordcheck').value) 
    console.log(event.target.querySelector('#signup-loc-state').value) 
    console.log(event.target.querySelector('#signup-loc-city').value) 
    console.log(event.target.querySelector('#signup-loc-zipcode').value) 

    const configObj = { 
        method: 'POST', 
        headers: { 
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }, 
        body: JSON.stringify({
            username: event.target.querySelector('#signup-username').value, 
            password: event.target.querySelector('#signup-password').value, 
            passwordcheck: event.target.querySelector('#signup-passwordcheck').value,
            locationstate: event.target.querySelector('#signup-loc-state').value, 
            locationcity: event.target.querySelector('#signup-loc-city').value, 
            locationzipcode: event.target.querySelector('#signup-loc-zipcode').value
        }) 
    } 

    fetch('http://localhost:3000/users/signup', configObj)
        .then(res => res.json()) 
        .then(json => { 
            if (json.status == "Success"){
                sessionStorage.setItem('userkey', json.username) 
                sessionStorage.setItem('hash', json.hash) 
                console.log(sessionStorage.getItem('userkey')) 
                LoginPage() 
            } 
            else { 
                signUpMessageSlot = qs('p#signup-message-slot')
                signUpMessageSlot.innerText = "Details Invalid, Please Try Again"
                setTimeout(function(){ 
                    signUpMessageSlot.innerText = ""
                }, 2000) 
            } 
            event.target.querySelector('#signup-username').value = ''
            event.target.querySelector('#signup-password').value = ''
            event.target.querySelector('#signup-passwordcheck').value = ''
            event.target.querySelector('#signup-loc-state').value = ''
            event.target.querySelector('#signup-loc-city').value = ''
            event.target.querySelector('#signup-loc-zipcode').value = ''
        })  

}






// DASHBOARD 

function Dashboard(){
    ClearMainBox() 
    console.log('yo, dashboard')

    // Set up split screen -- > 
    splitRight = ce('div')
    splitRight.id = "splitright"
    mainbox.append(splitRight)

    splitLeft = ce('div')
    splitLeft.id = "splitleft"
    mainbox.append(splitLeft)
    // End of set up split screen -- > 


    // Profile -- >
    profileBox = ce('div')
    profileBox.className = 'floathalfbox'
    splitLeft.append(profileBox)

    

    profileTitle = ce('p')
    profileTitle.className = 'floathalfbox-title'  
    profileTitle.innerText = "Welcome"
    profileBox.append(profileTitle) 
    // End of profile -- > 



    // Create a New Request Box -- >  
    createQuestBox = ce('div') 
    createQuestBox.className = 'floathalfbox'
    splitRight.append(createQuestBox)
    
    createQuestTitle = ce('p')
    createQuestTitle.className = 'floathalfbox-title'  
    createQuestTitle.innerText = "Create a Request"
    createQuestBox.append(createQuestTitle) 

    createQuestSubtitle = ce('p')
    createQuestSubtitle.className = 'floathalfbox-subtitle'
    createQuestSubtitle.innerText = "Help is only 6 feet away" 
    createQuestBox.append(createQuestSubtitle)

    createQuestForm = ce('form') 
    createQuestBox.append(createQuestForm)

    createQuestInputTitle = ce('input')
    createQuestInputTitle.id = "createquest-title" 
    createQuestInputTitle.placeholder = "Title"
    createQuestForm.append(createQuestInputTitle)

    createQuestInputCat = ce('select')
    createQuestInputCat.id = "createquest-cat" 
    createQuestForm.append(createQuestInputCat)

    createQuestInputCatRemote = ce('option')
    createQuestInputCatRemote.value = "Remote" 
    createQuestInputCatRemote.innerText = "Remote" 
    createQuestInputCat.append(createQuestInputCatRemote)

    createQuestInputCatErrand = ce('option')
    createQuestInputCatErrand.value = "Errand" 
    createQuestInputCatErrand.innerText = "Errand" 
    createQuestInputCat.append(createQuestInputCatErrand)

    createQuestInputCatMisc = ce('option')
    createQuestInputCatMisc.value = "Miscellaneous" 
    createQuestInputCatMisc.innerText = "Miscellaneous" 
    createQuestInputCat.append(createQuestInputCatMisc)

    createQuestInputCatSocial = ce('option')
    createQuestInputCatSocial.value = "Social" 
    createQuestInputCatSocial.innerText = "Social" 
    createQuestInputCat.append(createQuestInputCatSocial)
    
    createQuestInputTime= ce('input') 
    createQuestInputTime.type = "number"
    createQuestInputTime.placeholder = "Time Frame (minutes)"
    createQuestInputTime.id = "createquest-time" 
    createQuestForm.append(createQuestInputTime)


    createQuestInputDescription = ce('textarea') 
    createQuestInputDescription.id = "createquest-desc" 
    createQuestInputDescription.placeholder = "Details" 
    createQuestForm.append(createQuestInputDescription) 

    createQuestInputSubmit = ce('button')
    createQuestInputSubmit.id = "createquest-submit"
    createQuestInputSubmit.innerText = "Create"
    createQuestForm.append(createQuestInputSubmit)

    createQuestForm.addEventListener('submit', function(event){
        event.preventDefault()
        CreateQuest(event) 
    })

    // End of create a New Request Box -- > 

}

function CreateQuest(event) {
    console.log(event.target)
}




function Requests(){
    ClearMainBox() 
    console.log('yo, requests')
}

function Analytics(){
    ClearMainBox() 
    console.log('yo, analytics')
}

function Stories(){ 
    ClearMainBox() 
    console.log('yo, stories')
}



