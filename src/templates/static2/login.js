var pageInitialized = false;
$(document).ready(function(){
    if(pageInitialized) return;
    pageInitialized=true;
    init();
    addFunctions();
});
function init(){
    if (localStorage.getItem("token-user")  !== null){
	userLoged();
    }else{
	//	userAnon();
	//clear();
    }
}
function userLoged(){
    location.reload(); 
}
function addFunctions(){
    $('#entrar').click(function(){
	let email = $('#email').val();
	

    });

}
