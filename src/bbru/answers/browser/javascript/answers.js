/**
*
* This code was developed for http://bluebream.ru by its community and
* placed under Public Domain.
*
**/ 

function get_form_params (submit) {
    var form = $(submit).parents('form')[0];
    var params = $(form).serialize();
    return params.concat('&' + submit.name + '=' + submit.value);
}

function load_answers_listing (context_url) {
    $('#answers-place').load(context_url + "@@answers");
}

function load_answer_form (context_url, params) {
    var url = context_url + "@@answer";

    $('#form-place').load(url, params, function(text, status, response) {
	if (response.status == 202) {
	    $('#form-place').empty();
	    load_answers_listing(context_url);
	}

	$('input.cancel-button').click(function() {
	    $('#form-place').empty();
	    return false;
	});

	$('form.answer input:submit').click(function() {
	    load_answer_form(context_url, get_form_params(this));
	    return false;
	});
    });
}

function load_title_form (context_url) {
    var url = context_url + "@@title";
    
    $('#form-place').load(url, {}, function() {
	
	$('input.cancel-button').click(function() {
	    $('#form-place').empty();
	    return false;
	});
	
	$('form.title input:submit').click(function() {
	    $('#form-place').load(url, get_form_params(this), function(text) {
		
		$('#question-title').text(text);
		$('#form-place').empty();
	    });
	    
	    return false;
	});
    });
}

function load_text_form (context_url, params) {
    var url = context_url + "@@text";

    $('#form-place').load(url, params, function(text, status, response) {

	if (response.status == 202) {
	    $('#question-body').html(text);
	    $('#form-place').empty();
	}

	$('input.cancel-button').click(function() {
	    $('#form-place').empty();
	    return false;
	});

	$('form.text input:submit').click(function() {
	    load_text_form(context_url, get_form_params(this));
	    return false;
	});
    });
}

function question_init (context_url) {
    load_answers_listing(context_url);

    $('#do-answer').click(function() {
	load_answer_form(context_url);
	return false;
    });

    $('#set-title').click(function() {
	load_title_form(context_url);
	return false;
    });

    $('#edit-text').click(function() {
	load_text_form(context_url, {});
	return false;
    });
}

