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
}

// دالة حذف العنصر (remove )تُستخدم لحذف زر Add Definition عند الضغط عليه)
function remove(element) {
    element.remove();
}

function showAlert(element) {
    // بنكتب جملة التنبيه المطلوب
    alert("The button was clicked");

    if (element.innerText.includes("13")) {
        // إذا كان زر ال 13 لايك: نغير البادينج إلى 20px
        element.style.padding = "20px";
    } 
    else if (element.innerText.includes("37")) {
        // إذا كان زر ال 37 لايك: نغير لون وحجم الحدود
        element.style.color = "blue";
        element.style.borderColor = "red";
        element.style.borderWidth = "5px";
    }
}

// دالة زيادة عدد الإعجابات للمنشور السفلي وتغيير ألوان الزر
var count = 3;
function addLike(element) {
    count++;
    document.querySelector("#likes").innerText = count;

    // تغيير لون نص الزر إلى الأحمر وخلفيته إلى الأزرق
    element.style.color = "red";
    element.style.backgroundColor = "blue";
}
