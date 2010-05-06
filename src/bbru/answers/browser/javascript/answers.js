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
    $('#answers-place').load(context_url + "@@listing", {}, answer_init);
}

function load_answer_form (context_url, params) {
    var url = context_url + "@@add";

    $('#form-place').load(url, params, function(text, status, response) {
	if (response.status == 202) {
	    $('#form-place').empty();
	    load_answers_listing(context_url);
	}

	$('form input.cancel-button').click(function() {
	    $('#form-place').empty();
	    return false;
	});

	$('form input:submit').click(function() {
	    load_answer_form(context_url, get_form_params(this));
	    return false;
	});
    });
}

function load_title_form (context_url) {
    var url = context_url + "@@title";

    $.post(url, {}, function(data) {

	var container = $('#form-place');
	container.append(data);

	$('form input.cancel-button', container).click(function() {
	    container.empty();
	    return false;
	});
	
	$('form input:submit', container).click(function() {
	    $.post(url, get_form_params(this), function(data) {
		var title = $('.title', data).val();
		$('#question-title').text(title);
		$('#form-place').empty();
	    });
	    return false;
	});
    });
}

function load_edit_question_form (context_url, params) {
    var url = context_url + "@@edit";

    $.post(url, params, function(data) {

	var container = $('#form-place');

	if ( $('.status', data).text() == "Data successfully updated.") {
	    var body = $('textarea', data).text();
	    $('#question-body').html(body);
	    container.empty();
	    return;
	}

	container.append(data);

	$('form input.cancel-button', container).click(function() {
	    container.empty();
	    return false;
	});

	$('form input:submit', container).click(function() {
	    load_edit_question_form(context_url, get_form_params(this));
	    return false;
	});
    });
}

function load_edit_answer_form(anchor, params) {
    var place = $(anchor).parents('.answer-wrapper');
    var context_url = $('div.context_url', place).text();
    var question_url = $('.question .metadata .context_url').text();

    $.post(context_url + "/@@edit", params, function(data) {

	if ( $('.status', data).text() == "Data successfully updated.") {
	    load_answers_listing(question_url);
	    return;
	}

	var container = $('<div></div>');
	container.append(data);
	place.after(container);

	$('form input:submit', container).click(function() {
	    container.remove();
	    load_edit_answer_form(anchor, get_form_params(this));
	    return false;
	});

	$('form input.cancel-button', container).click(function() {
	    container.remove();
	    return false;
	});

    });

}

function load_delete_answer_form(anchor) {
    var place = $(anchor).parents('.answer-wrapper');
    var context_url = $('div.context_url', place).text();
    var question_url = $('.question .metadata .context_url').text();

    $.post(context_url + "/@@delete", {}, function(data) {

	var container = $('<div></div>');
	container.append(data);
	place.after(container);

	$('#form-buttons-delete', container).click(function() {
	    $.post(context_url + "/@@delete", get_form_params(this), function () {
		load_answers_listing(question_url);
	    });
	    return false;
	});

	$('#form-buttons-cancel', container).click(function() {
	    container.remove();
	    return false;
	});
    });
}

function question_init (context_url) {
    load_answers_listing(context_url);

    $('.do-answer').click(function() {
	load_answer_form(context_url);
	return false;
    });

    $('.set-title').click(function() {
	load_title_form(context_url);
	return false;
    });

    $('.edit-question').click(function() {
	load_edit_question_form(context_url, {});
	return false;
    });
}

function answer_init () {
    $('.edit-answer').click(function() {
	load_edit_answer_form(this, {});
	return false;
    });

    $('.delete-answer').click(function() {
	load_delete_answer_form(this);
	return false;
    });
}
