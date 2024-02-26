if (document.getElementsByClassName("content")[0].childElementCount > 0) {
    document.getElementsByClassName("lotto-form")[0].classList.add('hidden');
}

let previousValue = parseInt(document.getElementById('pagination-input').value);

function pageChange(input) {
    let newValue = parseInt(input.value);
    if ((newValue < 1) ^ (isNaN(newValue))) {
        newValue = 1;
        input.value = newValue;
    }

    let pages = parseInt(document.getElementById('pages-label').textContent);
    if (newValue > pages) {
        newValue = pages;
        input.value = newValue;
    }

    document.getElementById("page1").classList.add("hidden");

    let previousDraw = document.getElementById("page"+previousValue);
    previousDraw.classList.add("hidden");

    let nextDraw = document.getElementById("page"+newValue);
    nextDraw.classList.remove("hidden");

    previousValue = newValue;
}