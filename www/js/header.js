

console.log(window.location.href);
hrefs = window.location.href.split("/");
console.log(hrefs);
first = "";
second = "";
siteFlag = false;
for (var i = 0; i < hrefs.length; i++) {
  if (hrefs[i] == "www") siteFlag = true;

  if (siteFlag) first += hrefs[i] + "/";
  else second += hrefs[i] + "/";
}
first = first.slice(0, -1);
second = second.slice(0, -1);




// HEADER
data = `
<div class="my-container header">
        <div>
          <div class="header-logo"> 
             <img class="logo" src="${second}/www/icons/logo.svg" alt="logo">
          </div>
        </div>
        <div>
          <div>
            <a href="${second}/www/index.html" class="header-text">
              Главная
            </a>  
          </div>
        </div>
</div>
`;

var header = document.createElement('header');
header.innerHTML = data;
var body = document.querySelector('body');


if (body) {
    body.insertBefore(header, body.firstChild);
} else console.error("no body -placeholder");



// FOOOTER
data = `
<div class="d-flex justify-content-around align-items-center border-top mt-5 my-container" style="margin-top: 30px;">
    <div class="d-flex flex-row text-muted justify-content-around mt-2">
      <div class="d-flex flex-column ">
      <p class="text-container text-center"><strong>Авторы:</strong></p>
        <p class="text-container">Слушатель факультета подготовки сотрудников для оперативных подразделений СПбУ МВД России, младший лейтенант полиции Зайцев И.С.</p>
        <p class="text-container">Слушатель факультета подготовки сотрудников для оперативных подразделений СПбУ МВД России, младший лейтенант полиции Бизин Р.В.</p>
        <p class="text-container">Слушатель факультета подготовки сотрудников для оперативных подразделений СПбУ МВД России, младший лейтенант полиции Рогова Ю.Н.</p>

        <p class="text-container">Доцент кафедры специальной и автомобильной техники СПбУ МВД России, к.т.н., подполковник полиции Мельников Н.М.</p>
        <p class="text-container"> Доцент кафедры физической подготовки и прикладных единоборств СПбУ МВД России, к.ю.н., полковник полиции Никишкин А.В</p>
      </div>
    </div>
    <div class="d-flex flex-column align-self-start mt-2 text-muted">
       <p class="text-container text-center"><strong>Руководитель проекта:</strong></p>
       <p class="text-container "> доцент кафедры специальной и автомобильной техники СПбУ МВД России, к.т.н., подполковник полиции Мельников Н.М.</p>
    </div>
  </div>
`;


footer = document.createElement('footer');

// Добавляем содержимое в элемент <header> (пример)
footer.innerHTML = data;

// Находим элемент <body>
body = document.querySelector('body');

// Если элемент <body> найден
if (body) {
    // Вставляем элемент <header> в начало <body>
    body.insertBefore(footer, body.lastChild);
} else console.error("no body -placeholder");

