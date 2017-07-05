var slideIndex = 0;
carousel();
function carousel() {
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > x.length) {slideIndex = 1}
    x[slideIndex-1].style.display = "block";
    setTimeout(carousel, 6000); // Change image every 2 seconds
}
function myFunction(){
	setTimeout(showPage, 4000);
}
function showPage() {
	document.getElementById("loader").style.display = "none";
	document.getElementById("myDiv").style.display = "block";
}
document.getElementsByClassName("slideshow")[0].addEventListener("mouseover",show,false);
document.getElementsByClassName("slideshow")[0].addEventListener("mouseout",hide,false);
function show(){
	var k=document.getElementsByClassName("caption");
	for (i in k){
		k[i].style.display="block";
	}
}
function hide(){
	var k=document.getElementsByClassName("caption");
	for (i in k){
		k[i].style.display="none";
	}
}