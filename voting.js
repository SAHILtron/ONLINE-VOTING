function redirect(party) {
    // Store party name in hidden input field (for form submission)
    document.getElementById("selectedParty").value = party;

    // Store party name in localStorage (optional)
    localStorage.setItem("selectedParty", party);

    // Submit form manually
    document.querySelector("form").submit();

    window.location.href = "thank_you.html";
}

function redirect1() {
    redirect("Unity Front Party (UFP)");
}

function redirect2() {
    redirect("Progressive People's Alliance (PPA)");
}

function redirect3() {
    redirect("Green Future Movement (GFM)");
}
