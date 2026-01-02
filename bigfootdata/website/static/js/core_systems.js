"use strict";
let mobile_panel_button = document.getElementById("mobile_button");
if (mobile_panel_button) {
    mobile_panel_button.addEventListener('click', function () {
        const mobile_panel = document.createElement('div');
        let current_year = document.getElementById("currentYear");
        let current_year_value = current_year.value;
        console.log('aj');
        mobile_panel.id = 'mobile_panel_ID';
        let html_string = `
    <div id="xbutton_mobile_panel" ><button onclick="close_mobile_panel()">x</button></div>
    <h1>Bigfoot Research and Sightings</h1>
        
        <div id="mobile_panel_links">
            <a href="#">Donate</a>
            <a href="#">Research</a>
            <a href="#">Sightings</a>
            <a href="#">Audios</a>
            <a href="#">Videos</a>
            <a href="#">Contact</a>
        </div>

        <hr>

        <div id="button_panel">
            <img src="/static/images/125753-200.png" alt="big foot">
            <small>Copyright © 1995 - ${current_year_value} <span>BFRO</span>. All rights reserved.</small>
        </div>
    `;
        mobile_panel.innerHTML = html_string;
        document.body.appendChild(mobile_panel);
    });
}
;
function close_mobile_panel() {
    let mobile_panel = document.getElementById("mobile_panel_ID");
    document.body.removeChild(mobile_panel);
}
