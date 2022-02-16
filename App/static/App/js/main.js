function complete_test(id)
{
  $.ajax({
    url: '/test/'+id,
    type: 'post',
    data: $('#test_form').serialize() + '&action=complete_test',
    success: function(responce){
      window.location = '/result/'+responce.id
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function run_test(subject_id){
  $.ajax({
    url: '/',
    type: 'post',
    data: {
      'action': 'run_test',
      'subject_id': subject_id
    },
    success: function(responce){
      window.location = '/test/'+responce.id
    },
    error: function(responce){
      console.log(2);
    }
  })
}

$('#add_question_modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) 
  var subject_id = button.data('subject-id')
  var subject_title = button.data('subject-title')

  var modal = $(this)
  modal.find('.modal-title').text('Добавить вопрос к дисциплине ' + subject_title)
  modal.find('.modal-footer button#add').attr('onclick', 'add_question('+subject_id+')')
})

function add_question(subject_id){
  $.ajax({
    url: '/',
    type: 'post',
    data: {
      'action': 'add_question',
      'subject_id': subject_id,
      'text': $([name=q_text]).val(),
      'answer': $([name=q_answer]).val(),
      'q_dop_1': $([name=q_dop_1]).val(),
      'q_dop_2': $([name=q_dop_2]).val(),
      'q_dop_3': $([name=q_dop_3]).val()
    },
    success: function(responce){
      $('#add_question_modal').modal('hide');
      $([name=q_text]).val('');
      $([name=q_answer]).val('');
      $([name=q_dop_1]).val('');
      $([name=q_dop_2]).val('');
      $([name=q_dop_3]).val('');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function add_question_1(subject_id){
  $.ajax({
    url: '/questions/'+subject_id,
    type: 'post',
    data: {
      'action': 'add_question',
      'subject_id': subject_id,
      'text': $([name=q_text]).val(),
      'answer': $([name=q_answer]).val(),
      'q_dop_1': $([name=q_dop_1]).val(),
      'q_dop_2': $([name=q_dop_2]).val(),
      'q_dop_3': $([name=q_dop_3]).val()
    },
    success: function(responce){
      $('#question_modal').modal('hide');
      $([name=q_text]).val('');
      $([name=q_answer]).val('');
      $([name=q_dop_1]).val('');
      $([name=q_dop_2]).val('');
      $([name=q_dop_3]).val('');
      $('#main-container').html(responce);
    },
    error: function(responce){
      console.log(2);
    }
  })
}