$('#portfolio_tabs_bar').tabs();

// Projects: hover color change
$('.div_picture_small_frame').mouseenter(function(){
	$(this).css('border-color','#2F6AB3');
	$(this).css('cursor','pointer');		
});
$('.div_picture_small_frame').mouseleave(function(){
	$(this).css('border-color','silver');
});
