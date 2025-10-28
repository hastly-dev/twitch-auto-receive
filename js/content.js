(function() {
    'use strict';
    
    function waitForBonusButton() {
        console.log("Проверка загрузки функции получения");
        
        setInterval(() => {
            const button = document.querySelector('button[aria-label="Получить бонус"]');
            
            if (button) {
                
                // Проверяем, что кнопка видима и доступна
                if (button.offsetParent !== null && !button.disabled) {
                    button.click();
                    console.log("Баллы получены!");
                }
                
            }

        }, 1000); // Проверяем каждую секунду
    }
    
    // Запускаем поиск после загрузки страницы
    window.addEventListener('load', function() {
        chrome.storage.sync.get(['takePoints'], (result) => {
            if (result.takePoints) {
                waitForBonusButton();
                console.log('Скрипт заинжектен');
            }
        });
    });
    
})();