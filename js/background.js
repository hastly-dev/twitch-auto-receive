chrome.runtime.onInstalled.addListener(async () => {
    chrome.storage.sync.get(['takePoints'], (result) => {
        if (result.takePoints) {
            chrome.action.setBadgeText({text: 'ON'});
        }
    });
});