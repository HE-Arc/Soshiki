// From https://www.html5rocks.com/en/tutorials/dnd/basics/
$('#reorder-btn').click(function () {
  $(this).toggle();
  $('#save-reorder-btn').toggle();

  var elems = document.querySelectorAll('.card-columns div');
  [].forEach.call(elems, function (elem) {
    elem.classList.add('draggable-card');
    elem.setAttribute('draggable', true);
  });

  var cards = document.querySelectorAll('.draggable-card');

  var dragSrcEl = null;

  function handleDragStart(e) {
    // Target (this) element is the source node.
    // this.style.opacity = '0.4';

    dragSrcEl = this;

    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', this.innerHTML);
  }

  function handleDragOver(e) {
    if (e.preventDefault) {
      e.preventDefault(); // Necessary. Allows us to drop.
    }

    e.dataTransfer.dropEffect = 'move';  // See the section on the DataTransfer object.

    return false;
  }

  function handleDragEnter(e) {
    // this / e.target is the current hover target.
    this.classList.add('hover');
  }

  function handleDragLeave(e) {
    this.classList.remove('hover');  // this / e.target is previous target element.
  }

  function handleDrop(e) {
    // this/e.target is current target element.

    if (e.stopPropagation) {
      e.stopPropagation(); // Stops some browsers from redirecting.
    }

    // Don't do anything if dropping the same column we're dragging.
    if (dragSrcEl != this) {
      // Set the source column's HTML to the HTML of the column we dropped on.
      dragSrcEl.innerHTML = this.innerHTML;
      this.innerHTML = e.dataTransfer.getData('text/html');
    }

    return false;
  }

  function handleDragEnd(e) {
    // this/e.target is the source node.

    [].forEach.call(cards, function (card) {
      card.classList.remove('hover');
    });
  }

  [].forEach.call(cards, function(card) {
    card.addEventListener('dragstart', handleDragStart, false);
    card.addEventListener('dragenter', handleDragEnter, false);
    card.addEventListener('dragover', handleDragOver, false);
    card.addEventListener('dragleave', handleDragLeave, false);
    card.addEventListener('drop', handleDrop, false);
    card.addEventListener('dragend', handleDragEnd, false);
  });
});

$('#save-reorder-btn').click(function () {
  $(this).toggle();
  $('#reorder-btn').toggle();

  var arrayIDs = [];
  var elems = document.querySelectorAll('.draggable-card');
  [].forEach.call(elems, function (elem) {
    arrayIDs.push($(elem).children('h5').attr('id'));
    elem.classList.remove('draggable-card');
    elem.setAttribute('draggable', false);
  });
  arrayIDs = jQuery.grep(arrayIDs, function(n) { return (n); });
  var csrftoken = getCookie('csrftoken');

  //Ajax
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  $.ajax({
    method: 'POST',
    url: '/tables/reorder-lists',
    data: {
      'arrayIDs': arrayIDs
    },
    success: function (data) {
      // pass
    },
    error: function (data) {
      // pass
    }
  });
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
