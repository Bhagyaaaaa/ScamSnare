const form = document.getElementById('scamForm');
const inputText = document.getElementById('inputText');
const inputFile = document.getElementById('inputFile'); // new file input
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData();
    const file = inputFile.files[0];  // check if file is uploaded
    const text = inputText.value.trim();  // get text input

    if (file) {
        formData.append('file', file);  // if file is uploaded, send file
    } else if (text.length > 0) {
        formData.append('link', text);  // if no file, but text entered, send text
    } else {
        resultDiv.textContent = "Please enter a link or upload a file.";
        resultDiv.style.color = "red";
        return;
    }

    try {
        const response = await fetch('http://localhost:8000/check', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.result === "Fake") {
            resultDiv.textContent = "Warning! Scam detected.";
            resultDiv.style.color = "red";
        } else if (data.result === "Real") {
            resultDiv.textContent = "Looks Safe!";
            resultDiv.style.color = "green";
        } else {
            resultDiv.textContent = "Something went wrong.";
            resultDiv.style.color = "orange";
        }
    } catch (error) {
        console.error(error);
        resultDiv.textContent = "Error connecting to server.";
        resultDiv.style.color = "orange";
    }
});
