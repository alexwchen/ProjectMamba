$('document').ready(function(){
	var url = document.URL;
	var urlsplit = url.split('/');
		
	for (i=0;i<urlsplit.length;i++)
	{
		var str = urlsplit[i];
		if (str=="contact")
		{
			$('#contact').attr('class','a_top_menu_selected_link')
			$('#publication').attr('class','a_top_menu_link')
			$('#resume').attr('class','a_top_menu_link')
			$('#projects').attr('class','a_top_menu_link')			
			break;
		}
		else if(str=="project")
		{
			$('#contact').attr('class','a_top_menu_link')
			$('#publication').attr('class','a_top_menu_link')
			$('#resume').attr('class','a_top_menu_link')
			$('#projects').attr('class','a_top_menu_selected_link')
			break;
		}
		else if(str=="resume")
		{
			$('#contact').attr('class','a_top_menu_link')
			$('#publication').attr('class','a_top_menu_link')
			$('#resume').attr('class','a_top_menu_selected_link')
			$('#projects').attr('class','a_top_menu_link')
			break;
		}
		else if(str=="publication")
		{
			$('#contact').attr('class','a_top_menu_link')
			$('#publication').attr('class','a_top_menu_selected_link')
			$('#resume').attr('class','a_top_menu_link')
			$('#projects').attr('class','a_top_menu_link')
			break;
		}
		
	}
	
});
