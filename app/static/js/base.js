const language = document.getElementById("language");
const languageSelect = document.getElementById("lang-select");

languageSelect.addEventListener("change", () => {
    language.innerHTML = `${languageSelect.options[languageSelect.selectedIndex].text}`;
})