$(".js_feature li").mouseenter(function(){

	// handling feature formbox display
	var _id = $(this).data('link');
	$(".forms_seperate_box").hide();
	$('#'+_id).show();

	$(".preview_main_container").hide();	
	
	// handling hover effects
	$(".js_feature li").removeClass('changeable_form_hover_state');
	$(this).addClass('changeable_form_hover_state');
	
});

$("#top_title").keyup(function (e) {
    if (e.keyCode == 13) {
        var input_title = $(".input_portfolio_title_box").val();
		$(this).hide();
		$("#preview_top_title").text(input_title);
		$("#preview_top_title").show();
		// $(this).removeClass("font_middle_portfolio_publication_title");
		
    }
});

$("#preview_top_title").click(function(){
	var preview_title = $(this).text();
	$("#top_title").val(preview_title);
	$(this).hide();
	$("#top_title").show();
});

$("#top_author").keyup(function (e) {
    if (e.keyCode == 13) {
        var input_author = $(".input_portfolio_author_box").val();
		$(this).hide();
		$("#preview_top_author").text(input_author);
		$("#preview_top_author").show();
    }
});

$("#preview_top_author").click(function(){
	var preview_author = $(this).text();
	$("#top_author").val(preview_author);
	$(this).hide();
	$("#top_author").show();
});

$(".preview_button").click(function(){
	
	var whichbox = $(this).closest('div').attr('id');
 	if (whichbox == 'motivation')
	{
		// Input form var
		var parent_box = $(this).parent();
		var motivation_input_content_box = parent_box.find('.forms_content_input_box').val();
		var motivation_user_upload_image = parent_box.find('.div_right_img_container img').attr('src');
		
		// Preview form var			
		var motivation_preview_box = $('#motivation_preview');
		var motivation_preview_content = motivation_preview_box.find(".div_left_sectional_text_container_preview");
		var motivation_preview_img = motivation_preview_box.find(".div_right_img_container_preview img");
		
		// image transfer
		motivation_preview_img.attr('src',motivation_user_upload_image);
		
		// text transfer
		motivation_preview_content.text(motivation_input_content_box);	
		motivation_preview_box.show();
		parent_box.hide();
	}
	else if (whichbox == 'default_form1')
	{
		// Input form default
		var parent_box = $(this).parent();
		var input_content_box = parent_box.find('.forms_content_input_box').val();
	
		// Preview form default		
		var default_form1_preview_box = $('#default_form1_preview');
		var default_form1_preview_content = default_form1_preview_box.find(".font_middle_portfolio_publication_description_preview");
		default_form1_preview_content.text(input_content_box);
		
		default_form1_preview_box.show();
		$(".default_forms_seperate_box").hide();
	}
	else if (whichbox == 'form1')
	{
		
		// Input form var
		var parent_box = $(this).parent();
		var input_content_box = parent_box.find('.forms_content_input_box').val();
		
		// Preview form var			
		var form1_preview_box = $('#form1_preview');
		var form1_preview_content = form1_preview_box.find(".font_middle_portfolio_publication_description_preview");
		form1_preview_content.text(input_content_box);
		
		form1_preview_box.show();
		$(".changeable_form").hide();
		$(".forms_seperate_box").hide();
		
	}
	else if (whichbox == 'form2')
	{
		// Input form var
		var parent_box = $(this).parent();
		var input_title_box = parent_box.find('.font_sectional_title input').val();
		var input_content_box = parent_box.find('.forms_content_input_box').val();
		
		// Preview form var	
		var form2_preview_box = $('#form2_preview');
		var form2_preview_title = form2_preview_box.find(".font_sectional_title_preview");
		var form2_preview_content = form2_preview_box.find(".font_middle_portfolio_publication_description_preview");
		form2_preview_title.text(input_title_box);
		form2_preview_content.text(input_content_box);
		
		form2_preview_box.show();
		$(".changeable_form").hide();
		$(".forms_seperate_box").hide();
	}
	else if (whichbox=='form3')
	{
		// Input form var
		var parent_box = $(this).parent();
		var input_title_box = parent_box.find('.font_sectional_title input').val();
		var input_content_box = parent_box.find('.forms_content_input_box').val();
		var user_upload_image = parent_box.find('.div_right_img_container img').attr('src');

		// Preview form var	
		var form3_preview_box = $('#form3_preview');
		var form3_preview_title = form3_preview_box.find(".font_sectional_title_preview");
		var form3_preview_content = form3_preview_box.find(".font_middle_portfolio_publication_description_preview");
		var form3_preview_img = form3_preview_box.find(".div_right_img_container_preview img");
		form3_preview_title.text(input_title_box);
		form3_preview_content.text(input_content_box);
		form3_preview_img.attr('src', user_upload_image);

		form3_preview_box.show();
		$(".changeable_form").hide();
		$(".forms_seperate_box").hide();		
	}
	else if (whichbox=='form4')
	{
		// Input form var
		var parent_box = $(this).parent();
		var input_title_box = parent_box.find('.font_sectional_title input').val();
		var input_content_box1 = parent_box.find('#form4_content1').val();
		var input_content_box2 = parent_box.find('#form4_content2').val();
		var user_upload_image = parent_box.find('.div_right_img_container img').attr('src');
		
		// Preview form var
		var form4_preview_box = $('#form4_preview');
		var form4_preview_title = form4_preview_box.find(".font_sectional_title_preview");
		var form4_preview_content1 = form4_preview_box.find("#form4_content1");
		var form4_preview_content2 = form4_preview_box.find(".div_left_sectional_text_container_preview #form4_content2");
		var form4_preview_img = form4_preview_box.find(".div_right_img_container_preview img");

		form4_preview_title.text(input_title_box);
		form4_preview_content1.text(input_content_box1);
		form4_preview_content2.text(input_content_box2);
		form4_preview_img.attr('src', user_upload_image);

		form4_preview_box.show();
		$(".changeable_form").hide();
		$(".forms_seperate_box").hide();
	}
	else
	{
		// Input form var
		var parent_box = $(this).parent();
		var user_upload_image1 = parent_box.find('#form5_img1 img').attr('src');
		var user_upload_image2 = parent_box.find('#form5_img2 img').attr('src');
		
		// Preview form var
		var form5_preview_box = $('#form5_preview');
		var form5_preview_img1 = form5_preview_box.find("#form5_img1 img");
		var form5_preview_img2 = form5_preview_box.find("#form5_img2 img");
		form5_preview_img1.attr('src', user_upload_image1);
		form5_preview_img2.attr('src', user_upload_image2);
		
		form5_preview_box.show();
		$(".changeable_form").hide();
		$(".forms_seperate_box").hide();
	}
});

$(".edit_button").click(function(){
	var whichbox = $(this).closest('div').attr('id');
	if (whichbox == 'motivation_preview')
	{
		// extract text from original preview form
		var preview_box = $(this).parent();
		var motivation_preview_content = preview_box.find(".div_left_sectional_text_container_preview").text();
		var motivation_preview_img = preview_box.find(".div_right_img_container_preview img").attr('src');
		
		// put the text we extracted in user input form
		// so user can edit it 
		var user_input_box = $("#motivation");		
		var motivation_input_content_box = user_input_box.find('.forms_content_input_box').val(motivation_preview_content);
		var motivation_user_upload_image = user_input_box.find('.div_right_img_container img');
		motivation_user_upload_image.attr('src', motivation_preview_img);
		
		// show the user input form
		preview_box.hide();
		user_input_box.show();
	}
	else if (whichbox == 'default_form1_preview')
	{
		// extract text from original preview form
		var preview_box = $(this).parent();
		var default_form1_preview_content = preview_box.find(".font_middle_portfolio_publication_description_preview").text();
	
		// put the text we extracted in user input form
		// so user can edit it 
		var default_user_input_box = $("#default_form1");		
		var default_input_content_box = default_user_input_box.find('.forms_content_input_box').val(default_form1_preview_content);
		
		// show the user input form
		preview_box.hide();
		default_user_input_box.show();
	}
	else if (whichbox == 'form1_preview')
	{
		// extract text from original preview form
		var preview_box = $(this).parent();
		var form1_preview_content = preview_box.find(".font_middle_portfolio_publication_description_preview").text();
	
		// put the text we extracted in user input form
		// so user can edit it 
		var user_input_box = $("#form1");		
		var input_content_box = user_input_box.find('.forms_content_input_box').val(form1_preview_content);
		
		// show the user input form
		preview_box.hide();
		user_input_box.show();
		// show menu
		$('.changeable_form').show();
		
	}
	else if (whichbox == 'form2_preview')
	{
		// extract text from original preview form
		var preview_box = $(this).parent();
		var form2_preview_title = preview_box.find(".font_sectional_title_preview").text();
		var form2_preview_content = preview_box.find(".font_middle_portfolio_publication_description_preview").text();
	
		// put the text we extracted in user input form
		// so user can edit it 
		var user_input_box = $("#form2");		
		var input_title_box = user_input_box.find('.font_sectional_title').val(form2_preview_title);
		var input_content_box = user_input_box.find('.forms_content_input_box').val(form2_preview_content);
		
		
		// show the user input form
		preview_box.hide();
		user_input_box.show();
		// show menu
		$('.changeable_form').show();
	}
	else if (whichbox == 'form3_preview')
	{
		// extract text from original preview form
		var preview_box = $(this).parent();
		var form3_preview_title = preview_box.find(".font_sectional_title_preview").text();
		var form3_preview_content = preview_box.find(".font_middle_portfolio_publication_description_preview").text();
		var form3_preview_img = preview_box.find(".div_right_img_container_preview img").attr('src');
		
		// put the text we extracted in user input form
		// so user can edit it 
		var user_input_box = $("#form3");		
		var input_title_box = user_input_box.find('.font_sectional_title').val(form3_preview_title);
		var input_content_box = user_input_box.find('.forms_content_input_box').val(form3_preview_content);
		var user_upload_image = user_input_box.find('.div_right_img_container img');
		user_upload_image.attr('src', form3_preview_img);
		
		// show the user input form
		preview_box.hide();
		user_input_box.show();
		// show menu
		$('.changeable_form').show();
	}
	else if (whichbox == 'form4_preview')
	{
		// extract text from original preview form
		var preview_box = $(this).parent();
		var form4_preview_title = preview_box.find(".font_sectional_title_preview").text();
		var form4_preview_content1 = preview_box.find(".#form4_content1").text();
		var form4_preview_content2 = preview_box.find(".div_left_sectional_text_container_preview #form4_content2").text();
		var form4_preview_img = preview_box.find(".div_right_img_container_preview img").attr('src');
		
		// put the text we extracted in user input form
		// so user can edit it 
		var user_input_box = $("#form4");		
		var input_title_box = user_input_box.find('.font_sectional_title').val(form4_preview_title);
		var input_content_box1 = user_input_box.find('#form4_content1').val(form4_preview_content1);
		var input_content_box2 = user_input_box.find('#form4_content2').val(form4_preview_content2);
		var user_upload_image = user_input_box.find('.div_right_img_container img');
		user_upload_image.attr('src', form4_preview_img);
		
		// show the user input form
		preview_box.hide();
		user_input_box.show();
		// show menu
		$('.changeable_form').show();
	}
	else
	{
		// extract text from original preview form
		var preview_box = $(this).parent();
		var form5_preview_img1 = preview_box.find("#form5_img1 img").attr('src');
		var form5_preview_img2 = preview_box.find("#form5_img2 img").attr('src');
		
		// put the text we extracted in user input form
		// so user can edit it 
		var user_input_box = $("#form5");		
		var user_upload_image1 = user_input_box.find('#form5_img1 img');
		var user_upload_image2 = user_input_box.find('#form5_img2 img');
		user_upload_image1.attr('src', form5_preview_img1);
		user_upload_image2.attr('src', form5_preview_img2);
		
		// show the user input form
		preview_box.hide();
		user_input_box.show();
		// show menu
		$('.changeable_form').show();
		
	}
});

