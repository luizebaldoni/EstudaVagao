// Barra de Navegação
// ---------Responsive-navbar-active-animation-----------
$(function(){
	var n= "#nav";
	var no = ".nav-items";
	$(n).click(function(){
	   if($(no).hasClass("nav-open")){
		 $(no).animate({height:0},300);
			 setTimeout(function(){
		  $(no).removeAttr('style').removeClass("nav-open");
		 },320);
	   }else{
		 var h = $(no).css("height","auto").height();
		 $(no).height(0).animate({height:h},300);
		 setTimeout(function(){
		  $(no).removeAttr('style').addClass("nav-open");
		 },320);
	   }
	});
  });

// --------------add active class-on another-page move----------
jQuery(document).ready(function($){
	// Get current path and find target link
	var path = window.location.pathname.split("/").pop();
	// Account for home page with empty path
	if ( path == '' ) {
		path = 'index.html';
	}
	var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');
	// Add active class to target link
	target.parent().addClass('active');
});
function hideIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:none;");
    navigation.classList.remove("hide");
}

function showIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:block;");
    navigation.classList.add("hide");
}

// Comentários
function showComment(){
    var commentArea = document.getElementById("comment-area");
    commentArea.classList.remove("hide");
}

// Respostas
function showReplies(id){
    var replyArea = document.getElementById(id);
    replyArea.classList.remove("hide");
}
