

let mobile_panel_button: any = document.getElementById("mobile_button");



if (mobile_panel_button) {
    mobile_panel_button.addEventListener('click', function() {

    //. than make message pop up, fixed position and disappears in 3 seconds
    const mobile_panel = document.createElement('div');

    let current_year: any = document.getElementById("currentYear");
    let current_year_value: string = current_year.value;

    console.log('aj')

    // Add an ID to the <div> for easier management
    mobile_panel.id = 'mobile_panel_ID';

    let html_string: string = `
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

    // Append the <div> to the body
    document.body.appendChild(mobile_panel);
    })


};



function close_mobile_panel(): void {
    let mobile_panel: any = document.getElementById("mobile_panel_ID");
    document.body.removeChild(mobile_panel);
}