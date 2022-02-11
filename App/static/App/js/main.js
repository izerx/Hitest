function init(){
  flatpickr.localize(flatpickr.l10ns.ru);

  flatpickr(".datepicker", {
    altInput: true,
    altFormat: "j F Y года",
    dateFormat: "d-m-Y",
  });
  flatpickr(".datepicker.show-date", {
    altInput: true,
    altFormat: "j F Y года",
    dateFormat: "d-m-Y",
    defaultDate: "today"
  });
  flatpickr(".timepicker", {
      enableTime: true,
      noCalendar: true,
      dateFormat: "H:i",
      time_24hr: true
  });
}

function render_release() {
  $('#main-container').html('<main class="pt-5 mx-lg-5 w-100 h-fill"><div class="container-fluid mt-5 w-100 h-fill"><table class="w-100 h-fill"><tr><td class="align-middle" align="center">'+
            '<div class="d-flex justify-content-center"><div class="spinner-border text-primary" style="width: 3rem; height: 3rem;" role="status"><span class="sr-only">Loading...</span></div>'+
            '</div></td></tr></table></div></main>')
  show_date = $('.datepicker.show-date').val()
  console.log(show_date)
  $.ajax({
    url: '/',
    type: 'post',
    data: {
      action: 'show_list',
      show_date: show_date
    },
    success: function(responce){
      $('#main-container').html(responce)
    },
    error: function(responce){
      console.log(2);
      $('#main-container').html('')
    }
  })
}

$('.datepicker').on('change', function(){
  render_release()
})

$(document).ready(function(){
  init()
})

$('.modal.timeout').on('show.bs.modal', function (event) {
  setTimeout(function(){$('.modal.timeout').modal('hide')}, 2000)
})

function add_to_release(){
  $.ajax({
    url: '/creator/',
    type: 'post',
    data: $('#list_form').serialize() + '&action=add_to_release',
    success: function(responce){
      console.log(1);
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function set_release(){
  var checkbox = $('input[type=checkbox]').toArray()
  var data = 'release_id='+$('input[name=release_id]').val()+'&action=set_release&id='
  for(var i = 0; i < checkbox.length; i++){
    if(checkbox[i].checked){
      data = data + $(checkbox[i]).attr('data-id')+','
    }
  }
  $.ajax({
    url: '/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container').html(responce)
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function add_to_release_multi(){
  var checkbox = $('input[type=checkbox]').toArray()
  var data = 'action=add_to_release_multi&id='
  for(var i = 0; i < checkbox.length; i++){
    if(checkbox[i].checked){
      data = data + $(checkbox[i]).attr('data-id')+','
    }
  }
  $.ajax({
    url: '/templates/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#add_to_release_success_modal').modal('show')
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function delete_templates(){
  var checkbox = $('input[type=checkbox]').toArray()
  var data = 'action=delete_templates&id='
  for(var i = 0; i < checkbox.length; i++){
    if(checkbox[i].checked){
      data = data + $(checkbox[i]).attr('data-id')+','
    }
  }
  $.ajax({
    url: '/templates/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container-template').html(responce)
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function download_multi(){
  var date = $('.datepicker').val()
  var checkbox = $('input[type=checkbox]').toArray()
  var data = 'date='+date+'&action=download_multi&id='
  for(var i = 0; i < checkbox.length; i++){
    if(checkbox[i].checked){
      data = data + $(checkbox[i]).attr('data-id')+','
    }
  }
  $.ajax({
    url: '/',
    type: 'post',
    data: data,
    success: function(responce){

    },
    error: function(responce){
      console.log(2);
    }
  })
}

function download(id){
  $.ajax({
    url: '/templates/'+id,
    type: 'post',
    data: {
      download: '1',
      id: id
    },
    success: function(responce){
      document.location.href='/media/docx/'+id+'.docx'
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function save(id){
  var data = $('#list_form').serialize() + '&save=1&id='+id
  $.ajax({
    url: '/templates/'+id,
    type: 'post',
    data: data,
    success: function(responce){
      console.log(1);
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function remove_rider(){
  var checkbox = $('input[type=checkbox]').toArray()
  var data = 'action=remove&id='
  for(var i = 0; i < checkbox.length; i++){
    if(checkbox[i].checked){
      data = data + $(checkbox[i]).attr('data-id')+','
    }
  }
  $.ajax({
    url: '/riders/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container-rider').html(responce);
      $('#remove_rider_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function add_rider(){
  var data = $('#add_rider_form').serialize() + '&action=add'
  $.ajax({
    url: '/riders/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container-rider').html(responce);
      $('#add_rider_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

// function delete_template(id){
//   $.ajax({
//     url: '/riders/',
//     type: 'post',
//     data: {
//       delete_template: '1',
//       id: id,
//     },
//     success: function(responce){
//       $('#main-container').html(responce);
//       $('#add_rider_modal').modal('hide');
//     },
//     error: function(responce){
//       console.log(2);
//     }
//   })
// }

function remove_auto(){
  var checkbox = $('input[type=checkbox]').toArray()
  var data = 'action=remove&id='
  for(var i = 0; i < checkbox.length; i++){
    if(checkbox[i].checked){
      data = data + $(checkbox[i]).attr('data-id')+','
    }
  }
  $.ajax({
    url: '/autopark/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container-auto').html(responce);
      $('#remove_auto_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function add_auto(){
  var data = $('#add_auto_form').serialize() + '&action=add'
  $.ajax({
    url: '/autopark/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container-auto').html(responce);
      $('#add_auto_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function remove_distation(){
  var checkbox = $('input[type=checkbox]').toArray()
  var data = 'action=remove&id='
  for(var i = 0; i < checkbox.length; i++){
    if(checkbox[i].checked){
      data = data + $(checkbox[i]).attr('data-id')+','
    }
  }
  $.ajax({
    url: '/distations/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container-dist').html(responce);
      $('#remove_distation_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function add_distation(){
  var data = $('#add_distation_form').serialize() + '&action=add'
  $.ajax({
    url: '/distations/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#main-container-dist').html(responce);
      $('#add_distation_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function save_list(){
  var data = $('#list_form').serialize() + '&action=add_to_template'
  $.ajax({
    url: '/creator/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#success_save_modal').modal('show');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function update_company(){
  var data = $('#company_form').serialize() + '&company_update=1'
  $.ajax({
    url: '/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#success_request_modal').modal('show')
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function add_fin_income(){
  var data = $('#add_fin_income_form').serialize() + '&action=add_income'
  $.ajax({
    url: '/finance/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#fin_income_tbody').html(responce);
      $('#add_fin_income_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

function add_fin_outcome(){
  var data = $('#add_fin_outcome_form').serialize() + '&action=add_outcome'
  $.ajax({
    url: '/finance/',
    type: 'post',
    data: data,
    success: function(responce){
      $('#fin_outcome_tbody').html(responce);
      $('#add_fin_outcome_modal').modal('hide');
    },
    error: function(responce){
      console.log(2);
    }
  })
}

$('#fin_income').DataTable({
  "language": {
      "search": "Поиск",
      "lengthMenu": "Показать _MENU_ записей на странице",
      "zeroRecords": "Нет поступлений средств",
      "info": "_PAGE_ из _PAGES_ страниц",
      "infoFiltered": "(filtered from _MAX_ total records)",
      "paginate": {
        "next": "Вперед",
        "previous": "Назад"
      }
  }
});

$('#fin_outcome').DataTable({
  "language": {
      "search": "Поиск",
      "lengthMenu": "Показать _MENU_ записей на странице",
      "zeroRecords": "Нет расходов",
      "info": "_PAGE_ из _PAGES_ страниц",
      "infoFiltered": "(filtered from _MAX_ total records)",
      "paginate": {
        "next": "Вперед",
        "previous": "Назад"
      }
  }
});
$('.dataTables_length').addClass('bs-select');

function change_pass_success()
{
  $('#success_change_pass_modal').modal('show');
  $('#id_old_pass').val('');
  $('#id_new_pass').val('');
  $('#id_confirm_pass').val('');
}
