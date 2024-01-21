let darkThemeButton = document.querySelector('.theme-button-dark');
let lightThemeButton = document.querySelector('.theme-button-light');
let serifFontButton = document.querySelector('.font-button-serif');
let sansSerifFontButton = document.querySelector('.font-button-sans-serif');

darkThemeButton.onclick = function () {
  document.body.classList.add('dark');
  darkThemeButton.classList.add('active');
  lightThemeButton.classList.remove('active');
};

lightThemeButton.onclick = function () {
  document.body.classList.remove('dark');
  lightThemeButton.classList.add('active');
  darkThemeButton.classList.remove('active');
};

// Добавьте обработчик включения шрифта с засечками сюда
serifFontButton.onclick = function () {
    document.body.classList.add('serif');
    sansSerifFontButton.classList.remove('active');
    serifFontButton.classList.add('active');
}

sansSerifFontButton.onclick = function () {
  // код переключения шрифта
  document.body.classList.remove('serif');
  sansSerifFontButton.classList.add('active');
  serifFontButton.classList.remove('active');
};
