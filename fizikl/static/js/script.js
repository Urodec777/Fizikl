// picking necessary elements
let date = document.querySelector('#date')
let define = document.querySelector('#define')
let section = document.querySelector('section')

// initializing flatpickr to make scheduler for comfortable usage
flatpickr("#date", {
    dateFormat: 'd / m / Y',
    minDate: '1 / 01 / 2018',
    "locale": "ru",
    allowInput: true // defining this key to allow user to input date
});
define.addEventListener('click', () => {
    $.ajax({
        url: '/ajax/',
        type: 'GET',
        data: {
            'date': date.value // sending date's value to ajax function in views.py
        },
        success: (data) => {
            // insertion valid data
            section.innerHTML = `<span class="info">
                <span style="display: flex; align-items:center; gap:5px; color:white;"> Выбранная дата: <p class="user_date">${date.value}</p> </span>
                <span style="display: flex; align-items:center; gap:5px; color:white;"> Находится на: <p class="week_number">${data}</p> неделе </span>
            </span>`
        },
        error: (error) => {
            // Cleaning console for beauty of console
            console.clear()

            // insertion invalid data
            section.innerHTML = `<span class="info_error">
                <span style="display: flex; align-items:center; gap:5px; color:white;"> Выбранная дата: <p class="user_date">${date.value}</p> </span>
                <span style="display: flex; align-items:center; gap:5px; color:white;"> Не является верной, пожалуйста не обманывайте систему)</span>
            </span>`
        }
    })
})