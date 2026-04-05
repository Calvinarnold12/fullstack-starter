document.addEventListener('DOMContentLoaded', () => {
    // Grab all cards and all valid drop zones (piles)
    const cards = document.querySelectorAll('.card');
    const piles = document.querySelectorAll('.pile');

    // Add drag listeners to every card
    cards.forEach(card => {
        card.addEventListener('dragstart', dragStart);
        card.addEventListener('dragend', dragEnd);
    });

    // Add drop listeners to every pile
    piles.forEach(pile => {
        pile.addEventListener('dragover', dragOver);
        pile.addEventListener('dragenter', dragEnter);
        pile.addEventListener('dragleave', dragLeave);
        pile.addEventListener('drop', dragDrop);
    });
});

let draggedCard = null;

// --- CARD DRAG FUNCTIONS ---
function dragStart(e) {
    draggedCard = this;
    // Slight delay so the drag image stays visible while the original hides
    setTimeout(() => this.classList.add('dragging'), 0);
}

function dragEnd(e) {
    this.classList.remove('dragging');
    draggedCard = null;
}

// --- PILE DROP FUNCTIONS ---
function dragOver(e) {
    e.preventDefault(); // REQUIRED to allow dropping!
}

function dragEnter(e) {
    e.preventDefault();
    this.style.backgroundColor = 'rgba(255, 255, 255, 0.2)'; // Highlight pile when hovering
}

function dragLeave(e) {
    this.style.backgroundColor = 'transparent'; // Remove highlight
}

function dragDrop(e) {
    this.style.backgroundColor = 'transparent';
    this.append(draggedCard); // Physically moves the card HTML into the new pile!
}