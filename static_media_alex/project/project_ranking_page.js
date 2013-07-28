$('#portfolio_tabs_bar').tabs();

// Projects: hover color change
$('.div_portfolio_rank_frame').mouseenter(function(){
	
	if ( $('.img_arrow_display_size', this).attr('src') != '/static_media_alex/Images/like_button_hover.jpg'){
		$('.img_arrow_display_size', this).attr('src', '/static_media_alex/Images/like_button_ori.jpg');	
	}
	$(this).css('background-color','#CFECEC');
});
$('.div_portfolio_rank_frame').mouseleave(function(){
	$(this).css('background-color','white');
	$(this).css('border','0px solid #2F6AB3');
	$(this).css('border-bottom','1px solid #C0C0C0');

	$('.img_arrow_display_size', this).attr('src', '/static_media_alex/Images/like_button.jpg');			
});




// Like: hover size change
$('.img_arrow_display_size').mouseenter(function(){
	$(this).attr('src', '/static_media_alex/Images/like_button_hover.jpg')		
	$(this).css('width','35px');
	$(this).css('height','35px');	
});

$('.img_arrow_display_size').mouseleave(function(){
	$(this).attr('src', '/static_media_alex/Images/like_button_ori.jpg')
	$(this).css('width','30px');
	$(this).css('height','30px');
});

// Like: click size change + trigger votes
$('.img_arrow_display_size').click(function(){
	var current_page = $(this).attr('data-click');
	$.get("/projects/voting_project", {current_page_url: current_page}, function(data){
		//alert(data)
		// should I provide user feedback
	});

	$(this).css('width','35px');
	$(this).css('height','35px');
	$(this).fadeOut()
	return false
});



$("#select_ranking").change(function () 
{
	var str = "";
	/* Handy Code: We need to put this in documentation
				$("#portfolio_tabs_frame").empty();
				var content = $("#portfolio_rank_frame6").html();
				var content2 = $("#font_portfolio_rank_number3").html();
				$("#portfolio_rank_frame4").html(content);
				$("#font_portfolio_rank_number6").html(content2);
	*/
	
	$("select option:selected").each(function () {
		if ($(this).text() == 'Best'){

			var url = document.URL;
			var urlsplit = url.split('/');
			var username = urlsplit[url.split('/').length-3];

			// request calculate ranking
			var filter_opt = $(this).text();

			$.get("/"+username+"/projects/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
				
				// sort the rank according to the new list
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");										
					$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}																		
			});	
								
		}


		if ($(this).text() == 'Recommend For You'){

			var url = document.URL;
			var urlsplit = url.split('/');
			var username = urlsplit[url.split('/').length-3];

			// request calculate ranking
			var filter_opt = $(this).text();

			$.get("/"+username+"/project/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
				
				// sort the rank according to the new list
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");										
					$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}																		
			});	
								
		}
		
		if ($(this).text() == 'Most Recent'){
			
			var url = document.URL;
			var urlsplit = url.split('/');
			var username = urlsplit[url.split('/').length-3];
			
			// request calculate ranking
			var filter_opt = $(this).text();
			$.get("/"+username+"/projects/rankfilter", {filter_option: filter_opt}, function(data){
				
				var organized = JSON.parse(data);
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");					
					//$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}
				
			});									
		}


		if ($(this).text() == 'Less Recent'){
			
			var url = document.URL;
			var urlsplit = url.split('/');
			var username = urlsplit[url.split('/').length-3];
			
			// request calculate ranking
			var filter_opt = $(this).text();
			$.get("/"+username+"/projects/rankfilter", {filter_option: filter_opt}, function(data){
				
				var organized = JSON.parse(data);
				// store all the proj in an array
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");					
					//$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}
				
			});									
		}
		
		
		
	});
})
.change();
