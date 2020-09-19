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
        LoginPage()
    } 

    function LoginPage(){









}) 