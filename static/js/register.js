const typeSelect = document.querySelector('#id_type');
const usernameInput = document.querySelector('#id_username');

typeSelect.addEventListener('change', () => {
    const selectedOption = typeSelect.options[typeSelect.selectedIndex].value;
    if (selectedOption === 'Компания') {
        usernameInput.placeholder = 'Имя компании';
    } else {
        usernameInput.placeholder = 'Имя пользователя';
    }
});