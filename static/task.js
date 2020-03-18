function remove_task(event) {
    const id = event.target.parentNode.id
    fetch('/remove/' + id).then(response => window.location.reload())
}
// window.location Получает/устанавливает URL окна и его компоненты
// reload([forceget]) перезагрузить документ по текущему URL. Аргумент forceget - булево значение, если оно true, то документ перезагружается всегда с сервера, если false или не указано, то браузер может взять страницу из своего кэша.

function toggalModal(event) {
    const el = document.getElementsByTagName('form')[0]
    el.style.display = 'block'
}

const a = document.getElementById('form-toggler')
a.addEventListener('click', toggalModal)