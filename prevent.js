document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
});

// Disable specific key combinations
document.addEventListener('keydown', function (e) {
    // Disable F12
    if (e.key === 'F12') {
        e.preventDefault();
    }
    // Disable Ctrl + Shift + I
    if ((e.ctrlKey && e.shiftKey && e.key === 'I') || (e.ctrlKey && e.shiftKey && e.key === 'i')) {
        e.preventDefault();
    }
    // Disable Ctrl + Shift + J (for console)
    if ((e.ctrlKey && e.shiftKey && e.key === 'J') || (e.ctrlKey && e.shiftKey && e.key === 'j')) {
        e.preventDefault();
    }
    // Disable Ctrl + U (to prevent viewing source code)
    if ((e.ctrlKey && e.key === 'U') || (e.ctrlKey && e.key === 'u')) {
        e.preventDefault();
    }
});

