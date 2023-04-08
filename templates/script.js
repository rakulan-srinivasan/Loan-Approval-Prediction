function slider(get){
    const mySlider = document.getElementById("my-slider");
    const sliderValue = document.getElementById("slider-value");
    var valPercent = mySlider.value;
    console.log(valPercent);
    mySlider.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue.textContent = mySlider.value;
};
