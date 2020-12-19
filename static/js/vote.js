$('.js-vote').click(function(ev) {
	ev.preventDefault();
	var $this = $(this),
		action = $this.data('action'),
		object_type = $this.data('type'),
		object_id = $this.data('oid');

	$.ajax('/vote/', {
		method: 'POST',
		data: {
			action: action,
			object_type: object_type,
			object_id: object_id,
		},
	}).done(function(data) {
		new_rating = data['object_rating'];
		console.log("SERVER RESPONSE: new rating is " + new_rating);

		// обновляем поле rating актуальным значением
		rating_element_id = object_type + "-rating-qid-" + object_id;
		$('#' + rating_element_id).text(new_rating);

		// переставляем активность кнопки
		upvote_element_id = object_type + "-upvote-btn-qid-" + object_id;
		downvote_element_id = object_type + "-downvote-btn-qid-" + object_id;
		$('#' + upvote_element_id).toggleClass('js-vote-inactive');
		$('#' + downvote_element_id).toggleClass('js-vote-inactive');
	});
	console.log("CLIENT:" + action +  " - " + object_type + " - " + object_id);
});
