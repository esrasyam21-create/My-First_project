
// دالة تغيير نص زر الدخول والخروج عند الضغط عليه
function changeInnerTxt(element) {
    if (element.innerText == "Login") {
        element.innerText = "Logout";
        console.log("buttonLogout");
    }
    else if (element.innerText == "Logout") {
        element.innerText = "Login";
        console.log("buttonLogin");
    }
};

function remove(element) {
    element.remove();
};

function showAlert() {
    alert("Ninja was liked!");
};

// دالة زيادة عدد الإعجابات للمنشور السفلي
var count = 3;
function addLike() {
    count++;
    document.querySelector("#likes").innerText = count;
};
