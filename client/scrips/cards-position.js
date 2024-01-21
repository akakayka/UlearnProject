/* Элементы кнопок-переключателей раскладки */
let tileViewButton = document.querySelector('.card-view-button-grid');
let standardViewButton = document.querySelector('.card-view-button-list');

/* Элемент списка карточек */
let cardsList = document.querySelector('.cards');

tileViewButton.onclick = function () {
  cardsList.classList.remove('list');
  tileViewButton.classList.add('active');
  standardViewButton.classList.remove('active');
};

standardViewButton.onclick = function () {
  cardsList.classList.add('list');
  tileViewButton.classList.remove('active');
  standardViewButton.classList.add('active');
};
