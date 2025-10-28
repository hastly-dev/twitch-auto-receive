const checkBox = document.querySelector('.checkbox');
const statuse = document.getElementById('status');

chrome.storage.sync.get(['takePoints'], (result) => {
    checkBox.checked = result.takePoints;
    if (result.takePoints) {
        chrome.action.setBadgeText({text: 'ON'});
        statuse.classList.remove('inactive');
        statuse.classList.add('active');
        statuse.innerHTML = '✅ Активен';
    } else {
        statuse.classList.remove('active');
        statuse.classList.add('inactive');
        statuse.innerHTML = '❌ Неактивен';
    }
});

if (checkBox) {
    checkBox.addEventListener('click', async (e) => {
        const checked = e.target.checked;
        chrome.action.setBadgeText({text: checked ? 'ON' : ''});
        chrome.storage.sync.set({takePoints: checked});
        if (checked) {
            statuse.classList.remove('inactive');
            statuse.classList.add('active');
            statuse.innerHTML = '✅ Активен';
        } else {
            statuse.classList.remove('active');
            statuse.classList.add('inactive');
            statuse.innerHTML = '❌ Неактивен';
        }
    });
}