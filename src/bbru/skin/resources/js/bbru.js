/**
*
* This code was developed for http://bluebream.ru by its community and
* placed under Public Domain.
*
**/

// Loading...
$(function () {
    $("#spinner").ajaxStart(
	function () {$(this).show()}
    ).ajaxStop(
	function () {$(this).hide()});
});
