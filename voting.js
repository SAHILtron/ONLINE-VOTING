function redirect(party) {
    // Store party name in localStorage
    localStorage.setItem("selectedParty", party);

    // Redirect to thank_you.html
    window.location.href = "thank_you.html";
}

function redirect1() {
    redirect("CONGRESS");
}

function redirect2() {
    redirect("BJP");
}

function redirect3() {
    redirect("JDS");
}
