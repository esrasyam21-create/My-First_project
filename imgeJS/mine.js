function SwitchImge(element) {
    const animalImage = document.querySelector("#animalImig");
    if (element.innerText.includes("SwitchImge To octove")){
    element.innerText = "switchImage To octov";
    animalImage.src = "octove.png";
    }
    else{
        element.innerText="SwitchImge To octove";
        animalImage.src = "octov.png";
    }

}