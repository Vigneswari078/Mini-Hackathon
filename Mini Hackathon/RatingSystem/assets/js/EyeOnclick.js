var state= false;
function viewPassword(){
    if(state){
        document.getElementById("pass").setAttribute("type","text");
        document.getElementById("eye").className="fa fa-eye-slash";
        state=false;
    }
    else{
        document.getElementById("pass").setAttribute("type","password");
        document.getElementById("eye").className="fa fa-eye";
        state=true;
    }
}