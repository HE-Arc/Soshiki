// From https://www.html5rocks.com/en/tutorials/dnd/basics/

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
