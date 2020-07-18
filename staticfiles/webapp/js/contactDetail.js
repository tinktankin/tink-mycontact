function tab(event, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("tab-detail");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("bar-item");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active-tab", "");
    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active-tab";
}