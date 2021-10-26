
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


// The code for login with Local Storage
let submitForm = document.getElementById('login')
submitForm.addEventListener('submit', function(e){
    e.preventDefault();
    let username = document.getElementById("lg-username").value;
    let password = document.getElementById("lg-password").value;
    let error = document.getElementById("#error");
    console.log(username, password)
    if(username == localStorage.getItem("sg-username") && password == localStorage.getItem('sg-password'))
    {
        location.href = '../innerpage.html';
    } else {
        alert('Wrong Credentials!')
    }
})

// Sign-up Code with Local Storage
let signupForm = document.getElementById('signup');
signupForm.addEventListener('submit', function(e){
    e.preventDefault();
    let signUser = document.getElementById('sg-username').value;
    let signEmail = document.getElementById('sg-email').value
    let signPassword = document.getElementById('sg-password').value;
    let error = document.getElementById('#error');
    console.log(signUser, signPassword, signEmail);
    // if(signUser == localStorage.getItem("sg-username")){
    //     alert("Username is already used please try another one")
    //     document.getElementById('sg-username').value = " ";
    //     document.getElementById('sg-email').value = " ";
    //     document.getElementById('sg-password').value = " ";
    // }
    if(signEmail == localStorage.getItem('sg-email')){
        alert("Email already exists")
        document.getElementById('sg-email').value = " ";
    }

    if(signUser != localStorage.getItem('sg-username') && signPassword.length >= 8){
        localStorage.setItem("sg-username", signUser);
        localStorage.setItem("sg-email", signEmail)
        localStorage.setItem("sg-password", signPassword);
        console.log(localStorage.getItem("sg-username","sg-email",'sg-password'))
        alert('Credentials Saved!');
        location.reload()
        document.getElementById('sg-username').value = " ";
        document.getElementById('sg-email').value = " ";
        document.getElementById('sg-password').value = " ";
    }
    else { 
        alert('Error! Username already exist');
        document.getElementById('sg-username').value = '';
        document.getElementById('sg-email').value = "";
        document.getElementById('sg-password').value = "";
    }
})

