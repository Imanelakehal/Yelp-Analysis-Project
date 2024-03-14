let countries = ["Sichuan ", "Shanghai", "Beijing", "Guangzhou", "Chengdu", "Hangzhou", "Xi'an", "Shenzhen"];
let sortedCountries = countries.sort();
let input = document.getElementById("input");
let suggestionsContainer = document.querySelector(".suggestions-container");

input.addEventListener("keyup", (e) => {
    removeElements(); // Remove existing list items before adding new ones
    for (let i of sortedCountries) {
        if (i.toLowerCase().startsWith(input.value.toLowerCase()) && input.value != "") {
            let listItem = document.createElement("li");
            listItem.classList.add("list-item");
            listItem.textContent = i;
            listItem.addEventListener("click", () => {
                input.value = i;
                suggestionsContainer.innerHTML = ''; // Clear suggestions after clicking
            });
            suggestionsContainer.appendChild(listItem);
        }
    }
});

function removeElements() {
    suggestionsContainer.innerHTML = '';
}
