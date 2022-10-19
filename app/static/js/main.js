var act = "profile";

function abrirTab(event, idTab) {
    var conteud = document.getElementsByClassName('content_tab');

    for (var i = 0; i < conteud.length; i++) {
        conteud[i].style.display = 'none';
    }

    var tabs = document.getElementsByClassName('tab_btn');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].className = tabs[i].className.replace('bt_activate', '');
    }


    document.getElementById(idTab).style.display = 'block';
    event.currentTarget.className += ' bt_activate';
    act = idTab;
}
