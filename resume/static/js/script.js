document.addEventListener("DOMContentLoaded", () => {
    const phrases = [
        "",
        "",
        "",
        "",
    ];

    const typingSpeed = 100;
    const pauseBetweenPhrases = 2000;

    let currentPhraseIndex = 0;
    let currentCharIndex = 0;
    const typingElement = document.getElementById("typing-effect");

    const typeText = () =>{
        if(currentCharIndex < phrases[currentPhraseIndex].length){
            typingElement.textContent += phrases[currentPhraseIndex].charAt(currentCharIndex);
            currentCharIndex++;
            setTimeout(typeText, typingSpeed);
        } else{
            setTimeout(deleteText, pauseBetweenPhrases);
        }
    };

    const deleteText = () =>{

    }
})