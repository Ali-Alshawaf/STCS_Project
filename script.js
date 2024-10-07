async function processImage() {
    const imageUrl = document.getElementById('image-url-input').value;

    if (!imageUrl) {
        alert('Please enter an image URL.');
        return;
    }

    const apiKey = "sk-proj-b9LCuHKYsYZKlX2gztA3T3BlbkFJxtoUpiTFZMMNFK6p9FFB"; // Replace with your actual API key
    const endpoint = "https://api.openai.com/v1/chat/completions";
    const headers = {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${apiKey}`
    };

    const payload = {
        "model": "gpt-4-turbo",
        messages: [
            {
                role: "user",
                content: [
                    { type: "text", text: "اكتب ملخص في 30 كلمة, هل هذه الارض صالحة للزراعة ام لا لا وما هي صفات التربة؟" },
                    {
                        type: "image_url",
                        image_url: {
                            "url": imageUrl 
                        },
                    },
                ],
            },
        ],
        "max_tokens": 200
    };

    axios.post(endpoint, payload, { headers })
        .then(response => {
            setTimeout(() => {
                const output = response.data.choices[0].message.content;
                document.getElementById('reply-content').innerText = output;
                console.log(output)

                const mainContainer = document.getElementById('main-container');
                mainContainer.style.backgroundImage = `url(${imageUrl})`;
                mainContainer.style.backgroundSize = 'cover'; // Optional for better fit
                mainContainer.style.backgroundRepeat = 'no-repeat'; // Optional to avoid tiling

            }, 7000);
        })
        .catch(error => {
            console.error(error);
            document.getElementById('reply-content').innerText = 'Error: Could not process the image URL.';
        });
}

const submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click', processImage);
