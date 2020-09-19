document.addEventListener('DOMContentLoaded', function(){

console.log('hello')

if (sessionStorage.getItem('userkey') != null && sessionStorage.getItem('username') != null){
    coverUpLogin("LoggedInAt " + sessionStorage.getItem('userkey') + " " + sessionStorage.getItem('username'))
}








}) 